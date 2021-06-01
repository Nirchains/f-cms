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
		this.load_templates(frm, frm.doctype);

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
	},
	load_templates: function(frm, doctype) {
		frappe.call({
			method: "cms.cms.utils.load_templates",
			args: {
				doctype: doctype
			},
			callback: function(data) {
				console.log(data);
				if (data.message.length > 0) {
					frm.set_df_property("template", "options", data.message);
					if (frm.doc.template) {
						frm.set_value("template", frm.doc.template);
					} else {
						frm.set_value("template", data.message[0]);
					}
				}

			}
		});
	}
};