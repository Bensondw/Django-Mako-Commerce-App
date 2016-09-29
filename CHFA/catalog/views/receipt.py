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
from account import models as amod
from CHF.customform import CustomForm
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail

@view_function
def process_request(request):

	sale = amod.Sale.objects.get(id=request.urlparams[0])


	template_vars = {
		'sale':sale,
	}

	message = dmp_render_to_string(request, 'receipt.html', template_vars)
	send_mail('Receipt of Sale CHF', message, 'bensonweeks@byu.edu', ['bensonweeks@gmail.com'], fail_silently=False)

	return dmp_render(request, 'receipt.html', template_vars)