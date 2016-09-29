from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account import models as amod
from catalog import models as cmod
import operator




# def initialize_template_vars(request):
#   '''Initializes the template vars with the categories and last 5 items viewed'''
#   template_vars = {}
  
#   # add the catgories
#   template_vars['categories'] = cmod.Category.objects.order_by('name')
  
#   # return
#   return template_vars


# def add_new(request, template_vars):

# 	LAST_FIVE_KEY = 'lastFive'

# 	#  when they first visit the page during a session, there wont be anything there, so we need to just put a blank dictionary there
# 	if LAST_FIVE_KEY not in request.session:
# 		request.session[LAST_FIVE_KEY] = []

# 	# just put it in a variable to write less
# 	last5 = request.session[LAST_FIVE_KEY]

# 	if template_vars['product'].id not in last5[0:5]:
# 		last5.insert(0,template_vars['product'].id)




# 	request.session[LAST_FIVE_KEY] = last5


  
# def list_viewed(request, template_vars):

# 	LAST_FIVE_KEY = 'lastFive'

# 	if LAST_FIVE_KEY not in request.session:
# 		request.session[LAST_FIVE_KEY] = []

# 	lastfive = request.session[LAST_FIVE_KEY][0:5]

# 	products = []

# 	for item in lastfive:
# 		products.append(cmod.Product.objects.get(id=item))

# 	template_vars['list_of_them'] = products

# 	print (template_vars['list_of_them'])
# 	print ('hello')

# def test(request, template_vars):
# 	print("fun things")