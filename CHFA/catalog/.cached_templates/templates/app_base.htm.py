# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460006642.7230594
_enable_loop = True
_template_filename = 'C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_left', 'content_right', 'main_menu']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        categories = context.get('categories', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n\r\n\r\n<!-- content right with last five will go here -->\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n\t<h3 class="text-center"><a href="/catalog/index/" class = "btn btn-warning"> View All Products</a></h3>\r\n\r\n\t<h3>Search</h3>\r\n\t<div id="search_container">\r\n\t\t<form action="/catalog/search/" method="GET">\r\n\t\t\t<input type="text" name="q" class="sizing" />\r\n\t\t\t<button type="submit" class="search_button"><span class="glyphicon glyphicon-triangle-right">\r\n\t\t</form>\r\n\t</div>\r\n\r\n\t<h3>Categories</h3>\r\n\t<ul id="categories_list">\t\t\t\r\n\r\n')
        for category in categories:
            __M_writer('\t\t\t<li> <a href="/catalog/index/')
            __M_writer(str( category.id ))
            __M_writer('/">')
            __M_writer(str(category.name))
            __M_writer('</a> </li>\r\n')
        __M_writer('\r\n\t</ul>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h3> Recently Viewed: </h3>\r\n\r\n\r\n\t<ul id="last_viewed">\t\t \r\n')
        for product in request.shopping_cart.get_viewed_items():
            __M_writer('\t\t\t\t<li class="viewed_item">\r\n\t\t\t\t\t<a href = "/catalog/detail/')
            __M_writer(str(product.id))
            __M_writer('/">\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t<img class="img-thumbnail" src=" ')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/product_images/')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('"/>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t')
            __M_writer(str(product.name))
            __M_writer('\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</a>\r\n\t\t\t\t</li>\r\n')
        __M_writer('\t</ul>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t')

        menu_items = [
                [ 'Home',       'homepage',  'index'   ],
                [ 'Contact Us', 'homepage',  'contact' ],
                [ 'About Us',   'homepage',  'about'   ],
                [ 'Catalog',    'catalog',   'index'   ],
                
        ]
                
        
        __M_writer('\r\n\r\n')
        for title, app, page in menu_items:
            __M_writer('\t\t<li class="')
            __M_writer(str( 'active' if request.dmp_router_app == app and request.dmp_router_page == page else '' ))
            __M_writer('">\r\n\t\t\t<a href="/')
            __M_writer(str( app ))
            __M_writer('/')
            __M_writer(str( page ))
            __M_writer('/">\r\n\t\t\t\t')
            __M_writer(str( title ))
            __M_writer('\r\n\t\t\t</a>\r\n\t\t</li>\r\n')
        __M_writer('\t\t<a href = "/catalog/cart/" id="shopping_cart_button" class = "btn btn-info glyphicon glyphicon-shopping-cart pull-right">\r\n\t\t\t<span id="num_items"></span>\r\n\t\t</a>\r\n\t  <!-- # above should bring you to the cart, to dsiplay the number you need to use some js -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "line_map": {"128": 18, "129": 18, "130": 19, "131": 19, "132": 19, "69": 31, "70": 46, "71": 47, "72": 47, "73": 47, "74": 47, "75": 47, "76": 49, "135": 20, "142": 136, "82": 56, "90": 56, "91": 61, "92": 62, "93": 63, "94": 63, "95": 65, "96": 65, "97": 65, "98": 65, "99": 68, "100": 68, "101": 73, "133": 19, "28": 0, "42": 1, "107": 6, "47": 28, "136": 24, "114": 6, "115": 7, "52": 52, "126": 17, "134": 20, "125": 15, "62": 31, "127": 18}, "filename": "C:/Users/hbll-uarm/Desktop/SF/CHFA/catalog/templates/app_base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
