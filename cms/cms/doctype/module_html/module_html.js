// Copyright (c) 2019, Pedro Antonio Fernández Gómez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Module HTML', {
	onload: function(frm) {
		modulo.init_onload(frm);

		if (!Jodit.instances.jeditor_webpage) {
            $('<textarea id="jeditor_webpage"></textarea>').appendTo(frm.fields_dict.content_jodit.wrapper);
            var ele = document.getElementById('jeditor_webpage');
            var editor = new Jodit(ele);
            

            editor.value = frm.doc.content || "";
            ele.addEventListener('change', function () {
                frm.set_value("content", this.value);
            });
        }
	},
	refresh: function (frm) {
        modulo.init_refresh(frm);
        let editor = Jodit.instances.jeditor_webpage
        if (editor) {
            editor.value = frm.doc.content || "";
        }
    },

});
