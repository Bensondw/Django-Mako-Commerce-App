# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458173456.9862936
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


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
        event = context.get('event', UNDEFINED)
        creating = context.get('creating', UNDEFINED)
        form = context.get('form', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        event = context.get('event', UNDEFINED)
        creating = context.get('creating', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <h1 class="text-center">Edit Event</h1>\n\n  <!-- EVENT FORM -->\n  <form method="POST">\n    <table id="myform">\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <input type="submit" class="btn btn-warning" value="')
        __M_writer(str( 'Save and Add Areas' if creating else 'Save' ))
        __M_writer('"/>\n  </form>\n  \n')
        if event.id:
            __M_writer('\n    <!-- AREAS FOR THIS EVENT -->  \n    <h3 class="text-center">Areas in this Event</h3>\n    <div class="text-right">\n      <a class="btn btn-success edit_area_button" href="/manager/events.edit_area/')
            __M_writer(str( event.id ))
            __M_writer('/None/">New Area</a>\n    </div>\n    <table class="table table-striped">\n      <tr>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Place Number</th>\n        <th>Actions</th>\n      </tr>\n')
            for area in event.areas.order_by('name').all():
                __M_writer('        <tr>\n          <td>')
                __M_writer(str( area.name ))
                __M_writer('</td>\n          <td>')
                __M_writer(str( area.description ))
                __M_writer('</td>\n          <td>')
                __M_writer(str( area.place_number ))
                __M_writer('</td>\n          <td>\n            <a class="edit_area_button" href="/manager/events.edit_area/')
                __M_writer(str( event.id ))
                __M_writer('/')
                __M_writer(str( area.id ))
                __M_writer('/">Edit</a>\n            |\n            <a class="delete_area_button" href="/manager/events.delete_area/')
                __M_writer(str( event.id ))
                __M_writer('/')
                __M_writer(str( area.id ))
                __M_writer('/">Delete</a>\n          </td>\n        </tr>\n')
            __M_writer('    </table>\n\n\n  \n    <!-- MODAL FOR DELETE CONFIRMATION -->\n    <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog">\n      <div class="modal-dialog" role="document">\n        <div class="modal-content">\n          <div class="modal-header">\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n            <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n          </div>\n          <div class="modal-body">\n            Delete this user?\n          </div>\n          <div class="modal-footer">\n            <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n            <button class="btn btn-default" data-dismiss="modal">Cancel</button>\n          </div>\n        </div>\n      </div>\n    </div>\n    \n')
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
        __M_writer('Edit Event')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 6, "66": 13, "67": 13, "68": 15, "69": 15, "70": 19, "71": 20, "72": 24, "73": 24, "74": 33, "75": 34, "76": 35, "77": 35, "78": 36, "79": 36, "80": 37, "81": 37, "82": 39, "83": 39, "84": 39, "85": 39, "86": 41, "87": 41, "88": 41, "89": 41, "90": 45, "91": 69, "28": 0, "97": 4, "103": 4, "40": 1, "45": 4, "50": 70, "56": 6, "109": 103}, "filename": "C:/Users/hbll-uarm/Desktop/chf4/CHFA/CHFA/manager/templates/events.edit.html", "source_encoding": "utf-8", "uri": "events.edit.html"}
__M_END_METADATA
"""
