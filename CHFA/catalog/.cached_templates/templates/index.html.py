# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459531089.0246348
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


from catalog import models as cmod 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<form action="/homepage/contact/" method="POST"> <!-- action directs to where the logic will happen -->\r\n\r\n<!-- method Post (rather than Get) hides the data as it is sent from the user, doesn\'t put it into the url -->\r\n    <table> <!--lines up the form fields to look decent -->\r\n      <tr>\r\n        <td>Your name:</td> <!--Whatever you type here would just go in front of the form input field -->\r\n        <td><input type="text" name="yourname" /></td><!-- input types (just google these i guess) - they will mostly be type "text" for the form we are making --> \r\n      </tr><tr>\r\n        <td>Your email:</td>\r\n        <td><input type="text" name="youremail" /></td>  <!-- name of the input area -->\r\n      </tr><tr>\r\n        <td>Message:</td>\r\n        <td><textarea name="yourmessage"></textarea></td>\r\n      </tr><tr colspan="2">\r\n        <td><input type="submit" value="Send Message"></td>\r\n      </tr>\r\n    </table>\r\n  </form>\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' \r\n\r\n\r\n')
        for product in products:
            __M_writer('\t\t<div class="item"> \r\n\t\t\t<a href="/catalog/detail/')
            __M_writer(str(product.id))
            __M_writer('"> <!--THis will go to details.html-->\r\n\t\t\t\t <img class="img-thumbnail" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/product_images/')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('" /> \t \r\n\t\t\t</a>\r\n\t\t\t<p>\r\n\t\t\t\t')
            __M_writer(str(product.name))
            __M_writer('\r\n\t\t\t\t</br>\r\n\t\t\t\t$')
            __M_writer(str(product.price))
            __M_writer('\r\n\t\t\t</p>\r\n\t\t\t\r\n\t\t</div> <!-- flex container div  -->\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "line_map": {"64": 43, "65": 43, "66": 43, "67": 43, "68": 46, "69": 46, "70": 48, "39": 1, "40": 3, "71": 48, "45": 54, "78": 72, "17": 1, "51": 37, "30": 0, "72": 53, "59": 37, "60": 40, "61": 41, "62": 42, "63": 42}, "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/index.html"}
__M_END_METADATA
"""
