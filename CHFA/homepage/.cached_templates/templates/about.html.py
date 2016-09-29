# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460047459.6417575
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/about.html'
_template_uri = 'about.html'
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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
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
        __M_writer = context.writer()
        __M_writer("\n  \n\n\t<h2>The Colonial Heritage Foundation</h2>\n\n\t<p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America's founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America's historical writings, the presentation of lectures and seminars regarding America's founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</p>\n\n\n\t<h2>Education Exhibits</h2>\n\n\t<p>At its heart, the Foundation is an educational institution.  One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America's colonial period and is founding generation.  To this end, the Foundation has developed a variety of traveling exhibits.  One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.  The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence.\n\nAnother exhibit focuses on the early colonial period and the ides of self-government that were planted in Jamestowne and Plimoth.  At the center of this exhibit is a scale model of the Mayflower. The exhibit also includes replicas of various artifacts from the early colonial period.</p>\n\n\n\t<h2>Reading and Discussion Groups</h2>\n\n\t<p>The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America's historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America's current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation. </p>\n\n\n\t<h2>Workshops, Lectures, and seminars</h2>\n\t\n\t<p>The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America's founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today's population with the freedoms we enjoy. These events  seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America's founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee.</p>\n\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "about.html", "line_map": {"35": 1, "52": 3, "40": 28, "58": 52, "28": 0, "46": 3}, "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/homepage/templates/about.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
