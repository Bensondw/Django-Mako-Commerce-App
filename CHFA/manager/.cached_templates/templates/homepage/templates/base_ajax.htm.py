# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458337095.0037813
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/homepage/templates/base_ajax.htm'
_template_uri = '/homepage/templates/base_ajax.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  Sub-templates should place their ajax content here.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 7, "35": 10, "36": 10, "49": 13, "41": 15, "42": 18, "43": 18, "61": 55, "17": 6, "19": 0, "55": 13, "28": 4, "29": 6, "30": 7}, "uri": "/homepage/templates/base_ajax.htm", "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/homepage/templates/base_ajax.htm"}
__M_END_METADATA
"""
