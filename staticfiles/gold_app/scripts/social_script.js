$(document).ready(function(){
    $("#google_icon").on('click', function(){
        let google_href = $(".socialaccount_provider.google").attr("href");
        $(this).attr("href", google_href);
    });

    $("#twitter_icon").on('click', function(){
        let twitter_href = $(".socialaccount_provider.twitter").attr("href");
        $(this).attr("href", twitter_href);
    });

    var window_width = $(this).width()
    if (window_width < 576){
        $("#card_login").removeClass("shadow");
        $("#card_login").removeClass("p-3");
        $("#card_login").css("border", "none");
    }

    $(window).on('resize', function(){
        var screen_width = $(this).width();
        if (screen_width < 576){
            $("#card_login").removeClass("shadow");
            $("#card_login").removeClass("p-3");
            $("#card_login").css("border", "none");
            $("#card_login").removeClass("border");
        }else if (screen_width > 576){
            $("#card_login").addClass("shadow");
            $("#card_login").addClass("p-3");
            $("#card_login").addClass("border");
        }
    });

    
});