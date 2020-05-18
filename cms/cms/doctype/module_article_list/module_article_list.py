# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.website.render import clear_cache

class ModuleArticleList(Document):
	def on_update(self):
		clear_cache()

def __get_article_list(context):

    l_categories = []
    article_list = {}

    filters = {}

    for category in context.categories:
        l_categories.append(category.category)

        article_list[category.category] = __get_article_categories([category.category], context.article_order)

        if context.include_subcategories:
            subcategories = frappe.get_list("Article Category", fields="name", 
                            filters={"parent_article_category": category.category}, 
                            order_by=context.category_order, ignore_permissions=True, debug=True)

            for sc in subcategories:
                if context.format != "Categorías":
                    l_categories.append(sc.name)
                else:
                    article_list[sc.name] = __get_article_categories([sc.name], context.article_order)


    if context.format != "Categorías":
        article_list["Todas las categorias"] = __get_article_categories(l_categories, context.article_order)

    return article_list

def __get_article_categories(l_categories, order):
    filters = {}

    filters["article_category"] = ("in",",".join(map(str, l_categories)))
    filters["published"] = 1
    return frappe.get_list("Article", 
                                filters=filters, order_by=order,
                                fields="*", ignore_permissions=True)