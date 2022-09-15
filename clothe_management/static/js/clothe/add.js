var keyList_category = Object.keys(dict_category)
var init_select_child

$(document).ready(function(){
    var select_parent = $('#select-parent');

    keyList_category.forEach(function(item) {
        var option_parent = document.createElement('option');
        $(option_parent).val(item);
        $(option_parent).text(item);

        select_parent.append(option_parent);
    });

});

$('#select-parent').change(function(){
    $('#select-child option:gt(0)').remove()
    
    var select_child = $('#select-child');
    var key = $(this).val()
    dict_category[key].forEach(function(item) {
        var option_child = document.createElement('option');
        $(option_child).val(item);
        $(option_child).text(item);

        select_child.append(option_child);
    });

});

$('#btn-img').click(function(){
    $('#form-img').trigger('click');
});

$(function() {
    $("#form-img").on('change', function(){
    readURL(this);
    });
});
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
        $('#input_img').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

