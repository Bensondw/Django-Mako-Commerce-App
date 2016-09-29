from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django import forms
from .. import dmp_render_to_string, dmp_render
from account.models import User

@view_function
def process_request(request):
  # ensure the user is logged in
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/account/login/')
  
  # process the form
  form = ChangeForm(initial={
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
  })
  if request.method == 'POST':  # just submitted the form
    form = ChangeForm(request.POST)
    if form.is_valid():
      u = request.user
      u.set_password(form.cleaned_data.get('password1'))
      u.save()

      # django automatically logs the user out
      authenticate(username=u.username, password=form.cleaned_data.get('password1'))
      login(...)
      
      return HttpResponseRedirect('/homepage/index/')
  
  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'change.html', template_vars)
  
  
class ChangeForm(forms.Form):
  current_password = forms.CharField(label='Current password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  password1 = forms.CharField(label='New passowrd', required=True, max_length=100)  
  password2 = forms.CharField(label='Repeat password', required=True, max_length=100)  

   # clean here
  def clean_current_password(self):
    if not self.request.user.check_password(self.cleaned_data.get('current_password')):
      raise forms.ValidationError('Try your current password again.')
    
    return self.cleaned_data.get('current_password')
    
  def clean(self):
    # check the two password are the same
    return self.cleaned_data
    
    