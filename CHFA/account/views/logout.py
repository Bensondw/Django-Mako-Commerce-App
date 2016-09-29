from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django import forms
from .. import dmp_render_to_string, dmp_render
from account.models import User

@view_function
def process_request(request):
  # log the user out
  logout(request)
  
  return HttpResponseRedirect('/homepage/index/')
  