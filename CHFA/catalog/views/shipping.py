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


	# cart = request.shopping_cart.get_items()

	
	
	template_vars = {
		# 'product': product,
		'categories': categories,
		# 'cart': cart,
	}

	
	return dmp_render(request, 'shipping.html', template_vars)





