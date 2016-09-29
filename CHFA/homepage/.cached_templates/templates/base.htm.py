# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460005421.7532768
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'maintenance_message', 'main_menu', 'user_message', 'content_right', 'icon', 'title', 'footer', 'content_left']


from django_mako_plus import static_files 

import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        def user_message():
            return render_user_message(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def icon():
            return render_icon(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n    \r\n    \r\n')
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-2.2.1.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.css" />\r\n  \r\n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.min.css" />\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n      <header>\r\n        <div id="maintenance_message">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        \r\n        \r\n      \r\n        <div id="main_menu">\r\n          <nav class="navbar navbar-default  notroundy">\r\n            <!-- Site Icon -->\r\n            <div class="pull-left">\r\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'icon'):
            context['self'].icon(**pageargs)
        

        __M_writer('\r\n            </div><!-- pull-left -->\r\n\r\n            <!-- Login  -->\r\n            <div id="account_menu" class="pull-right">\r\n')
        if not request.user.is_authenticated():
            __M_writer('                <a class="btn btn-success" href="/account/signup/">Sign Up</a>\r\n                <button id="loginbutton" type="button" class="btn btn-primary">Login</button>\r\n')
        else:
            __M_writer('                <div class="dropdown">\r\n                  <button class="btn btn-default dropdown-toggle" type="button" id="account_menu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">\r\n                    Welcome, ')
            __M_writer(str( request.user.first_name ))
            __M_writer('!\r\n                    <span class="caret"></span>\r\n                  </button>\r\n                  <ul class="dropdown-menu" aria-labelledby="account_menu">\r\n                    <li><a href="/account/index/">Edit Information</a></li>\r\n                    <li><a href="/account/change/">Change Password</a></li>\r\n                    <li><a href="/manager/users/">Manage the Site</a></li>\r\n                    <li role="separator" class="divider"></li>\r\n                    <li><a href="/account/logout/">Logout</a></li>\r\n                  </ul>\r\n                </div>\r\n')
        __M_writer('            </div>\r\n\r\n            <!-- Main Nav menu -->\r\n            <div id="main_title" class="classy">\r\n              <img class = "main_title_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/title.png">\r\n\r\n              \r\n\r\n\r\n\r\n            </div><!-- main_title -->\r\n\r\n\r\n\r\n\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n              <ul id="main_menu_nav" class="nav navbar-nav pull-right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\r\n              </ul><!-- nav -->\r\n            </div><!-- navbar-collapse -->\r\n\r\n            <div class="clearfix"></div>\r\n\r\n          </nav><!-- navbar -->\r\n        </div><!-- main_menu -->\r\n        \r\n        <div id="user_message">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

        __M_writer('\r\n        </div>\r\n      \r\n      </header>\r\n  \r\n  \r\n    <div class="container-fluid">\r\n      <div class="row">\r\n        <div id="content_left" class="col-md-2">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n        </div><!-- left -->\r\n        <div id="content" class="col-md-8">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div><!-- center content -->\r\n        <div id="content_right" class="col-md-2">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n        </div><!-- right -->\r\n      </div><!-- row -->\r\n    </div><!-- container -->\r\n    \r\n    \r\n    <footer>  \r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n    </footer>\r\n    \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n          \r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def user_message():
            return render_user_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n          \r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def icon():
            return render_icon(context)
        __M_writer = context.writer()
        __M_writer('\r\n                 \r\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('CHF')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Copyright &copy; Benson Weeks ')
        __M_writer(str( datetime.date.today().year ))
        __M_writer('\r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n          \r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"128": 134, "129": 134, "196": 43, "135": 114, "141": 114, "17": 4, "19": 7, "21": 0, "153": 33, "159": 85, "165": 85, "177": 96, "220": 128, "171": 96, "47": 2, "48": 4, "49": 5, "178": 100, "53": 5, "54": 7, "184": 119, "59": 14, "60": 18, "61": 18, "62": 18, "63": 19, "64": 19, "65": 20, "66": 20, "67": 21, "68": 21, "69": 22, "70": 22, "71": 23, "72": 23, "73": 25, "74": 25, "75": 27, "76": 27, "77": 27, "208": 14, "82": 34, "214": 14, "87": 45, "88": 50, "89": 51, "90": 53, "91": 54, "92": 56, "93": 56, "94": 68, "95": 72, "96": 72, "226": 128, "227": 129, "228": 129, "101": 86, "106": 100, "111": 111, "240": 109, "147": 33, "116": 116, "190": 119, "246": 240, "202": 43, "121": 121, "234": 109, "126": 130, "127": 134}, "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
