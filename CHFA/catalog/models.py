from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel
import inspect

#############################################################
###   Types of Products in the system

class Category(models.Model):
  '''A category that holds multiple products'''
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return self.name

admin.site.register(Category)


class Sale(models.Model):
  order_date = models.DateTimeField(null = True, blank = True)
  ship_date = models.DateTimeField(null = True, blank = True)
  tracking_number = models.IntegerField(default=0)
  total_price = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2) # max number is 99,999.99
  ship_name = models.TextField(null=True, blank=True)
  ship_address = models.TextField(null=True, blank=True)
  ship_city = models.TextField(null=True, blank=True)
  ship_state = models.TextField(null=True, blank=True)
  ship_zip_code = models.TextField(null=True, blank=True)

admin.site.register(Sale)

class SaleItem(models.Model):
  description = models.TextField(null=True, blank=True)  
  price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2) # max number is 99,999.99
  quantity = models.IntegerField(default=0)
  extended= models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2) 

admin.site.register(SaleItem)

class Payment(models.Model):
  payment_date = models.DateTimeField(null = True, blank = True)
  amount = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2) 
  variation_code = models.IntegerField(default=0)

admin.site.register(Payment)

class Product(PolymorphicModel):
  '''The superclass of all products in our database'''
  title = 'Product'  # this field isn't a DB field, just used to display this product  
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  category = models.ForeignKey(Category, null=True, blank=True)
  price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2) # max number is 99,999.99
  # image was taken out per S4 requirements
  # image = models.TextField(null=True, blank=True)
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Product (abstract): %s (%s)' % (self.name, self.add_date)
  

  def get_image_filename(self):
    '''Returns the filename of the first image, or the unavailable image if no images have been added.'''
    first_image = self.images.first()
    return first_image.filename if first_image != None else 'image_unavailable.gif'


admin.site.register(Product)



class ProductImage(models.Model):
  '''An image for a product'''
  product = models.ForeignKey(Product, related_name='images')
  filename = models.TextField(null=True, blank=True)
  
admin.site.register(ProductImage)





RENTAL_STATUS_CHOICES = (
  ( 'current', 'Rentable'),
  ( 'damaged', 'Damaged'),
  ( 'retired', 'No Long Rentable'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

class RentalProduct(Product):
  '''A product that is rentable'''
  title = 'Rental Product'  # this field isn't a DB field, just used to display this product
  
  purchase_date = models.DateTimeField(null=True, blank=True)
  status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)

  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Rental Product: %s (%s): %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)



INDIVIDUAL_STATUS_CHOICES = (
  ( 'current', 'For Sale'),
  ( 'sold', 'Sold'),
  ( 'retired', 'No Long For Sale'),
)
INDIVIDUAL_STATUS_CHOICES_MAP = dict(INDIVIDUAL_STATUS_CHOICES)

class IndividualProduct(Product):
  '''A product we track individually'''
  title = 'Individual Product'  # this field isn't a DB field, just used to display this product

  creator = models.ForeignKey('account.User')
  status = models.TextField(null=True, blank=True, choices=INDIVIDUAL_STATUS_CHOICES)
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Individual Product: %s (%s): %s' % (self.name, self.add_date, self.creator.get_full_name())

admin.site.register(IndividualProduct)
  
  
class BulkProduct(Product):
  '''A product we track by quantity'''
  title = 'Bulk Product'  # this field isn't a DB field, just used to display this product

  quantity = models.IntegerField(default=0)
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Bulk Product: %s (%s): %s' % (self.name, self.add_date, self.quantity)

admin.site.register(BulkProduct)
  
  

##############################################################################
###  The types of products, keyed by their class names.
###  This must always be at the END of the class so the dynamic        
###  populating works right.

PRODUCT_SUBCLASSES = []
PRODUCT_SUBCLASSES_DICT = {}

# populate the dictionary dynamically (globals() returns all the module-level variables)
#
# As of this code time, PRODUCT_SUBCLASSES is:
# [
#   ['RentalProduct',     <class 'catalog.models.RentalProduct'>     ],
#   ['IndividualProduct', <class 'catalog.models.IndividualProduct'> ],
#   ['BulkProduct',       <class 'catalog.models.BulkProduct'>       ],
# ]
# and PRODUCT_SUBCLASSES_DICT is:
# {
#   'IndividualProduct': <class 'catalog.models.IndividualProduct'>,
#   'RentalProduct': <class 'catalog.models.RentalProduct'>,
#   'BulkProduct': <class 'catalog.models.BulkProduct'>}
# }
#
for varname in list(globals()):
  obj = globals()[varname]
  if inspect.isclass(obj):
    class_inheritance_list = inspect.getmro(obj)
    if len(class_inheritance_list) >= 2 and class_inheritance_list[1] == Product:
      PRODUCT_SUBCLASSES.append([ obj.__name__, obj ])
      PRODUCT_SUBCLASSES_DICT[obj.__name__] = obj


###################################################
###   Factory method to create products

def create_product(ptype):
  '''Creates a product of the given type - this is a simple implementation of the FACTORY pattern.'''
  # method 1 (using if statements)
  # if ptype == 'RentalProduct':
  #   return RentalProduct()
  # elif ptype == 'IndividualProduct':
  #   return IndividualProduct()
  # elif ptype == 'BulkProduct':
  #   return BulkProduct()
  # raise TypeError('Invalid product type: %s' % ptype)
  # method 2 (using a dictionary -- this way is better)
  if ptype in PRODUCT_SUBCLASSES_DICT:
    return PRODUCT_SUBCLASSES_DICT[ptype]()
  raise TypeError('Invalid product type: %s' % ptype)
  


