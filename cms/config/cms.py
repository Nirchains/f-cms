# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Módulos"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Module HTML",
					"description": _(""),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Module menu",
					"description": _(""),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Module Article List",
					"description": _(""),
					"onboard": 1,
				}
			]
		},
		{
			"label": _("Páginas"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Web Page",
					"description": _("Content web page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Web Form",
					"description": _("User editable form on Website."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Common modules",
					"description": _(""),
					"onboard": 1,
				},
			]
		},
		{
			"label": _("Web Site"),
			"icon": "fa fa-star",
			"items": [
				
				{
					"type": "doctype",
					"name": "Website Sidebar",
				},
				{
					"type": "doctype",
					"name": "Website Slideshow",
					"description": _("Embed image slideshows in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Route Meta",
					"description": _("Add meta tags to your web pages"),
				},
			]
		},
		{
			"label": _("Artículos"),
			"items": [
				{
					"type": "doctype",
					"name": "Article",
					"description": _("Single article."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Blogger",
					"description": _("A user who posts blogs."),
				},
				{
					"type": "doctype",
					"name": "Article Category",
					"description": _("Categorize articles."),
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Website Settings",
					"description": _("Setup of top navigation bar, footer and logo."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Script",
					"description": _("Javascript to append to the head section of the page."),
				},
				{
					"type": "doctype",
					"name": "CSS Class",
					"description": _(""),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Layout",
					"description": _(""),
					"onboard": 1,
				},
			]
		},
	]