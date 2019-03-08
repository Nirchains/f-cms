// Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Layout', {
	onload: function(frm) {
		frm.set_query("css_class", function() {
			return {
				"filters": {
					"type": "tag"
				}
			};
		});
	},
	refresh: function(frm) {

	}
});
