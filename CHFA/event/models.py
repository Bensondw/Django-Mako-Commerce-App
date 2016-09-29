from django.db import models
from django.contrib import admin



class Venue(models.Model):
  '''A venue where an event is hosted.'''
  name = models.TextField(null=True, blank=True)
  address = models.TextField(null=True, blank=True)
  city = models.TextField(null=True, blank=True)
  state = models.TextField(null=True, blank=True)
  zip_code = models.TextField(null=True, blank=True)
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return self.name
    


class Event(models.Model):
  '''A CHF event'''
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  venue = models.ForeignKey(Venue, null=True, blank=True, related_name="events")
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return '%s (%s to %s)' % (self.name, self.start_date.strftime('%Y-%m-%d'), self.end_date.strftime('%Y-%m-%d'))



class Area(models.Model):
  '''An area within an event.  Areas are specific to individual events.'''
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  place_number = models.IntegerField(null=True, blank=True)
  event = models.ForeignKey(Event, related_name="areas")
  
  def __str__(self):
    '''Prints for debugging purposes'''
    return '%s (%s)' % (self.name, self.place_number)
    
