from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from account import models as amod
from catalog import models as cmod
import datetime


@view_function
@permission_required('catalog.change_product', login_url='/')
def process_request(request):
  '''Lists the products in a table on the screen'''
  # pull all products
  products = cmod.Product.objects.all()
  
  # order it case insensitively (thanks to stackoverflow for this)
  products = products.extra(select={'lower_name':'lower(name)'}).order_by('lower_name')
    
  template_vars = {
    'products': products
  }
  return dmp_render(request, 'products.html', template_vars)
  
  
  
###################################################################
###   Ajax endpoint to get the updated quantity for an item  

@view_function
@permission_required('catalog.change_product', login_url='/')
def get_quantity(request):
  '''Edits a product'''
  # get the product
  try:
    product = cmod.BulkProduct.objects.get(id=request.urlparams[0])
  except cmod.Product.DoesNotExist:
    return Http404() # not found response
   
  # return the quantity in a response
  return HttpResponse(product.quantity)
  
  
  
######################################################
###   Creating a product

@view_function
@permission_required('catalog.add_product', login_url='/')
def create(request):
  '''Creates a product'''
  # process the form
  form = CreateForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateForm(request.POST)
    if form.is_valid():
      # create the correct product
      product = cmod.create_product(form.cleaned_data.get('ptype'))
        
      # set general product fields
      product.name = form.cleaned_data.get('name')
      product.description = form.cleaned_data.get('description')
      # image taken out per S4 requirements
      # product.image = form.cleaned_data.get('image')
      product.price = form.cleaned_data.get('price')
      product.category = form.cleaned_data.get('category')
      
      # set specific fields (this could better be done with class methods)
      if form.cleaned_data.get('ptype') == 'RentalProduct':
        product.status = form.cleaned_data.get('status')
      elif form.cleaned_data.get('ptype') == 'IndividualProduct':
        product.creator = form.cleaned_data.get('creator')
        product.ind_status = form.cleaned_data.get('ind_status')
      elif form.cleaned_data.get('ptype') == 'BulkProduct':
        product.quantity = form.cleaned_data.get('quantity')
      
      # save and return
      product.save()
      return HttpResponseRedirect('/manager/products/')

  # return the form
  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'products.create.html', template_vars)


class CreateForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  description = forms.CharField(label='Description', required=False, max_length=100, widget=forms.Textarea(attrs={ 'class': 'form-control' }))  
  # image taken out per S4 requirements
  # image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  category = forms.ModelChoiceField(label='Category', queryset=cmod.Category.objects.order_by('name'), required=True, widget=forms.Select(attrs={ 'class': 'form-control' }))  
  price = forms.DecimalField(label="Price", required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  ptype = forms.ChoiceField(label="Product Type", required=True, choices=cmod.PRODUCT_SUBCLASSES, widget=forms.Select(attrs={ 'class': 'form-control' }))  
  purchase_date = forms.DateField(label='Purchase Date', required=False, input_formats=[ '%Y-%m-%d %H:%M:%S' ], widget=forms.TextInput(attrs={ 'class': 'form-control RentalProductField' }))  
  status = forms.ChoiceField(label="Status", required=False, choices=cmod.RENTAL_STATUS_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control RentalProductField' }))  
  creator = forms.ModelChoiceField(label='Creator', queryset=amod.User.objects.order_by('last_name', 'first_name'), required=False, widget=forms.Select(attrs={ 'class': 'form-control IndividualProductField' }))  
  ind_status = forms.ChoiceField(label="Status", required=False, choices=cmod.INDIVIDUAL_STATUS_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control IndividualProductField' }))  
  quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.NumberInput(attrs={ 'class': 'form-control BulkProductField' }))  




######################################################
###   Editing a product

@view_function
@permission_required('catalog.change_product', login_url='/')
def edit(request):
  '''Edits a product'''
  # get the product
  try:
    product = cmod.Product.objects.get(id=request.urlparams[0])
  except cmod.Product.DoesNotExist:
    return HttpResponse('/manager/products/')
  
  # figure out which form to create
  form_class = PRODUCT_EDIT_FORMS[product.__class__.__name__]
  
  # process the form
  form = form_class(initial=model_to_dict(product))
  if request.method == 'POST':  # just submitted the form
    form = form_class(request.POST)
    if form.is_valid():
      form.set_data(product)
      product.save()
      return HttpResponseRedirect('/manager/products/')

  # render the template
  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'products.edit.html', template_vars)



class EditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control AllProductField' }))  
  description = forms.CharField(label='Description', required=False, max_length=1000, widget=forms.Textarea(attrs={ 'class': 'form-control AllProductField' }))  
  # image taken out per S4 requirements
  # image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control AllProductField' }))  
  price = forms.DecimalField(label="Price", required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  category = forms.ModelChoiceField(label='Category', queryset=cmod.Category.objects.order_by('name'), required=True, widget=forms.Select(attrs={ 'class': 'form-control AllProductField' }))  
  
  def set_data(self, product):
    '''Sets the common data in the form cleaned_data dict to the given product'''
    product.name = self.cleaned_data.get('name')
    product.description = self.cleaned_data.get('description')
    # image taken out per S4 requirements
    # product.image = self.cleaned_data.get('image')
    product.price = self.cleaned_data.get('price')
    product.category = self.cleaned_data.get('category')
    
  
class RentalProductEditForm(EditForm):  
  purchase_date = forms.DateField(label='Purchase Date', required=False, input_formats=[ '%Y-%m-%d %H:%M:%S' ], widget=forms.TextInput(attrs={ 'class': 'form-control RentalProductField' }))  
  status = forms.ChoiceField(label="Status", required=False, choices=cmod.RENTAL_STATUS_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control RentalProductField' }))  

  def set_data(self, product):
    '''Sets the data in the form cleaned_data dict to the given product'''
    super().set_data(product)
    product.purchase_date = self.cleaned_data.get('purchase_date')
    product.status = self.cleaned_data.get('status')

  
class IndividualProductEditForm(EditForm):
  creator = forms.ModelChoiceField(label='Creator', queryset=amod.User.objects.order_by('last_name', 'first_name'), required=False, widget=forms.Select(attrs={ 'class': 'form-control IndividualProductField' }))  

  def set_data(self, product):
    '''Sets the data in the form cleaned_data dict to the given product'''
    super().set_data(product)
    product.creator = self.cleaned_data.get('creator')

  
class BulkProductEditForm(EditForm):
  quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.NumberInput(attrs={ 'class': 'form-control BulkProductField' }))  

  def set_data(self, product):
    '''Sets the data in the form cleaned_data dict to the given product'''
    super().set_data(product)
    product.quantity = self.cleaned_data.get('quantity')


PRODUCT_EDIT_FORMS = {
  'RentalProduct': RentalProductEditForm,
  'IndividualProduct': IndividualProductEditForm,
  'BulkProduct': BulkProductEditForm,
}



######################################
###   Delete product

@view_function
@permission_required('catalog.delete_product', login_url='/')
def delete(request):
  '''Deletes a product'''
  try:
    product = cmod.Product.objects.get(id=request.urlparams[0])
  except cmod.Product.DoesNotExist:
    return HttpResponseRedirect('/manager/products/')
    
  # delete the user
  product.delete()
  
  # redirect
  return HttpResponseRedirect('/manager/products/')


