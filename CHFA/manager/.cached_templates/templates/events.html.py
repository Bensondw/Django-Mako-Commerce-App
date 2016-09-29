# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458091677.5256348
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        __M_writer('Events')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <p class="text-right"><a href="/manager/events.edit/" class="btn btn-primary">New Event</a></p>\n\n  <table class="table table-striped">\n    <tr>\n      <th>Name</th>\n      <th>Description</th>\n      <th>Venue</th>\n      <th>Start Date</th>\n      <th>End Date</th>\n      <th>Actions</th>\n    </tr>\n  \n')
        for event in events:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str( event.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( event.venue.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( event.start_date.strftime('%Y-%m-%d') ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( event.end_date.strftime('%Y-%m-%d') ))
            __M_writer('</td>\n        <td>\n          <a href="/manager/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('/">Edit</a>\n          |\n          <a href="/manager/events.delete/')
            __M_writer(str( event.id ))
            __M_writer('/" class="delete_button">Delete</a>\n        </td>\n      </tr>\n      \n      \n')
        __M_writer('  </table>\n  \n  \n  <!-- Modal -->\n  <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\n    <div class="modal-dialog" role="document">\n      <div class="modal-content">\n        <div class="modal-header">\n          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n          <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n        </div>\n        <div class="modal-body">\n          Delete this event?\n        </div>\n        <div class="modal-footer">\n          <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n          <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n        </div>\n      </div>\n    </div>\n  </div>\n  \n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "line_map": {"66": 6, "73": 6, "74": 20, "75": 21, "76": 22, "77": 22, "78": 23, "79": 23, "80": 24, "81": 24, "82": 25, "83": 25, "84": 26, "85": 26, "86": 28, "87": 28, "88": 30, "89": 30, "90": 36, "28": 0, "96": 90, "38": 1, "43": 4, "48": 60, "54": 4, "60": 4}, "source_encoding": "utf-8", "filename": "C:/Users/hbll-uarm/Desktop/CHFA/CHFA/manager/templates/events.html"}
__M_END_METADATA
"""
