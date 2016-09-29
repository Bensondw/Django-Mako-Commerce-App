# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460046698.348214
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main_menu']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  ')

        menu_items = [
          [ 'Home',       'homepage',  'index'   ],
          [ 'Contact Us', 'homepage',  'contact' ],
          [ 'About Us',   'homepage',  'about'   ],
          [ 'Catalog',    'catalog',   'index'   ],
          
        ]
          
        
        __M_writer('\r\n\r\n')
        for title, app, page in menu_items:
            __M_writer('    <li class="')
            __M_writer(str( 'active' if request.dmp_router_app == app and request.dmp_router_page == page else '' ))
            __M_writer(' pull-left"><a href="/')
            __M_writer(str( app ))
            __M_writer('/')
            __M_writer(str( page ))
            __M_writer('/">')
            __M_writer(str( title ))
            __M_writer('</a></li>\r\n')
        __M_writer('  <a href = "/catalog/cart/" id="shopping_cart_button" class = "btn btn-info glyphicon glyphicon-shopping-cart pull-right">\r\n    <span id="num_items"></span>\r\n  </a>\r\n  <!-- # above should bring you to the cart, to diplay the number you need to use some js -->\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "line_map": {"64": 14, "65": 16, "66": 17, "67": 17, "36": 1, "69": 17, "70": 17, "71": 17, "72": 17, "73": 17, "74": 17, "75": 19, "46": 4, "81": 75, "53": 4, "54": 6, "68": 17, "28": 0}, "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/app_base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
