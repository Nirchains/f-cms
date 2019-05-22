# -*- coding: utf-8 -*-
# Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ModuleHTML(Document):
	def on_update(self):
		frappe.clear_cache()
