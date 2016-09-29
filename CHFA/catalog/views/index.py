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
# from . import initialize_template_vars
# from . import initialize_template_vars, add_new, list_viewed, test






@view_function
def process_request(request):

	

	'''Lists the products in a table on the screen'''
	# pull all products
	products = cmod.Product.objects.not_instance_of(cmod.RentalProduct).order_by('name')
	categories = cmod.Category.objects.all()	


	if request.urlparams[0]:
		products = products.filter(category=request.urlparams[0])


	# order it case insensitively (thanks to stackoverflow for this)
	products = products.extra(select={'lower_name':'lower(name)'}).order_by('lower_name')

	


	template_vars = {
		'products': products,
		'categories': categories,
	}

	return dmp_render(request, 'index.html', template_vars)


