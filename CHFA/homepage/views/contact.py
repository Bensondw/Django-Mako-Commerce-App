from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render

@view_function
def process_request(request):
  
  clientname = request.POST.get('yourname')
  
  template_vars = {
  }
  
  return dmp_render(request, 'contact.html', template_vars)