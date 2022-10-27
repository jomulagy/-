$(document).ready(function(){
    $("#keyward").val(keyward);
    print_clothes();
    console.log($(".row-cols-4>.col"))
    $(".row-cols-4>.col").click(function(){
        location.href = "/clothe/detail/"+$(this).attr("id");
    })
    $(".row-cols-4>.col").hover(function(){
        $(this).css('cursor', 'pointer');
    })
    $(".bar>.col").hover(function(){
        $(this).css('cursor', 'pointer');
    })
});
function print_clothes(){
    var container = $("#card-area")
    var start = 0;
    var end = (clothes.length<20)?clothes.length:20
    
    for(var i = start; i<end;i++){
        if(i%4==0){
            var row = document.createElement('div');
            $(row).addClass('row row-cols-4')
            container.append(row)
        }
        var col = document.createElement('div');
        $(col).addClass('col')
        $(col).attr("id",clothes[i].id);

        row.append(col)

        var card = document.createElement('div');
        $(card).addClass('card');
        col.append(card)

        var img = document.createElement('img');
        $(img).addClass('card_img');
        $(img).attr("src",clothes[i].url);
        card.append(img);

        var card_body = document.createElement('div');
        $(card_body).addClass('card-body');
        card.append(card_body);

        var card_title = document.createElement('h5');
        $(card_title).addClass('card-title');
        $(card_title).text(clothes[i].name);
        card_body.append(card_title);
    }
}


$(".bar>.col").click(function(){
    
    $(".area").css("display",'none');
    if($(this).attr("id") == "s1"){
        $("#top_area").css("display","block");
    }
    else if($(this).attr("id") == "s2"){
        $("#bottom_area").css("display","block");
    }
    else if($(this).attr("id") == "s3"){
        $("#shoes_area").css("display","block");
    }
    else if($(this).attr("id") == "s4"){
        $("#accs_area").css("display","block");
    }
});

