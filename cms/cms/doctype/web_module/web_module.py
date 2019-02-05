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
                                fields="name,css_class")

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
    if module.module_type == "Menu":
        module.menu_items = __get_menu_items(module.parent_label)
    if module.module_type == "Module HTML":
		module.context = frappe.get_doc(module.module_type, module.module_name)
    return module

def __get_menu_items(parent_label):
    query = """\
        select url, label, target
        from `tabTop Bar Item`
        where 
        parent_label = '%(parent_label)s'
        order by `idx` asc""" % {
            "parent_label": parent_label
        }
        
    return frappe.db.sql(query, as_dict=1)