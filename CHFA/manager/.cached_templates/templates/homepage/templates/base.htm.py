# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459884064.5367608
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['maintenance_message', 'icon', 'content_right', 'main_menu', 'user_message', 'content_left', 'title', 'content', 'footer']


from django_mako_plus import static_files 

import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def maintenance_message():
            return render_maintenance_message(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def icon():
            return render_icon(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def user_message():
            return render_user_message(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n    \n    \n')
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-2.2.1.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.js"></script>\n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.css" />\n  \n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.min.css" />\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n  </head>\n  <body>\n      <header>\n        <div id="maintenance_message">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintenance_message'):
            context['self'].maintenance_message(**pageargs)
        

        __M_writer('\n        </div>\n        \n        \n      \n        <div id="main_menu">\n          <nav class="navbar navbar-default  notroundy">\n            <!-- Site Icon -->\n            <div class="pull-left">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'icon'):
            context['self'].icon(**pageargs)
        

        __M_writer('\n            </div><!-- pull-left -->\n\n            <!-- Login  -->\n            <div id="account_menu" class="pull-right">\n')
        if not request.user.is_authenticated():
            __M_writer('                <a class="btn btn-success" href="/account/signup/">Sign Up</a>\n                <button id="loginbutton" type="button" class="btn btn-primary">Login</button>\n')
        else:
            __M_writer('                <div class="dropdown">\n                  <button class="btn btn-default dropdown-toggle" type="button" id="account_menu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">\n                    Welcome, ')
            __M_writer(str( request.user.first_name ))
            __M_writer('!\n                    <span class="caret"></span>\n                  </button>\n                  <ul class="dropdown-menu" aria-labelledby="account_menu">\n                    <li><a href="/account/index/">Edit Information</a></li>\n                    <li><a href="/account/change/">Change Password</a></li>\n                    <li><a href="/manager/users/">Manage the Site</a></li>\n                    <li role="separator" class="divider"></li>\n                    <li><a href="/account/logout/">Logout</a></li>\n                  </ul>\n                </div>\n')
        __M_writer('            </div>\n\n            <!-- Main Nav menu -->\n            <div id="main_title" class="classy">\n              Colonial Heritage Foundation\n            </div><!-- main_title -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul id="main_menu_nav" class="nav navbar-nav pull-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\n              </ul><!-- nav -->\n            </div><!-- navbar-collapse -->\n\n            <div class="clearfix"></div>\n\n          </nav><!-- navbar -->\n        </div><!-- main_menu -->\n        \n        <div id="user_message">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

        __M_writer('\n        </div>\n      \n      </header>\n  \n  \n    <div class="container-fluid">\n      <div class="row">\n        <div id="content_left" class="col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n        </div><!-- left -->\n        <div id="content" class="col-md-8">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div><!-- center content -->\n        <div id="content_right" class="col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n        </div><!-- right -->\n      </div><!-- row -->\n    </div><!-- container -->\n    \n    \n    <footer>  \n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n    </footer>\n    \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintenance_message():
            return render_maintenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def icon():
            return render_icon(context)
        __M_writer = context.writer()
        __M_writer('\n                 <a  href="/">\n                  <img class = "magic" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/lincoln.jpg" />\n                </a>\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n          \n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def user_message():
            return render_user_message(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n          \n          ')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n          \n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n        Copyright &copy; Benson Weeks ')
        __M_writer(str( datetime.date.today().year ))
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "/homepage/templates/base.htm", "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/base.htm", "line_map": {"133": 33, "139": 33, "17": 4, "19": 7, "21": 0, "152": 43, "153": 45, "154": 45, "197": 102, "160": 112, "247": 241, "166": 112, "221": 107, "172": 78, "47": 2, "48": 4, "49": 5, "178": 78, "53": 5, "54": 7, "215": 14, "184": 89, "59": 14, "60": 18, "61": 18, "62": 18, "63": 19, "64": 19, "65": 20, "66": 20, "67": 21, "68": 21, "69": 22, "70": 22, "71": 23, "72": 23, "73": 25, "74": 25, "75": 27, "76": 27, "77": 27, "209": 14, "82": 34, "227": 107, "203": 102, "87": 47, "88": 52, "89": 53, "90": 55, "91": 56, "92": 58, "93": 58, "94": 70, "99": 79, "145": 43, "104": 93, "233": 121, "109": 104, "239": 121, "240": 122, "241": 122, "114": 109, "190": 89, "119": 114, "191": 93, "124": 123, "125": 127, "126": 127, "127": 127}}
__M_END_METADATA
"""
