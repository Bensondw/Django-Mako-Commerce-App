
from django import forms
from django.http import HttpRequest
from catalog import models as cmod
import datetime, decimal
import operator


########################################################################
###   Shopping Cart middleware that adds a shopping cart to the
###   current request.
###
###   Installation:
###      1. Since this code uses decimal.Decimal() objects, it cannot use the regular JSON serializer
###         that sessions default to.  Switch to pickle-based sessions by adding this to settings.py:
###
###         SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
###
###      2. Enable this middleware by adding the following to settings.py:
###         (assuming you have this file in the /CHF/ directory, of course)
###
###         MIDDLEWARE_CLASSES = [
###             ...
###             'CHF.shopping_cart.ShoppingCartMiddleware',
###             ...
###         ]
###
###         The above line must come after SessionAuthenticationMiddleware in the list because it uses sessions.
###

# the key we use for the shopping cart list  
SHOPPING_CART_KEY = 'shopping_cart'

### STUDENTS ###
# the key we use for the last viewed items
LAST_VIEWED_KEY = 'shopping_cart_last_viewed'

LAST_VIEWED_COUNT = 5 #keep only the last five

TAX_RATE = decimal.Decimal(0.0725) #just using a default rate

SHIPPING_AMOUNT = decimal.Decimal(10)


class ShoppingCartMiddleware:
	'''Adds shopping cart methods to the request'''

	def process_request(self, request):
		'''Called when the request starts in Django'''
		#attach a ShoppingCart instance to the request object
		request.shopping_cart = ShoppingCart(request.session) #init function


	def process_response(self, request, response):
		'''Called when the response goes back to the browser.'''
		#save the shopping cart
		request.shopping_cart.save(request.session) #save function

		# return the repsponse object per Django docs
		return response


