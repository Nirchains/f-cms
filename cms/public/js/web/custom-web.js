frappe.provide("cms.utils");

$.extend(cms.utils, {
    getUrlParameter: function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
    },

    isElementInView: function (element, fullyInView) {

        if ( !($(element).length )) {
            return false;
        }
      
        var pageTop = $(window).scrollTop();
        var pageBottom = pageTop + $(window).height();
        var elementTop = $(element).offset().top + 150;
        var elementBottom = elementTop + $(element).height() + 150;

        if (fullyInView === true) {
            return ((pageTop < elementTop) && (pageBottom > elementBottom));
        } else {
            return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
        }
    },

    infiniteScroll: function () {
        //show more on scroll
        $(window).scroll(function() {
            var isElementInView = cms.utils.isElementInView($(".btn-more"), false);

            if (isElementInView) {
                $('#portfolioLoadMoreLoader').addClass('portfolio-load-more-loader-showing').show();

                setTimeout( function () {
                    $(".btn-more").click();
                    $('#portfolioLoadMoreLoader').removeClass('portfolio-load-more-loader-showing').hide();
                    }, 500);

            } 
        });
    }
    
});


