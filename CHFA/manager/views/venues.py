from django.conf import settings
from django import forms
from django.contrib.auth.decorators import permission_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from account import models as amod
from catalog import models as cmod
from event import models as emod
import datetime


@view_function
@permission_required('event.change_venue', login_url='/')
def process_request(request):
  '''Lists the venues in a table on the screen'''
  venues = emod.Venue.objects.all().order_by('name')
    
  template_vars = {
    'venues': venues
  }
  return dmp_render(request, 'venues.html', template_vars)
  
  

  

######################################################
###   Creating a venue

@view_function
@permission_required('event.change_venue', login_url='/')
def create(request):
  '''Creates a venue'''
  # process the form
  form = CreateForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateForm(request.POST)
    if form.is_valid():
      venue = emod.Venue()
      venue.name = form.cleaned_data.get('name')
      venue.address = form.cleaned_data.get('address')
      venue.city = form.cleaned_data.get('city')
      venue.state = form.cleaned_data.get('state')
      venue.zip_code = form.cleaned_data.get('zip_code')
      venue.save()
      return HttpResponseRedirect('/manager/venues/')

  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'venues.create.html', template_vars)


class CreateForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  zip_code = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  



######################################################
###   Editing a venue

@view_function
@permission_required('event.change_venue', login_url='/')
def edit(request):
  '''Edits a venue'''
  try:
    venue = emod.Venue.objects.get(id=request.urlparams[0])
  except emod.Venue.DoesNotExist:
    return HttpResponseRedirect('/manager/venues/')
    
  # process the form
  form = EditForm(initial=model_to_dict(venue))
  if request.method == 'POST':  # just submitted the form
    form = EditForm(request.POST)
    if form.is_valid():
      venue.name = form.cleaned_data.get('name')
      venue.address = form.cleaned_data.get('address')
      venue.city = form.cleaned_data.get('city')
      venue.state = form.cleaned_data.get('state')
      venue.zip_code = form.cleaned_data.get('zip_code')
      venue.save()
      return HttpResponseRedirect('/manager/venues/')

  template_vars = {
    'form': form,
  }
  return dmp_render(request, 'venues.edit.html', template_vars)


class EditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  zip_code = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  




######################################
###   Delete venue

@view_function
@permission_required('event.delete_venue', login_url='/')
def delete(request):
  '''Deletes a venue'''
  try:
    venue = emod.Venue.objects.get(id=request.urlparams[0])
  except emod.Venue.DoesNotExist:
    return HttpResponseRedirect('/manager/venues/')
    
  # delete the venue
  venue.delete()
  
  # redirect
  return HttpResponseRedirect('/manager/venues/')

