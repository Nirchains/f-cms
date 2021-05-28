# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.render import clear_cache
from frappe.utils import today, cint, global_date_format, get_fullname, strip_html_tags, markdown, sanitize_html
from frappe.website.utils import (find_first_image, get_html_content_based_on_type,
	get_comment_list)
from cms.cms.utils import normalize_url
from cms.cms.doctype.web_module.web_module import get_doctype_template_folder


class Article(WebsiteGenerator):

	def get_feed(self):
		return self.title

	def make_route(self):
		if not self.route:
			return frappe.db.get_value('Article Category', self.article_category,
				'route') + '/' + self.scrub(normalize_url(self.title))

	def validate(self):
		super(Article, self).validate()

		if not self.article_intro:
			content = get_html_content_based_on_type(self, 'content', self.content_type)
			#self.article_intro = content[:140]
			#self.article_intro = strip_html_tags(self.article_intro)

		if self.published and not self.published_on:
			self.published_on = today()

		if not self.order:
			self.order = frappe.db.sql("""select max(t.order)+1 as orden
				from `tab%s` t where t.article_category = '%s'""" % ("Article", self.article_category))[0][0]
						

	def on_update(self):
		clear_cache("writers")

	def get_context(self, context):
		# this is for double precaution. usually it wont reach this code if not published
		if not cint(self.published):
			raise Exception("El artículo no está publicado")

		#if self.blogger:
		#	context.blogger_info = frappe.get_doc("Blogger", self.blogger).as_dict()
		#	context.author = self.blogger

		context.content = get_html_content_based_on_type(self, 'content', self.content_type)
		#context.description = self.article_intro or strip_html_tags(context.content[:140])

		#context.modules = frappe.get_list("Web module", fields="*", 
        #filters={"parenttype": "Web Page", "parent": "investigadores"}, ignore_permissions=True)
		
		context.metatags = {
			"name": self.title,
			"description": context.description,
		}

		#
		context.category = frappe.db.get_value("Article Category", context.doc.article_category, ["title", "route", "parent_article_category", "img_bootstrap_size", "template"], as_dict=1)
		context.parents = []
		context.header = "<h1>{0}</h1>".format(context.category.title)
		context.doctype = self.doctype
		context.name = self.name

		context.template_dir = "cms/doctype/article/templates/"
		context.category.template = context.category.template or "article_base.html"
		context.template_dir = "{0}{1}".format(context.template_dir, context.category.template)
		
		#context.img_bootstrap_size = frappe.db.get_value('Module Article List', self.article_category,	'route')

		get_parent_category(context, context.category.parent_article_category)

		context.parents.append({"label": context.category.title, "route":context.category.route})

		context.parents.insert(0, {"name": _("Home"), "route":"/"})
		

def get_parent_category(context, article_category):
	category = frappe.db.get_value("Article Category", article_category, ["name", "title", "route", "parent_article_category", "published"], as_dict=1)
	#frappe.log_error("{0}".format(category))
	if category and category.published:
		context.parents.insert(0, {"label": category.title, "route": category.route})
		get_parent_category(context, category.parent_article_category)