module = {
	init: function(frm) {
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
	}
};