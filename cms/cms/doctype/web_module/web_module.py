# -*- coding: utf-8 -*-
# Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, os
from frappe.model.document import Document

class Webmodule(Document):
	pass

"""Return array module_position
Carga los modulos adicionales de "Page Modules" en las posiciones correspondientes
"""
def load_module_positions_context(context):
    #module_position = {"Left": [], "Right": [], "Top": [], "Bottom": []}
    context.no_cache = True
    layout = {}
    layout['layout_positions'] = {}
    layout['module_positions'] = {}
    
    
    layout_positions = frappe.get_list("Layout posiciones", 
                                filters={'parent': 'Layout',
                                        'parenttype': 'Layout',
                                        'parentfield': 'positions_layout' },
                                fields="name,type,create_row,css_class,css_section,data_appear_animation,data_appear_animation_delay")

    for position in layout_positions:
        layout['layout_positions'][position.name] = position
        layout['module_positions'][position.name] = []

    #frappe.throw("{0}".format(context))

    for module in context.modules or []:
        module = __prepare_module(module)
        #frappe.throw("{0}".format(module))
        if module.enabled and module.context.enabled:
            layout['module_positions'][module.position].append(module)

    common_modules = frappe.get_list("Web module", 
                                filters={'parent': 'Common modules',
                                        'parenttype': 'Common modules',
                                        'parentfield': 'modules' },
                                order_by="idx asc",
                                fields="*", debug=False)

    #frappe.log_error("{0}".format(common_modules))

    for module in common_modules:
        module = __prepare_module(module)
        if module.enabled and module.context.enabled:
            try:
                layout['module_positions'][module.position].append(module)
            except:
                pass
        #frappe.throw("{0}".format(module))
        #layout['module_positions'][module.position].append(module)

    context.layout = layout

    return context

def has_web_edit_permission(context):
    context.has_web_edit_permission = False

    if ("Website Manager" in frappe.get_roles() and "Website Manager Frontend" in frappe.get_roles()):
        context.has_web_edit_permission = True
    
    return context

"""Actualiza las posiciones bootstrap
"""
def update_positions_size(module_positions, left_size = 0, right_size = 0):
    positions_size = {"Left": left_size, "Right": right_size, "Top": 12, "Bottom": 12, "Content": 12}
    if len(module_positions["Left"]) == 0:
        positions_size["Left"] = 0
    if len(module_positions["Right"]) == 0:
        positions_size["Right"] = 0
    positions_size["Content"] = 12 - positions_size["Left"] - positions_size["Right"]
    return positions_size

#En funcion del tipo de modulo, carga los campos adicionales
def __prepare_module(module):
    #if module.module_type == "Noticias":
        #module.news = get_latest_news(module.news_number)
    if module.module_type == "Module menu":
        try:
            module.context = frappe.get_doc(module.module_type, module.module_name)
            module.template_dir = 'cms/doctype/module_menu/templates/module_menu.html'
            module.template_dir = get_doctype_template_folder(module.context, module.template_dir)
        except Exception as e:
            frappe.throw("Module_type: {0} - Module_name: {1}".format(module.module_type, module.module_name))

        try:
            module.menu_items = __get_menu_items(module.context.parent_label)
        except Exception as e:
            frappe.throw("Module_type: {0} - Module_name: {1} - Parent label: {2} <br>{3}".format(module.module_type, module.module_name, module.context.parent_label, e))
       
    if module.module_type == "Module HTML":
        try:
            module.context = frappe.get_doc(module.module_type, module.module_name)
            module.template_dir = 'cms/doctype/module_html/templates/module_html.html'
            module.template_dir = get_doctype_template_folder(module.context, module.template_dir)
        except Exception as e:
            frappe.throw("Module_type: {0} - Module_name: {1}".format(module.module_type, module.module_name))

    if module.module_type == "Module Article List":
        try:
            module.context = frappe.get_doc(module.module_type, module.module_name)
            module.template_dir = "cms/doctype/module_article_list/templates/module_article_list.html"
            module.template_dir = get_doctype_template_folder(module.context, module.template_dir)
            
            frappe.log_error("{0}".format(module.template_dir))
            
            from cms.cms.doctype.module_article_list.module_article_list import __get_article_list
            module.article_list, module.categories = __get_article_list(module.context)
        except Exception as e:
            frappe.throw("Module_type: {0} - Module_name: {1}".format(module.module_type, module.module_name))
		
    return module

def __get_menu_items(parent_label):
    web_page = frappe.get_doc("Web Page", parent_label)

    query = """\
        select url, label, target
        from `tabTop Bar Item`
        where 
        parent_label = '%(parent_label)s'
        order by `idx` asc""" % {
            "parent_label": web_page.title
        }

    #frappe.log_error(query)
        
    return frappe.db.sql(query, as_dict=1)

def get_doctype_template_folder(doctypeobj, template_dir):
    if (doctypeobj.template):               
        path = doctypeobj.__class__.__module__
        arr_path = path.split(".")
        arr_path.pop()
        arr_path.pop(0)
        arr_path.append("templates")
        arr_path.append(doctypeobj.template)
        path = "/".join(arr_path)
    else:
        path = template_dir
    return path