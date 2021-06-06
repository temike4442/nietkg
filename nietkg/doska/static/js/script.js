$(document).ready(function(){
   

$('#select_cat').on('change', function(){
    var selectid = $(this).find(':selected').val();
    if (selectid > 0)
    {
        $.ajax({
            type: "POST",
            url: "functions/get_cat.php",
            data: "cat_id="+selectid,
            success: function(msg){
                if (msg !== '')
                {
                    $("#sub_cat").fadeIn(500).css('display','block');
                    $("#sub_cat_2").fadeOut(500);
                    $("#select_cat_sub_2").empty();
                    $("#select_cat_sub").empty();
                    $("#select_cat_sub").append('<option selected value="0">--Выберите под категории--</option>');
                    $("#select_cat_sub").append(msg);
                    $("#select_cat_sub").trigger("chosen:updated");
                } else
                {
                    $("#sub_cat").fadeOut(500);
                    $("#select_cat_sub").empty();
                    $("#sub_cat_2").css('display','none');
                    $("#select_cat_sub_2").empty();
                }
           }
        });
    } else
    {
        $("#sub_cat").fadeOut(500);
        $("#select_cat_sub").empty();
        $("#sub_cat_2").css('display','none');
        $("#select_cat_sub_2").empty();
    }
  });

$('#select_cat_sub').on('change', function(){
    var select_sub_id = $(this).find(':selected').val();
    if (select_sub_id > 0)
    {
        $.ajax({
            type: "POST",
            url: "functions/get_sub_cat.php",
            data: "sub_cat_id="+select_sub_id,
            success: function(msg){
                if (msg !== '')
                {
                    $("#sub_cat_2").fadeIn(500).css('display','block');
                    $("#select_cat_sub_2").empty();
                    $("#select_cat_sub_2").append(msg);
                    $("#select_cat_sub_2").trigger("chosen:updated");
                } else
                {
                    $("#sub_cat_2").fadeOut(500);
                    $("#select_cat_sub_2").empty();
                }
           }
        });
    } else
    {
        $("#sub_cat_2").fadeOut(500);
        $("#select_cat_sub_2").empty();
    }   
  });

var count_input = 1;

    $('#add_input').click(function(){

        count_input++;

        $('<div class="col-lg-6" style="margin-top:10px;" id="add_img'+count_input+'"><input  type="hidden" name="MAX_FILE_SIZE" value="2000000"/><input style="border-bottom: 1px solid;padding-bottom: 5px;" type="file" name="gallery_img[]"/><br><a class="delete_input_img btn btn-danger btn-sm" style="color:white; margin-top:-55px; margin-left:400px;"  rel="'+count_input+'">Удалить</a></div>').fadeIn(600).appendTo('#object');
    });

$('#object').on('click','a',function(){
        var rel = $(this).attr("rel");
        $("#add_img"+rel).fadeOut(300,function(){
        $("#add_img"+rel).remove();
        });
    });

/*============== Validation ==================*/


$('#ad_submit').click(function(){

    var title = $('#ad_title').val();
    var body  = $('#ad_body').val();
    var cat   = $('#select_cat').val();
    var sub_cat = $('#select_cat_sub').val();
    var phone = $('#ad_phone').val();
    var image = $('#ad_image').val();

    if (title == ''){
        status_title = 'no';
        $('#ad_title').addClass('is-invalid');
    } else { status_title = 'ok'; $('#ad_title').removeClass('is-invalid').addClass('is-valid');}

    if (body == ''){
        status_body = 'no';
        $('#ad_body').addClass('is-invalid');
    } else { status_body = 'ok'; $('#ad_body').removeClass('is-invalid').addClass('is-valid');}

    if (cat == '0'){
        status_cat = 'no';
        $('#select_cat').addClass('is-invalid');
    } else { status_cat = 'ok'; $('#select_cat').removeClass('is-invalid').addClass('is-valid');}

    if (sub_cat == '0'){
        status_subcat = 'no';
        $('#select_cat_sub').addClass('is-invalid');
    } else { status_subcat = 'ok'; $('#select_cat_sub').removeClass('is-invalid').addClass('is-valid');}

    if (phone == ''){
        status_phone = 'no';
        $('#ad_phone').addClass('is-invalid');
    } else { status_phone = 'ok'; $('#ad_phone').removeClass('is-invalid').addClass('is-valid');}

    if (image == ''){
        status_image = 'no';
        $('#ad_image').addClass('is-invalid');
    } else { status_image = 'ok'; $('#ad_image').removeClass('is-invalid').addClass('is-valid');}


    if (status_title == 'ok' && status_body == 'ok' && status_cat == 'ok' && status_subcat == 'ok' && status_phone == 'ok' && status_image == 'ok')
    {
        var formData = new FormData(document.getElementById('add_form'));
        $('#add_form').fadeOut(200);
        $('#loading').removeClass('d-none');
        $.ajax({
            type: "POST",
            processData: false,
            contentType: false,
            url: "functions/addpost.php",
            data:  formData, 
            success: function(data){

            if (data =='ok')
            {
              $('#loading').fadeOut(300);
              $('#msg_success').removeClass('d-none');      
            } else
            {
              alert('Произошла ошибка');
            }
          }
        });       
    }

});


});  