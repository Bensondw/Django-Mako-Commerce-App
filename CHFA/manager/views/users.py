from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from account import models as amod
from CHF.customform import CustomForm
from django.contrib.auth.models import Group, Permission
import datetime


@view_function
@permission_required('account.change_user', login_url='/')
def process_request(request):
  '''Lists the users in a table on the screen'''
  users = amod.User.objects.all().order_by('last_name', 'first_name')
    
  template_vars = {
    'users': users
  }
  return dmp_render(request, 'users.html', template_vars)
  
  

######################################################
###   Editing a user

@view_function
@permission_required('account.change_user', login_url='/')
def edit(request):
  '''Edits a user'''
  try:
    user = amod.User.objects.get(id=request.urlparams[0])
  except amod.User.DoesNotExist:
    return HttpResponseRedirect('/manager/users/')
    
  # process the form (note the parameters are different because this form uses CustomForm)
  form = EditForm(request, initial=model_to_dict(user), extra={ 'user': user })
  if request.method == 'POST':  # just submitted the form
    form = EditForm(request, request.POST, extra={ 'user': user })
    form.user = user
    # this next line removed because the CustomForm has the "extra" parameter
    #form.user = user  # so we can check username later
    if form.is_valid():
      user.username = form.cleaned_data.get('username')
      user.first_name = form.cleaned_data.get('first_name')
      user.last_name = form.cleaned_data.get('last_name')
      user.email = form.cleaned_data.get('email')
      user.address = form.cleaned_data.get('address')
      user.city = form.cleaned_data.get('city')
      user.state = form.cleaned_data.get('state')
      user.zip_code = form.cleaned_data.get('zip_code')
      user.birth_date = form.cleaned_data.get('birth_date')
      user.phone_number = form.cleaned_data.get('phone_number')
      user.save()
      user.groups.clear()
      for g in form.cleaned_data.get('groups'):
        user.groups.add(g)
      user.user_permissions.clear()
      for p in form.cleaned_data.get('user_permissions'):
        user.user_permissions.add(p)
      return HttpResponseRedirect('/manager/users/')

  template_vars = {
    'form': form,
    'user': user,
  }
  return dmp_render(request, 'users.edit.html', template_vars)


# note this class is using the CustomForm
class EditForm(CustomForm):
  username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  first_name = forms.CharField(label='First Name', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  last_name = forms.CharField(label='Last Name', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  email = forms.CharField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  address = forms.CharField(label='Address 1', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  birth_date = forms.DateField(label='Birth Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  phone_number = forms.CharField(label='Phone Number', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  groups = forms.ModelMultipleChoiceField(label="Groups", required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))
  user_permissions = forms.ModelMultipleChoiceField(label="Special Permissions", required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))

  def clean_username(self):
    '''Ensures a unique username'''
    # we need to exclude our own record because otherwise it would match
    if amod.User.objects.filter(username=self.cleaned_data.get('username')).exclude(id=self.extra['user'].id).count() > 0:
      raise forms.ValidationError('This username is already taken.')
    return self.cleaned_data.get('username')
    


  

######################################################
###   Creating a user

@view_function
@permission_required('account.add_user', login_url='/')
def create(request):
  '''Creates a user'''
  # process the form (note the parameters are different because this form uses CustomForm)
  form = CreateForm(request)
  if request.method == 'POST':  # just submitted the form
    form = CreateForm(request, request.POST)
    if form.is_valid():
      user = amod.User()
      user.username = form.cleaned_data.get('username')
      user.set_password(form.cleaned_data.get('password'))
      user.first_name = form.cleaned_data.get('first_name')
      user.last_name = form.cleaned_data.get('last_name')
      user.email = form.cleaned_data.get('email')
      user.address = form.cleaned_data.get('address')
      user.city = form.cleaned_data.get('city')
      user.state = form.cleaned_data.get('state')
      user.zip_code = form.cleaned_data.get('zip_code')
      user.birth_date = form.cleaned_data.get('birth_date')
      user.phone_number = form.cleaned_data.get('phone_number')
      user.save()
      user.groups.clear()
      for g in form.cleaned_data.get('groups'):
        user.groups.add(g)
      user.user_permissions.clear()
      for p in form.cleaned_data.get('user_permissions'):
        user.user_permissions.add(p)
      return HttpResponseRedirect('/manager/users/')

  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'users.create.html', template_vars)


class CreateForm(CustomForm):
  username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  first_name = forms.CharField(label='First Name', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  last_name = forms.CharField(label='Last Name', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  email = forms.CharField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  address = forms.CharField(label='Address 1', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  birth_date = forms.DateField(label='Birth Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  phone_number = forms.CharField(label='Phone Number', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  groups = forms.ModelMultipleChoiceField(label="Groups", required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))
  user_permissions = forms.ModelMultipleChoiceField(label="Special Permissions", required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={ 'class': 'form-control' }))


  def clean_username(self):
    '''Ensures a unique username'''
    if amod.User.objects.filter(username=self.cleaned_data.get('username')).count() > 0:
      raise forms.ValidationError('This username is already taken.')
    return self.cleaned_data.get('username')
    
    
    

######################################
###   Delete user

@view_function
@permission_required('account.delete_user', login_url='/')
def delete(request):
  '''Deletes a user'''
  try:
    user = amod.User.objects.get(id=request.urlparams[0])
  except amod.User.DoesNotExist:
    return HttpResponseRedirect('/manager/users/')
    
  # delete the user
  user.delete()
  
  # redirect
  return HttpResponseRedirect('/manager/users/')




########################################
###   Change user password


@view_function
@permission_required('account.change_user', login_url='/')
def password(request):
  # get the user
  try:
    user = amod.User.objects.get(id=request.urlparams[0])
  except amod.User.DoesNotExist:
    return HttpResponseRedirect('/manager/users/')
    
  # process the form
  form = PasswordForm(request)
  if request.method == 'POST':  # just submitted the form
    form = PasswordForm(request, request.POST)
    if form.is_valid():
      user.set_password(form.cleaned_data.get('password1'))
      user.save()
      return HttpResponse('''
        <script>
          document.location.href = '/manager/users.edit/%s/';
        </script>
      ''' % user.id)
  
  template_vars = {
    'form': form,
    'user': user,  # so we can put user.id on form action
  }
  return dmp_render(request, 'users.password.html', template_vars)
  
  
class PasswordForm(CustomForm):
  is_ajax = True
  form_id = 'password_form'
  
  password1 = forms.CharField(label='New password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  password2 = forms.CharField(label='Repeat password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  

  def clean(self):
    # check the two password are the same
    if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
      raise forms.ValidationError('Please ensure the two passwords match.')
    return self.cleaned_data
    