// Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Module Article List', {
	onload: function(frm) {
		modulo.init_onload(frm);		
	},
	refresh: function (frm) {
        modulo.init_refresh(frm);        
    },
});
