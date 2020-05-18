frappe.provide("modulo");

modulo = {
	init_onload: function(frm) {
		frm.set_query("css_class", function() {
			return {
				"filters": {
					"type": "tag"
				}
			};
		});

		frm.set_query("css_title", function() {
			return {
				"filters": {
					"type": "title"
				}
			};
		});
	},
	init_refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(__("Ver páginas"),
				function() {
					frappe.route_options = {
						"module_type": frm.doctype,
						"module_name": frm.doc.name
					};
					frappe.set_route("List", "Web Page");
				}
			);
		}
	}
};