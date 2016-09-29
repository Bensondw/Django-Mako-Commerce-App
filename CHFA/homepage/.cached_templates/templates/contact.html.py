# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458086634.8484502
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/CHFA/CHFA/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Contact Us')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <form action="/homepage/contact/" method="POST">\n    <table>\n      <tr>\n        <td>Your name:</td>\n        <td><input type="text" name="yourname" /></td>\n      </tr><tr>\n        <td>Your email:</td>\n        <td><input type="text" name="youremail" /></td>\n      </tr><tr>\n        <td>Message:</td>\n        <td><textarea name="yourmessage"></textarea></td>\n      </tr><tr colspan="2">\n        <td><input type="submit" value="Send Message"></td>\n      </tr>\n    </table>\n  </form>\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "line_map": {"65": 5, "59": 3, "53": 3, "71": 5, "42": 3, "47": 24, "28": 0, "77": 71, "37": 1}, "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/CHFA/CHFA/homepage/templates/contact.html"}
__M_END_METADATA
"""
