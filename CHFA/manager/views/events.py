from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from account import models as amod
from catalog import models as cmod
from event import models as emod
import datetime


@view_function
@permission_required('event.change_event', login_url='/')
def process_request(request):
  '''Lists the events in a table on the screen'''
  events = emod.Event.objects.all().order_by('name')
    
  template_vars = {
    'events': events
  }
  
  return dmp_render(request, 'events.html', template_vars)
  
  

  
######################################################
###   Creating and Editing a event

@view_function
@permission_required('event.change_event', login_url='/')
@permission_required('event.add_event', login_url='/')
def edit(request):
  '''Creates or Edits a event'''
  # get or create the Event object
  creating = False
  if request.urlparams[0]:  # edit
    try:
      event = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
      return HttpResponseRedirect('/manager/events/')
  else:  # create
    creating = True
    event = emod.Event()
    
  # process the form
  form = EditForm(initial=model_to_dict(event))
  if request.method == 'POST':  # just submitted the form
    form = EditForm(request.POST)
    if form.is_valid():
      event.name = form.cleaned_data.get('name')
      event.description = form.cleaned_data.get('description')
      event.start_date = form.cleaned_data.get('start_date')
      event.end_date = form.cleaned_data.get('end_date')
      event.venue = form.cleaned_data.get('venue')
      event.save()
      if creating:
        return HttpResponseRedirect('/manager/events.edit/%s/' % event.id)  # show the edit for so the user can add areas
      else:
        return HttpResponseRedirect('/manager/events/')  # go back to events
      
  # render the form
  template_vars = {
    'form': form,
    'event': event,
    'creating': creating,
  }
  return dmp_render(request, 'events.edit.html', template_vars)


class EditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  start_date = forms.DateField(label='Start Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  end_date = forms.DateField(label='End Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  venue = forms.ModelChoiceField(label='Venue', queryset=emod.Venue.objects.order_by('name'), required=True, widget=forms.Select(attrs={ 'class': 'form-control' }))  




######################################
###   Delete event

@view_function
@permission_required('event.delete_event', login_url='/')
def delete(request):
  '''Deletes a event'''
  try:
    event = emod.Event.objects.get(id=request.urlparams[0])
  except emod.Event.DoesNotExist:
    return HttpResponseRedirect('/manager/events/')
    
  # delete the event
  event.delete()
  
  # redirect
  return HttpResponseRedirect('/manager/events/')





######################################
###   Edits an area


  
######################################################
###   Creating and Editing an area

@view_function
@permission_required('event.change_area', login_url='/')
@permission_required('event.add_area', login_url='/')
def edit_area(request):
  '''Creates or Edits an aera'''
  # get the event object
  try:
    event = emod.Event.objects.get(id=request.urlparams[0])
  except emod.Event.DoesNotExist:
    return HttpResponse('''
      <script>
        document.location.href = '/manager/events/';
      </script>
    ''')

  # get or create the object
  if request.urlparams[1] != 'None':  # edit
    try:
      area = emod.Area.objects.get(id=request.urlparams[1])
    except emod.Event.DoesNotExist:
      return HttpResponse('''
        <script>
          document.location.href = '/manager/events/';
        </script>
      ''')
  else:  # create
    area = emod.Area()
    
  # process the form
  form = AreaEditForm(initial=model_to_dict(area))
  if request.method == 'POST':  # just submitted the form
    form = AreaEditForm(request.POST)
    if form.is_valid():
      area.name = form.cleaned_data.get('description')
      area.description = form.cleaned_data.get('description')
      area.place_number = form.cleaned_data.get('place_number')
      area.event = event
      area.save()
      return HttpResponse('''
        <script>
          document.location.href = '/manager/events.edit/%s/';
        </script>
      ''' % event.id)
      
  # render the form
  template_vars = {
    'form': form,
    'event': event,
    'area': area,
  }
  return dmp_render(request, 'events.edit_area.html', template_vars)


class AreaEditForm(forms.Form):
  name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  place_number = forms.IntegerField(label='Place Number', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  



######################################
###   Delete area

@view_function
@permission_required('event.delete_area', login_url='/')
def delete_area(request):
  '''Deletes an area'''
  try:
    area = emod.Area.objects.get(id=request.urlparams[1])
  except emod.Area.DoesNotExist:
    return HttpResponseRedirect('/manager/events.edit/%s/' % request.urlparams[0])
    
  # delete the event
  area.delete()
  
  # redirect
  return HttpResponseRedirect('/manager/events.edit/%s/' % request.urlparams[0])

