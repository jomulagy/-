var img_url =[]
var clothe_id =[]

var page_num = 0
var total_page_num

$(document).ready(function(){
    if (clothe_id=='[]'){
        img_url = []
        clothe_id = []
    }
    else{
        image_urls = image_urls.split(",")
        for(var url of image_urls){
            img_url.push(url.substring(url.indexOf("&#x27;")+6,url.lastIndexOf("&#x27;")))
        }

        clothe_ids = clothe_ids.substring(1,clothe_ids.length-1)
        clothe_ids = clothe_ids.split(", ")

        for(var id of clothe_ids){
            clothe_id.push(id)
        }
    }

    print_clothes(page_num)
    print_pagenations()

    $('.page-item').click(function(){
        $("#card-area").empty();
    
        var request_page = $(this).text();
        if(request_page == 'Previous'){
            request_page=parseInt(page_num)-1
        }

        else if(request_page == 'Next'){
            request_page = parseInt(page_num)+1
        }

        $(".pagination>.page-item:first").removeClass("disabled");
        $(".pagination>.page-item:last").removeClass("disabled");
    
        if (request_page == 1) {
            $(".pagination>.page-item:first").addClass("disabled");
        }
        else if (request_page == total_page_num) {
            $(".pagination>.page-item:last").addClass("disabled");
        }
        $(".pagination>.page-item").eq(page_num).removeClass("active");
        $(".pagination>.page-item").eq(request_page).addClass("active");
        if (img_url.length != 0){
            print_clothes(request_page-1);
        }
        page_num = request_page;
    
    });

    $('.pagination>.page-item:nth-child(2)').trigger("click");
});

function print_pagenations(){  
    var target = $('.pagination>.page-item:first-child')
    if (img_url.length%20!=0){
        total_page_num = parseInt(img_url.length/20)+1
    }
    else{
        total_page_num = parseInt(img_url.length/20)
    }
    if(total_page_num==0){
        total_page_num = 1
    }
    for(var i = 0;i<total_page_num;i++){
        var page_item = document.createElement('li');
        $(page_item).addClass('page-item');
        $(target).after(page_item)
        target = $(page_item);

        var page_link = document.createElement('a');
        $(page_link).addClass('page-link');
        $(page_link).text(i+1);
        page_item.append(page_link);
    }
    
}
function print_clothes(page_num){
    var container = $("#card-area")
    var start = 20*page_num;
    var end = (img_url.length<20*(page_num+1)-1)?img_url.length:20*(page_num+1)-1
    
    for(var i = start; i<end;i++){
        if(i%4==0){
            var row = document.createElement('div');
            $(row).addClass('row row-cols-4')
            container.append(row)
        }
        var col = document.createElement('div');
        $(col).addClass('col')
        row.append(col)

        var card = document.createElement('div');
        $(card).addClass('card')
        col.append(card)
        
        var a = document.createElement('a');
        $(a).attr("href","/clothe/detail/"+clothe_id[i])
        card.append(a)

        var img = document.createElement('img');
        $(img).addClass('card-img-top');
        $(img).attr("src",img_url[i]);
        a.append(img);
    }
}

