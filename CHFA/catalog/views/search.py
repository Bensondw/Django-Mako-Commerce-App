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




@view_function
def process_request(request):
	q = request.GET['q']

	# if someone comes here by accident:
	if not q:
		return httpResponseRedirect("/catalog/index/")

	qry = cmod.Product.objects.not_instance_of(cmod.RentalProduct) #this is to exclude all the rental products
	qry = qry.filter(name__icontains=q) #this searches for the product among bulk and individual
	qry = qry.order_by('name')

	# we need to use "qry" as criteria for which products will be displayed 
	products = qry
	categories = cmod.Category.objects.all()


	template_vars = {
	'products': products,
	'categories': categories,	
	}

	

	return dmp_render(request, 'index.html', template_vars)