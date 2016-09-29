'''
A very simple form extension that does the following:

  1. Prints the full form tags, including <form></form>.
     (the normal Django form class only prints fields)
  
  2. Allows an "extra" dictionary to be sent, which allows
     the caller to pass variables to the form class.
  
  3. Automatically includes the $.formAjax() call if
     ajax=True.
     
  4. Adds the request as a form class variable.
'''

from django import forms
from django.http import HttpRequest


class CustomForm(forms.Form):
  # subclasses should override the form_id if they need a specific id
  form_id = 'custom_form'
  
  # subclasses should override the submit_buttons if they need specific text on buttons
  submit_buttons = [ 'Submit' ]
  
  # subclasses should set is_ajax=True to ajaxify the form
  is_ajax = False
  ajax_target = '#jquery-loadmodal-js-body' # this is the default loadmodal.js body id
  
  
  def __init__(self, request, *args, **kwargs):
    '''Creates the custom form.  Two optional parameters can be sent.  Examples:
    
       class MyForm(forms.Form):
         ...
      
       form = MyForm(request, extra={ 'user': request.user })
       if request.method == "POST":
         form = MyForm(request, request.POST, extra={ 'user': request.user })
         ...
      
       The user is now accessible in the form clean methods through self.extra['user'].
      
    '''      
    # set the request, extra, and ajax
    assert isinstance(request, HttpRequest), 'The first parameter to the CustomForm class must be the request object.'
    self.request = request
    self.extra = kwargs.pop('extra', None) # pop out of the kwargs dictionary or the superclass complains

    # call the superclass constructor
    super().__init__(*args, **kwargs)
    
  
  def as_table(self):
    '''Returns this form rendered with <tr> elements'''
    html = []
    
    # <form> tag
    html.append('<div class="custom_form_container" id="%s_container">' % self.form_id)
    html.append('<form class="custom_form" id="%s" action="%s" method="POST">' % (self.form_id, self.request.path))
    
    # form fields (the super knows how to do this)
    html.append('<table class="custom_form_table">')
    html.append(super().as_table())
    html.append('</table>')
    
    # submit buttons
    html.append('<div class="custom_form_buttons">')
    for sb in self.submit_buttons:
      html.append('<input name="submit_button" type="submit" class="btn btn-primary" value="%s" />' % sb)
    html.append('</div>')
    
    # add the javascript if ajax
    if self.is_ajax:
      html.append('''
        <script>
          $(function() {
            // ensure two forms with this id don't exist (this is a check for programmer error)
            if ($('[id="%(form_id)s"]').length > 1) {
              console.error('CustomForm found two forms with id=%(form_id)s.  The form will likely not be ajaxified correctly. No soup for you.');
            }
            // ajaxify the form
            $('#%(form_id)s').ajaxForm({ 
              target: '%(ajax_target)s', 
            }); 
          });//ready
        </script>
      ''' % {
        'form_id': self.form_id, 
        'ajax_target': self.ajax_target
      })
    
    # </form> tag
    html.append('</form>')
    html.append('</div>')
    
    # join the list and return
    return '\n'.join(html)
    