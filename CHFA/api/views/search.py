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

# 1. Create a normal view (i.e. process_request method). Mine is at the url /api/search/.

# 2. Within the view, start by setting "qry = cmod.Product.objects"

# 3. Then do a series of "if" statements 
	# that check if certain parameters were sent in request.GET. 
	# For example, if a name was sent in request.GET, you can modify 
	# the initial query variable with "qry = qry.filter(...)". That 
	# will add a new filter to the qry variable. Do this for every 
	# parameter that was sent in. Note that I'm not using a Django 
	# form object -- I'm just accessing request.GET directly to get the parameters.

# 4. Once you've added all the filter statements to the qry variable, do a 
	# "for" loop through the query. For each product that is pulled, create a 
	# dictionary with its information. Add that dictionary to a list of results.

# 5. We now have a list of results (a list containing dictionaries). 
	# Send this back to the user with "return JsonResponse(resultslist)". 
	# Be sure to import JsonResponse. It's in the standard Django libraries. 
	# The JsonResponse will automatically take your list of dictionaries, 
	# turn it into json, and send back to the browser.

@view_function
def process_request(request):	

	categories = cmod.Category.objects.all()

	qry = cmod.Product.objects.all()


	# if blank in request.GET:
	# 	qry = qry.filter()
	# elif blank in request.GET:
	# 	qry = qry.filter()
	# elif blank in request.GET:
	# 	qry = qry.filter()
	
	
	template_vars = {
		# 'product': product,
		'qry': qry,
		'categories': categories,
	}

	
	return dmp_render(request, 'search.html', template_vars)

