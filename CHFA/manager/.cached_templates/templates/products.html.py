# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458159444.1059844
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


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
        isinstance = context.get('isinstance', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <p class="text-right"><a href="/manager/products.create/" class="btn btn-primary">Create Product</a></p>\n\n  <table class="table table-striped">\n    <tr>\n      <th>Name</th>\n      <th>Type</th>\n      <th>Picture</th>\n      <th>Price</th>\n      <th>Quantity</th>\n      <th>Actions</th>\n    </tr>\n    \n')
        for product in products:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str( product.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product.title ))
            __M_writer('</td>\n        <td>\n          <img class="img-thumbnail" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/product_images/')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('" />\n        </td>\n        <td>$')
            __M_writer(str( product.price ))
            __M_writer(' "and" ')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('</td>\n        <td>\n')
            if isinstance(product, cmod.BulkProduct):
                __M_writer('            <a class="refresh_quantity_button pull-right" href="/manager/products.get_quantity/')
                __M_writer(str( product.id))
                __M_writer('/"><span class="glyphicon glyphicon-refresh"></span></a>\n            <!-- I\'m hard coding the quantity here so I can demonstrate the update quantity button.  Normally we\'d put ')
                __M_writer(str( product.quantity ))
                __M_writer(' instead of the number 14. -->\n            <div class="text-center quantity">14</div>\n')
            __M_writer('        </td>\n        <td>\n          <a href="/manager/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n          |\n          <a href="/manager/products.delete/')
            __M_writer(str( product.id ))
            __M_writer('/" class="delete_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n  \n  \n  <!-- Modal -->\n  <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\n    <div class="modal-dialog" role="document">\n      <div class="modal-content">\n        <div class="modal-header">\n          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n          <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n        </div>\n        <div class="modal-body">\n          Delete this product?\n        </div>\n        <div class="modal-footer">\n          <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n          <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n        </div>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Current Users')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"68": 8, "69": 22, "70": 23, "71": 24, "72": 24, "73": 25, "74": 25, "75": 27, "76": 27, "77": 27, "78": 27, "79": 29, "80": 29, "17": 1, "82": 29, "83": 31, "84": 32, "85": 32, "86": 32, "87": 33, "88": 33, "89": 36, "90": 38, "91": 38, "92": 40, "93": 40, "30": 0, "112": 106, "100": 6, "81": 29, "42": 1, "43": 3, "48": 6, "106": 6, "53": 66, "59": 8, "94": 44}, "uri": "products.html", "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
