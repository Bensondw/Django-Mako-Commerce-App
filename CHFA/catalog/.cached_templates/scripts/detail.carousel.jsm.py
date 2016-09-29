# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458341451.5797958
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/catalog/scripts/detail.carousel.jsm'
_template_uri = 'detail.carousel.jsm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('//this will handle the logic of carouseling images\r\n\r\n\r\n$(function() {\r\n\tconsole.log("beginning");\r\n\r\n\t$(\'.pimage\').first().removeClass(\'hide\');\r\n\r\n\t$(\'.previous\').click(function() {\r\n\r\n\t\tvar current = $(\'.pimage:not(.hide)\');\r\n\t\tvar next = current.prev(\'.pimage\');\r\n\r\n\t\tif (next.length == 0 ) {\r\n\t\t\tnext = current.nextAll().last();\r\n\t\t}\r\n\t\tcurrent.addClass(\'hide\');\r\n\t\tnext.removeClass(\'hide\');\r\n\r\n\t}); // show images modal\r\n\r\n\t$(\'.next\').click(function() {\r\n\r\n\t\tvar current = $(\'.pimage:not(.hide)\');\r\n\t\tvar next = current.next(\'.pimage\');\r\n\r\n\t\tif (next.length == 0 ) {\r\n\t\t\tnext = current.prevAll().last();\r\n\t\t}\r\n\t\tcurrent.addClass(\'hide\');\r\n\t\tnext.removeClass(\'hide\');\r\n\r\n\t}); // show images modal\r\n\r\n\tconsole.log("end");\r\n});\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "detail.carousel.jsm", "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/catalog/scripts/detail.carousel.jsm", "line_map": {"17": 0, "28": 22, "22": 1}}
__M_END_METADATA
"""
