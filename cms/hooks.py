# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cms"
app_title = "CMS"
app_publisher = "Pedro Antonio Fernández Gómez"
app_description = "CMS frappe framework"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pedro@hispalisdigital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cms/css/cms.css"
app_include_js = ["assets/cms/js/build/custom.min.js", "/assets/cms/vendor/autoresize/autoresize.jquery.min.js"]

# include js, css files in header of web template
web_include_css = ["assets/cms/css/build/vendor.css", "assets/cms/css/build/theme.css", "assets/cms/css/build/rs-plugin.css", "assets/cms/css/build/custom.css", "assets/cms/css/build/skin.css"]
web_include_js =  []

doctype_js = {
    "Web Page":[
        "custom_script/web_page.js"
    ]
}

fixtures=['Custom Field', 'Property Setter','Print Format','Custom Script', 'Domain', 'Module Def']


update_website_context_all = 'cms.cms.doctype.web_module.web_module.load_module_positions_context'

#website_context = {
#	'layout': 'cms.cms.doctype.web_module.web_module.load_module_positions_context'
#}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cms.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cms.install.before_install"
# after_install = "cms.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cms.tasks.all"
# 	],
# 	"daily": [
# 		"cms.tasks.daily"
# 	],
# 	"hourly": [
# 		"cms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cms.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cms.event.get_events"
# }

