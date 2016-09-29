# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458337094.995781
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/events.edit_area.html'
_template_uri = 'events.edit_area.html'
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
        area = context.get('area', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        area = context.get('area', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <form id="areaform" action="/manager/events.edit_area/')
        __M_writer(str( event.id ))
        __M_writer('/')
        __M_writer(str( area.id ))
        __M_writer('/" method="POST">\n    <table>\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <input type="submit" class="btn btn-primary" value="Save"/>\n  </form>\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 9, "70": 64, "38": 1, "28": 0, "43": 14, "49": 5, "58": 5, "59": 7, "60": 7, "61": 7, "62": 7, "63": 9}, "uri": "events.edit_area.html", "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/events.edit_area.html"}
__M_END_METADATA
"""
