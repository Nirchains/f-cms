// Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Module HTML', {
	onload: function(frm) {
		module.init(frm);
	},
	refresh: function(frm) {

	}
});
