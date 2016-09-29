# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459894117.0745356
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/detail.html'
_template_uri = 'detail.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer(' \r\n\r\n\t<div>\t\t\t\r\n\t\t<img class="img-thumbnail lefty" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/product_images/')
        __M_writer(str( product.get_image_filename() ))
        __M_writer('" /> \t \r\n\t\t\t<a href="/catalog/detail.carousel/')
        __M_writer(str(product.id))
        __M_writer('/" class="btn btn-warning under" id="view_more_images">View all Images</a>\r\n\r\n\t\t<div class="texty">\t\r\n\t\t\t<p>\r\n\t\t\t\t')
        __M_writer(str(product.name))
        __M_writer('\r\n\t\t\t\t</br>\r\n\t\t\t\t$')
        __M_writer(str(product.price))
        __M_writer('\r\n\t\t\t</p>\r\n\r\n\t\t\t<h5>')
        __M_writer(str(product.description))
        __M_writer('</h5>\r\n\r\n\t\t\t<p> ')
        __M_writer(str(product.category))
        __M_writer(' <br> ')
        __M_writer(str(product.title))
        __M_writer(' </p>\r\n\r\n')
        if isinstance(product, cmod.BulkProduct):
            __M_writer('\t\t\t\t<p class="pull-right">Left in Stock: ')
            __M_writer(str( product.quantity ))
            __M_writer(' </p>\r\n')
        __M_writer('\r\n\r\n\t\t\t\r\n\r\n\t\t\t\r\n\r\n\r\n\r\n\r\n\r\n\t\t</div>\t<!--text on the right  -->\r\n\r\n\r\n\t\t\r\n\t</div> <!--everything  -->\r\n\r\n\t<div id="buyform" class="pull-right">\r\n\t\t\t\t\r\n\t</div>\r\n\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/detail.html", "source_encoding": "utf-8", "uri": "detail.html", "line_map": {"64": 9, "65": 9, "66": 10, "67": 10, "68": 14, "69": 14, "70": 16, "71": 16, "72": 19, "73": 19, "74": 21, "75": 21, "76": 21, "77": 21, "78": 23, "79": 24, "80": 24, "17": 1, "82": 26, "88": 82, "30": 0, "81": 24, "40": 1, "41": 3, "46": 47, "52": 6, "61": 6, "62": 9, "63": 9}}
__M_END_METADATA
"""
