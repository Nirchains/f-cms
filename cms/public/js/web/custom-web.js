frappe.provide("cms.utils");

$.extend(cms.utils, {
    getUrlParameter: function (sParam) {
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

    insertURLParam: function(key, value)
    {
        key = encodeURI(key); value = encodeURI(value);

        var kvp = document.location.search.substr(1).split('&');

        var i=kvp.length; var x; while(i--) 
        {
            x = kvp[i].split('=');

            if (x[0]==key)
            {
                x[1] = value;
                kvp[i] = x.join('=');
                break;
            }
        }

        if(i<0) {kvp[kvp.length] = [key,value].join('=');}

        return kvp.join('&'); 
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


