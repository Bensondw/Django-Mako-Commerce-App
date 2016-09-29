# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460046579.7174287
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        cart = context.get('cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        cart = context.get('cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n\t<table class = "table table-striped">\r\n\t\t<tr>\r\n\t\t\t<th>Item</th>\t\t\r\n\t\t\t<!-- <th>Image</th> -->\t\t\r\n\t\t\t<th>Quantity</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>Extended Price</th>\r\n\t\t\t<th>Remove Item</th>\t\t\r\n\t\t</tr>\r\n\r\n\t\t\r\n')
        for item in cart:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<a href="/catalog/detail/')
            __M_writer(str(item.product_id))
            __M_writer('/">\t\t\t\t\t\r\n\t\t\t\t\t\t')
            __M_writer(str(item.name))
            __M_writer('\r\n\t\t\t\t\t</a>\r\n\t\t\t\t</td>\r\n\t\t\t\t<!-- \r\n\t\t\t\t<td>\t\r\n\t\t\t\t\t<a href="/catalog/detail/{item.id}/">\r\n\t\t\t\t\t\t<img class="img-thumbnail shopping" src="{ STATIC_URL }catalog/media/product_images/{ item.get_image_filename() }" /> \t \r\n\t\t\t\t\t</a>\r\n\t\t\t\t</td> -->\r\n\r\n\t\t\t\t<td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\r\n\t\t\t\t\r\n\r\n\t\t\t\t<td> $ ')
            __M_writer(str(item.price))
            __M_writer('</td>\r\n\t\t\t\t\r\n\t\t\t\t<td> $ ')
            __M_writer(str(item.calc_extended()))
            __M_writer('</td>\r\n\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<a href="/catalog/cart.remove/')
            __M_writer(str(item.product_id))
            __M_writer('" class="glyphicon glyphicon-trash"/>\r\n\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        __M_writer('\r\n\t</table>\r\n\r\n\r\n')
        if not cart:
            __M_writer('\t\t<h2>There are no items in your cart YET....(yet).......</h2>\r\n')
        __M_writer('\r\n\t<a href="/catalog/shipping/" class = "btn btn-primary pull-right">Proceed to checkout</a>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "cart.html", "line_map": {"64": 34, "65": 34, "66": 37, "67": 37, "68": 39, "69": 39, "70": 42, "71": 42, "72": 47, "73": 51, "74": 52, "75": 54, "17": 1, "30": 0, "81": 75, "38": 1, "39": 3, "44": 57, "50": 5, "57": 5, "58": 20, "59": 21, "60": 23, "61": 23, "62": 24, "63": 24}, "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/cart.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
