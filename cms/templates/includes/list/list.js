frappe.ready(function() {
	var next_start = {{ next_start or 0 }};
	var previus_start = -1;
	var result_wrapper = $(".website-list .result");

	$(".website-list .btn-more").on("click", function() {
		if (previus_start != next_start){
			previus_start = next_start;
			var btn = $(this);
			btn.prop("disabled", true);
			var data = $.extend(frappe.utils.get_query_params(), {
				doctype: "{{ doctype }}",
				txt: "{{ txt or '' }}",
				tipo_de_documento: "{{tipo_de_documento_url}}",
				limit_start: next_start,
				pathname: location.pathname,
			});
			data.web_form_name = frappe.web_form_name;
			data.pathname = location.pathname;
			
			return $.ajax({
				url:"/api/method/frappe.www.list.get",
				data: data,
				statusCode: {
					200: function(data) {
						var data = data.message;
						next_start = data.next_start;
						$.each(data.result, function(i, d) {
							$(d).appendTo(result_wrapper);
						});
						toggle_more(data.show_more);
					}
				}
			}).always(function() {
				btn.prop("disabled", false);
			});
		}
	});
	var toggle_more = function(show) {
		if (!show) {
			//$(".website-list .more-block").addClass("hide");
			$(".website-list .more-block").remove();
		}
	};

	if($('.navbar-header .navbar-toggle:visible').length === 1)
	{
		$('.page-head h1').addClass('list-head').click(function(){
			window.history.back();
	 	});
	}
});
