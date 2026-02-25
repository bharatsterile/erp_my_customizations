app_name = "my_customizations"
app_title = "My Customizations"
app_publisher = "Amit"
app_description = "My Customizations"
app_email = "amit@clubcodetechnology.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "my_customizations",
# 		"logo": "/assets/my_customizations/logo.png",
# 		"title": "My Customizations",
# 		"route": "/my_customizations",
# 		"has_permission": "my_customizations.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_customizations/css/my_customizations.css"
# app_include_js = "/assets/my_customizations/js/my_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_customizations/css/my_customizations.css"
# web_include_js = "/assets/my_customizations/js/my_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "my_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "my_customizations/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "my_customizations.utils.jinja_methods",
# 	"filters": "my_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "my_customizations.install.before_install"
# after_install = "my_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "my_customizations.uninstall.before_uninstall"
# after_uninstall = "my_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "my_customizations.utils.before_app_install"
# after_app_install = "my_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "my_customizations.utils.before_app_uninstall"
# after_app_uninstall = "my_customizations.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "my_customizations.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"my_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"my_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"my_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"my_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"my_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "my_customizations.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "my_customizations.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "my_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "my_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["my_customizations.utils.before_request"]
# after_request = ["my_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["my_customizations.utils.before_job"]
# after_job = ["my_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"my_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []
fixtures = [
    {
        "dt": "Property Setter",
        "filters": [
            ["doc_type", "in", ["Purchase Invoice", "Purchase Receipt", "BOM", "BOM Item", "BOM Scrap Item", "Production Plan", "Stock Entry" ,"Employee", "Vehicle In Permissions", "Vehicle In", "Vehicle Out Permission", "Vehicle Out", "Visitor Permission", "Visitor In", "Visitor Out", "Employee Permission", "Employee In", "Employee Out", "Courier In", "Courier Out", "Courior Out Detail"]]
        ]
    },
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", ["Purchase Invoice", "Purchase Receipt", "BOM", "BOM Item", "BOM Scrap Item", "Production Plan", "Stock Entry", "Vehicle In Permissions", "Vehicle In", "Vehicle Out Permission", "Vehicle Out", "Visitor Permission", "Visitor In", "Visitor Out", "Employee Permission", "Employee In", "Employee Out", "Courier In", "Courier Out", "Courior Out Detail"]]
        ]
    },
	{
    "dt":"Client Script",
	},
	{
    "dt":"Server Script"
	},	
    {
        "dt": "Item Group"
    },
    {
        "dt": "Workspace",
        "filters": [
            ["name", "=", "Gate Entry"]
        ]
    },
    {
    "dt": "Print Format",
    "filters": [
        ["name", "in", [
            "Vehicle In Receipt",
            "Visitor In Receipt",
            "Employee In Receipt",
			"Courier In Receipt"
        ]]
    ]
    },
    # ROLE MASTER
    # --------------------
    {
        "dt": "Role",
        "filters": [
            ["name", "not in", ["Administrator", "Guest", "All"]]
        ]
    },

    # --------------------
    # ROLE PERMISSIONS (DocType Permission)
    # --------------------
    {
        "dt": "Custom DocPerm"
    },
    {
        "dt": "Warehouse",
        "filters": [
            ["company", "=", "BHARAT STERILE PRIVATE LIMITED"]
        ]
    }
]