class ShoppingCart(object):
	'''The user's shopping cart. One of these is created for each request. 
		Note that he hasn't added any efficiency code yet, such as lazy loading/saving 
		the shopping cart object (only if/when it gets accessed) or using a set for faster 
		item lookup. '''

	def __init__(self, session):
		'''constructor. called from process_request() above.'''
		self.session = session 

		# load the cart from the session
		self.cart = session.get(SHOPPING_CART_KEY, [])	 #we load up self.cart with the list found in the session that has the key SHOPPING_CART_KEY. If the key refers to nothing, it is defaulted to an empty list

		# load the last 5 items
		self.last5ids = session.get(LAST_VIEWED_KEY, []) #we load up self.last5ids with the list found in the session that has the key LAST_VIEWED_KEY. If the key refers to nothing, it is defaulted to an empty list




	def save(self, session):
		'''Saves the current shopping cart to the session.
		This is called from the middleware above'''

		# sort the cart by name
		self.cart.sort(key=operator.attrgetter('name'))

		# set the cart in the session (this saves it to the disk so we can access it again)
		session[SHOPPING_CART_KEY] = self.cart

		# set the shopping_last_viewed in the session
		session[LAST_VIEWED_KEY] = self.last5ids



	### Shopping Cart

	def get_items(self):
		'''Returns the items to the shopping cart'''
		return self.cart

	def get_real_items(self):
		real = []
		# pull in the cart list
		for word in self.cart:
			real.append(cmod.Product.objects.get(id = word.product_id)) # use list items to query database and get the real instances of them
		return real

	def check_availability(self, product, desired_quantity=1):
		'''checks that the product is available at the given quantity, returns a value'''		
		# get the available per the database for individual or bulk		
		
		if isinstance(product, cmod.BulkProduct):
			available = product.quantity
		else:
			available = 1

		for thing in self.cart:
			if product.id == thing.product_id:
				available -= thing.quantity
				break


		if isinstance(product, cmod.IndividualProduct):
			desired_quantity = 1
			if desired_quantity > available: 
				raise ValueError
		else:
			if desired_quantity > available: 
				raise ValueError 


	def add_item(self, product, quantity = 1):
		'''adds the products to the current cart. if the item already exists in the cart, increment the quantity accordingly'''
		print('>>>>>>>>>>>>>>>>>>>> in shopping_cart at  add item')
		
		# check the availability
		self.check_availability(product)		

		# ensure it is in our cart - see if it is in the cart
		for item in self.cart:
			if product.id == item.product_id:
				item.quantity += quantity
				break
		else:
			newOne = ShoppingItem(product)
			if isinstance(product, cmod.IndividualProduct):
				quantity = 1
			newOne.quantity = quantity
			self.cart.append(newOne)		
		print(self.cart)
		

	def remove_item(self, product):
		'''removes the given item id from the cart 
			the product can be a real product instance or an id'''

			# not currently working

			# i use the function below to manually clear out the cart for testing purposes
		# self.cart = []

		for p in self.cart:
			if p.product_id == product.id:
				self.cart.remove(p)

		

	def clear_items(self):
		'''clears all items from the shopping cart'''
		
		self.cart = []

		# return the cart? - nope this is a void method. it just does something. we dont care about getting anything back.


	def get_item_count(self):
		'''returns the item count of all items in the cart, 
		   not unique instances, but total number of items'''

		item_count = decimal.Decimal(0)

		for item in self.cart:
			item_count += item.quantity

		return item_count


			# the other way for the above method:
			 # return len(self.cart) - will return the number of unique instances in the cart




	###Financial Methods

	def calc_subtotal(self):
		'''returns the subtotal (sum of product) cost'''
		subtotal = decmial.Decimal(0)

		for item in cart:
			subtotal += item.calc_extended()
		
		return subtotal.quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_UP)

	def calc_tax(self):
		'''returns the tax on the current cart'''
		# so use the tax rate defined at the top and apply it to the subtotal you just calculated		
		tax = subtotal * TAX_RATE
		return tax.quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_UP)

	def calc_shipping(self):
		'''returns the shipping cost on the items in the cart'''
		return SHIPPING_AMOUNT


	def calc_total(self):
		'''returns the total cost for items in the cart'''
		return self.calc_subtotal() + self.calc.tax() + self.calc_shipping()


	# LAST VIEWED PRODUCT METHODS

	def item_viewed(self, product): #add an item to the list
		'''adds the item to the last-viewed items'''
		
		# Get list out of session (self.last_5_ids), and store in local list.
		# Remove product.id (which comes in as a parameter) from list if its already there
		# Insert product.id at index 0
		# Prune list to 5
		# Save local list onto self.last_5_ids
		# local_last5 = self.last5ids



		# self.last5ids = local_last5



		# delete from the list if currently there (so it isnt listed twice)
		try:
			self.last5ids.remove(product.id)
		except ValueError:
			pass
		
		# add the last viewed list
		self.last5ids.insert(0, product.id)

		# ensure the list isnt too long - 5 items 
		self.last5ids = self.last5ids[0:5]

		return self.last5ids

	def get_viewed_items(self): #display the list
		'''returns a django query object of the last items viewed'''
		
		
		# Translate self.last_5_ids into a list of full products and return that list.
		HAROLD = self.last5ids
		print(self.last5ids)
		products = [cmod.Product.objects.get(id=p) for p in HAROLD]
		
		return products


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







class ShoppingItem(object):
	'''A shopping cart item. Each of these objects represents a product in the shopping cart.  In
	other words, the shopping cart is a list of these objects (ShoppingItem objects).

	This class cannot contain any pointers because it is serialized to the user's session object.
	That's why it references product.id instead of product directly.
	'''
	def __init__(self, product):
		'''Constructor.  Starts the quantity at 0, so be sure to set it.'''
		self.product_id = product.id
		self.filename = product.get_image_filename()
		self.name = product.name
		self.price = product.price
		self.quantity = decimal.Decimal(0)


	def calc_extended(self):
		return self.price * self.quantity