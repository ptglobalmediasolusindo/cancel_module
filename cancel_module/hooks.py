# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cancel_module"
app_title = "Cancel Module"
app_publisher = "DAS"
app_description = "Cancel all linked document after cancel SO / PO"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ptglobalmediasolusindo@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cancel_module/css/cancel_module.css"
# app_include_js = "/assets/cancel_module/js/cancel_module.js"

# include js, css files in header of web template
# web_include_css = "/assets/cancel_module/css/cancel_module.css"
# web_include_js = "/assets/cancel_module/js/cancel_module.js"

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
# get_website_user_home_page = "cancel_module.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cancel_module.install.before_install"
# after_install = "cancel_module.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cancel_module.notifications.get_notification_config"

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

doc_events = {
	"Sales Order": {
		"before_cancel": "cancel_module.cancel_modu.cancel_all_links_sales"
	},
    "Purchase Order": {
		"before_cancel": "cancel_module.cancel_modu.cancel_all_links_purchase"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cancel_module.tasks.all"
# 	],
# 	"daily": [
# 		"cancel_module.tasks.daily"
# 	],
# 	"hourly": [
# 		"cancel_module.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cancel_module.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cancel_module.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cancel_module.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cancel_module.event.get_events"
# }
