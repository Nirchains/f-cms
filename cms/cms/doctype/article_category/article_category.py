# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.render import clear_cache

class ArticleCategory(WebsiteGenerator):

	def make_route(self):
		if not self.route:
			route = ""
			if self.parent_article_category:
				route = frappe.db.get_value('Article Category', self.parent_article_category,
				'route') + '/'
			return route + self.scrub(self.title)

	def autoname(self):
		# to override autoname of WebsiteGenerator
		self.name = self.article_category_name

	def on_update(self):
		clear_cache()
