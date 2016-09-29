# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458091659.4986036
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/app_base.htm'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  ')

        menu_items = [
          [ 'Catalog',    'catalog',   'index'   ],
          [ 'Users',      'manager',   'users'   ],
          [ 'Products',   'manager',   'products'   ],
          [ 'Venues',     'manager',   'venues'   ],
          [ 'Events',     'manager',   'events'   ],
        ]
          
        
        __M_writer('\n\n\n')
        for title, app, page in menu_items:
            __M_writer('    <li class="')
            __M_writer(str( 'active' if request.dmp_router_app == app and request.dmp_router_page == page else '' ))
            __M_writer('"><a href="/')
            __M_writer(str( app ))
            __M_writer('/')
            __M_writer(str( page ))
            __M_writer('/">')
            __M_writer(str( title ))
            __M_writer('</a></li>\n')
        __M_writer('  \n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "line_map": {"64": 14, "65": 17, "66": 18, "67": 18, "36": 1, "69": 18, "70": 18, "71": 18, "72": 18, "73": 18, "74": 18, "75": 20, "46": 4, "81": 75, "53": 4, "54": 6, "68": 18, "28": 0}, "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/app_base.htm"}
__M_END_METADATA
"""
