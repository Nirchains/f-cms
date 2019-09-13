# -*- coding: utf-8 -*-
# Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Webmodule(Document):
	pass

"""Return array module_position
Carga los modulos adicionales de "Page Modules" en las posiciones correspondientes
"""
def load_module_positions(page_modules):
    #module_position = {"Left": [], "Right": [], "Top": [], "Bottom": []}
    module_position = {}
    layout = {}
    
    layout_positions = frappe.get_list("Layout posiciones", 
                                filters={'parent': 'Layout',
                                        'parenttype': 'Layout',
                                        'parentfield': 'positions_layout' },
                                fields="name,type,css_class,css_section,data_appear_animation,data_appear_animation_delay")

    for position in layout_positions:
        layout[position.name] = position
        module_position[position.name] = []

    for module in page_modules:
        module = __prepare_module(module)
        #frappe.throw("{0}".format(module))
        module_position[module.position].append(module)

    common_modules = frappe.get_list("Web module", 
                                filters={'parent': 'Common modules',
                                        'parenttype': 'Common modules',
                                        'parentfield': 'modules' },
                                fields="*")

    for module in common_modules:
        module = __prepare_module(module)
        #frappe.throw("{0}".format(module))
        module_position[module.position].append(module)

    return module_position, layout

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
                                fields="name,type,css_class,css_section,data_appear_animation,data_appear_animation_delay")

    for position in layout_positions:
        layout['layout_positions'][position.name] = position
        layout['module_positions'][position.name] = []

    #frappe.throw("{0}".format(context))

    for module in context.modules or []:
        module = __prepare_module(module)
        #frappe.throw("{0}".format(module))
        layout['module_positions'][module.position].append(module)

    common_modules = frappe.get_list("Web module", 
                                filters={'parent': 'Common modules',
                                        'parenttype': 'Common modules',
                                        'parentfield': 'modules' },
                                fields="*")

    for module in common_modules:
        module = __prepare_module(module)
        #frappe.throw("{0}".format(module))
        layout['module_positions'][module.position].append(module)

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
            module.menu_items = __get_menu_items(module.context.parent_label)
        except Exception as e:
            frappe.throw("Module_type: {0} - Module_name: {1}".format(module.module_type, module.module_name))
       
    if module.module_type == "Module HTML":
        try:
            module.context = frappe.get_doc(module.module_type, module.module_name)
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