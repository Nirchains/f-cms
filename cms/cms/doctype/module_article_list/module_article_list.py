#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, os
import json
from frappe.model.document import Document
from frappe.website.render import clear_cache
from frappe.model.naming import set_name_from_naming_options
from frappe.modules import scrub, get_module_path, load_doctype_module


class ModuleArticleList(Document):

    def autoname(self):
        set_name_from_naming_options(frappe.get_meta(self.doctype).autoname, self)
        self.name = '{0}-{1}'.format(self.name, self.title)

    def on_update(self):
        clear_cache()

@frappe.whitelist()
def load_templates():
    #todo
    path = os.path.dirname(os.path.abspath(__file__))

    path = "{0}/{1}".format(path, "templates")
    templates = []
    try:
        for fname in os.listdir(path):
            if fname.endswith(".html"):
                templates.append(fname)
    except:
        pass

    return templates


def __get_article_list(context):
    l_categories = []
    article_list = {}
    context.n_articles = 0
    context.n_pags = 1
    context.show_pagination = (context.pagination > 0) and (context.format != "Listado")

    filters = {}

    for category in context.categories:
        l_categories.append(category.category)

        article_list[category.category] = __get_article_categories([category.category],context)

        if context.include_subcategories:
            subcategories = frappe.get_list(
                'Article Category',
                fields='name',
                filters={'parent_article_category': category.category},
                order_by=context.category_order,
                ignore_permissions=True,
                debug=True,
                )

            for sc in subcategories:
                if context.format != "Categorías":
                    l_categories.append(sc.name)
                else:
                    article_list[sc.name] = __get_article_categories([sc.name],context)
                    l_categories.append(sc.name)

    #if context.format != "Categorías":
    #    article_list['Todas las categorias'] = __get_article_categories(l_categories,context)

    if context.n_articles > 1 and context.show_pagination:
        context.n_pags = int(((context.n_articles-1) / context.pagination) + 1)

    return (article_list, l_categories)


def __get_article_categories(l_categories, context):
    filters = {}
    limit_start = 0
    context.actual_page = 1    
    
    if context.show_pagination:
        parametros = frappe.local.form_dict
        if parametros:
            if parametros.p:
                context.actual_page = int(parametros.p)
                limit_start = (context.actual_page - 1) * context.pagination
    else:
        limit_start = 0

    filters = {
        'article_category': ['in', l_categories],
        'published': 1
    }
        
    #filters['article_category'] = ('in', ','.join(map(str,l_categories)))
    #filters['published'] = 1

    #frappe.log_error("{0}<br><br>{1}".format(filters, json.dumps(filters)))

    article_list = frappe.get_list('Article', filters=filters, order_by=context.article_order,
                           fields='*', ignore_permissions=True, limit_start=limit_start, limit_page_length=context.pagination,debug=False)


    context.n_articles += int(frappe.db.count("Article", filters, debug=True))
        
    return article_list
