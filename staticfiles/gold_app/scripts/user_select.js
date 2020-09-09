$(document).ready(function(){

    $("#gold_mine a").click(function(e){
        e.preventDefault();
        e.stopImmediatePropagation();

        var data = $(this).data("box");
        var href = $(this).attr("href");
        $.ajax({
            type: 'GET',
            url: href,
            success: function(response){
                if (response.click >= 0){
                    $("#number_clicks").html(response.click);

                    if(response.click == 0)
                        $("#gold_mine a").removeAttr("href");
                }

                $("#golds").html(response.golds);
                $("#diamond").html(response.diamond);

                console.log(response.session);

                var gold = "Gold-" + data;
                var diamond = "Diamond-" + data;
                var bomb = "Bomb-" + data;
                var none = "None-" + data;
                var id = "#"+ data;

                if (response.session.indexOf(gold) > -1){
                    $("[data-box="+ data +"]").removeAttr("href");
                    $("img[id="+data+"]").attr("src", imgGold);
                }else if(response.session.indexOf(diamond) > -1){
                   
                    $("[data-box="+ data +"]").removeAttr("href");
                    $("img[id="+data+"]").attr("src", imgDiamond);
                }else if(response.session.indexOf(bomb) > -1){
                  
                    $("[data-box="+ data +"]").removeAttr("href");
                    $("img[id="+data+"]").attr("src", imgBomb);
                }else if(response.session.indexOf(none) > -1){
                    $("[data-box="+ data +"]").removeAttr("href");
                    $(id).remove();
                }

                var score = 0;
                if (response.diamond > 0){
                    score = response.golds * 2;
                }else{
                    score = response.golds;
                }

                $("#score").html(score);
            }
        });
    });
});