# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458428408.2028458
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/catalog/templates/detail.carousel.html'
_template_uri = 'detail.carousel.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        images = context.get('images', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        images = context.get('images', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\r\n\r\n\t<!-- images will go here -->\r\n')
        for image_obj in images:
            __M_writer('\t\t<img class="pimage hide" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/product_images/')
            __M_writer(str(image_obj.filename))
            __M_writer('"/>\r\n')
        __M_writer('\r\n\t<button class="btn btn-warning pull-left previous">Previous</button>\r\n\t<button class="btn btn-warning pull-right next">Next</button>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/catalog/templates/detail.carousel.html", "line_map": {"68": 62, "37": 1, "60": 10, "47": 4, "55": 4, "56": 9, "57": 10, "58": 10, "59": 10, "28": 0, "61": 10, "62": 12}, "uri": "detail.carousel.html"}
__M_END_METADATA
"""
