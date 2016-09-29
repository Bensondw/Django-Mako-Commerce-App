from django.conf import settings
from django_mako_plus import view_function
from django.forms import extras
from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod
from CHF.customform import CustomForm
from django.contrib.contenttypes.models import ContentType
# from . import initialize_template_vars, add_new, list_viewed



LAST_FIVE_KEY = 'last5productsviewed'





@view_function
def process_request(request):	

	categories = cmod.Category.objects.all()

	# if not request.urlparams[0]:
	# 	return HttpResponseRedirect("/catalog/index/")

	# 	# this is kind of reduntant to have two if statements
	# if request.urlparams[0]:
	# 	product = cmod.Product.objects.get(id=request.urlparams[0])  


	cart = request.shopping_cart.get_items()

	
	
	template_vars = {
		# 'product': product,
		'categories': categories,
		'cart': cart,
	}

	
	return dmp_render(request, 'cart.html', template_vars)

@view_function
def remove(request):
	'''removes the item from the cart'''
	try: 
		product = cmod.Product.objects.get(id=request.urlparams[0])		
	except cmod.Product.DoesNotExist:
		return Http404()

	request.shopping_cart.remove_item(product)

	return HttpResponseRedirect('/catalog/cart/')


@view_function
def add(request):
	'''shows the add form called via ajax'''
	try: 
		product = cmod.Product.objects.get(id=request.urlparams[0])		
	except cmod.Product.DoesNotExist:
		return Http404()



	print('>>>>>>>>>>>>>>>>>>>>here in cart.add function')

	form = AddForm(request, initial = {'quantity':1}, extra={'product':product})
	if request.method == 'POST': #la forma e' stata appena sottomesso
		print('>>>>>>>>>>>>>>>>>>>>>>>>form has been submitted')

		form = AddForm(request, request.POST, extra={'product':product})
		if form.is_valid():
			print('>>>>>>>>>>>>>>>>>>>>>>>>form is valid ')
			# ricordare nello cart
			try:
				request.shopping_cart.add_item(product, form.cleaned_data['quantity'])
				print('>>>>>>>>>>>>>>>>>>>>>>>>called add_item function from shopping cart ')
			except ValueError as e:
				# the error message is defined in the form. this would usually not be done up here, but in the form. 
				form.add_error('quantity', str(e))
		else:
			print('>>>>>>>>>>>>>>>>>>>>>>>>form is not valid')		
	else:
		print('>>>>>>>>>>>>>>>>>>>>>>>>form was not submitted')

	template_vars = {
	'form': form,
	'product':product,

	}

	

	return dmp_render(request, 'cart.add.html', template_vars)


class AddForm(CustomForm):
	quantity = forms.IntegerField(label = 'Quantity', required = False, min_value=1, max_value=100)


	# def __init__(self, *args, **kwargs):
	# 	self.request = kwargs.pop('request')
	# 	super(AddForm, self).__init__(*args, **kwargs)

	def clean_quantity(self):
		'''ensure we have enough of this product'''
		try:
			self.request.shopping_cart.check_availability(self.extra['product'], self.cleaned_data.get('quantity')) #i actually do this in my add_item method, so i dont think i need to do it here
		except ValueError as e:
			raise forms.ValidationError(str(e))
		return self.cleaned_data['quantity']



