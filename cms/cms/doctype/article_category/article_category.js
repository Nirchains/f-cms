// Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article Category', {
	refresh: function(frm) {
		modulo.load_templates(frm, "Article"); 
	}
});
