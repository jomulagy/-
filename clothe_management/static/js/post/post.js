$("#btn-like").click(function(){
    $.ajax({
        //요청이 전송될 URL 주소
        url: '/increase_like/',
        type: "POST",
        dataType: "JSON",
        data: {
            'post_id': post_id,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        headers: { "X-CSRFToken": "{{ csrf_token }}" }
    });
    location.reload();
});