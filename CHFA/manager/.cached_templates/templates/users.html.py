# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458091659.484603
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <p class="text-right"><a href="/manager/users.create/" class="btn btn-primary">New User</a></p>\n\n  <table class="table table-striped">\n    <tr>\n      <th>Username</th>\n      <th>First Name</th>\n      <th>Last Name</th>\n      <th>Email</th>\n      <th>Groups</th>\n      <th>Actions</th>\n    </tr>\n  \n')
        for user in users:
            __M_writer('      <tr>\n        <td>\n          ')
            __M_writer(str( user.username ))
            __M_writer('\n        </td>\n        <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\n        <td></td>\n        <td>\n          <a href="/manager/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a>\n          |\n          <a href="/manager/users.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class="delete_button">Delete</a>\n        </td>\n      </tr>\n      \n      \n')
        __M_writer('  </table>\n  \n  \n  <!-- Modal -->\n  <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\n    <div class="modal-dialog" role="document">\n      <div class="modal-content">\n        <div class="modal-header">\n          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n          <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n        </div>\n        <div class="modal-body">\n          Delete this user?\n        </div>\n        <div class="modal-footer">\n          <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n          <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n        </div>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "line_map": {"66": 6, "73": 6, "74": 20, "75": 21, "76": 23, "77": 23, "78": 25, "79": 25, "80": 26, "81": 26, "82": 27, "83": 27, "84": 30, "85": 30, "86": 32, "87": 32, "88": 38, "28": 0, "94": 88, "38": 1, "43": 4, "48": 60, "54": 4, "60": 4}, "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/users.html"}
__M_END_METADATA
"""
