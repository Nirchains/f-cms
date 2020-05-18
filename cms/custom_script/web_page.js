cur_frm.add_fetch("module_name", "title", "module_name_title");
//frappe.breadcrumbs.add("CMS");

//frappe.breadcrumbs.add("CMS", "Web Page");

frappe.ui.form.on("Web Page", {
	onload: function(frm) {
		frappe.breadcrumbs.add("CMS", "Web Page");
	},
});