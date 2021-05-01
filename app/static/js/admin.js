$(function(){
    $('.edit_pricing').on('click', function (e) {
        e.preventDefault();
        let pricing_id = $(this).attr('id');

        $.ajax({
            url:'/edit_pricing_detail/',
            type:'POST',
            data: $('#form_have_product_'+pricing_id).serialize(),
            success:function(response){
                console.log(response);
                $('.edit_pricing').trigger("reset");
                openModal(response);
            },
            error:function(){
                console.log('something went wrong here');
            },
        });
    });
});

function openModal(pricing_data){
  $('#pricing_category').value(pricing_data.category);
  $('#pricing_waste_type').value(pricing_data.waste_type);
  $('#pricing_price').value(pricing_data.categoria_producto_id);
  $('#pricing_metrics').text(pricing_data.other_metrics);
//   $('#color_name').text(pricing_data.company.color);
//   $('#packaging').text(pricing_data.company.packaging);
//   $('.description1 > p:eq(0)').html(pricing_data.company.descripcion);
//   $('#product_target').text(pricing_data.usos);
//   $('#modal_img_1').attr('src', '/static/img/'+pricing_data.company.foto_1 );
//   $('#modal_img_2').attr('src', '/static/img/'+pricing_data.company.foto_2 );
  $('#editModal').modal('show');
};


<script>
  $(function(){
    $('.detail_pickup').on('click', function (e) {
        e.preventDefault();
        let pickup_id = $(this).attr('id');
        // alert(pricing_id);

        $.ajax({
            url:'/pickup_detail/',
            type:'POST',
            data: $('#form_have_product_'+pickup_id).serialize(),
            success:function(response){
                console.log(response);
                $('.detail_pickup').trigger("reset");
                openModal(response);
            },
            error:function(){
                console.log('something went wrong here');
            },
        });
    });
});

function openModal(pickup_data){
  $('#pickup_firstname').val(pickup_data.user.firstname);
  $('#pickup_lastname').val(pickup_data.user.lastname);
  $('#pickup_waste_type').val(pickup_data.waste_type);
  $('#pickup_phone').val(pickup_data.user.user_phone);
  $('#pickup_address').val(pickup_data.user.user_address);
  $('#pickup_weight').val(pickup_data.weight);
  $('#pickupDetailModal').modal('show');
};
</script>

$(function(){
    $('.booking').on('click', function (e) {
        e.preventDefault();
        let booking_id = $(this).attr('id');
        $('#scehdule_id').val(booking_id);
        $('#bookModal').modal('show');
    });
});

function openModal(booking_data){
  $('#pricing_id').val(pickup_data.pricing_id);
  $('#pricing_category').val(pickup_data.category);
  $('#pricing_waste_type').val(pickup_data.waste_type);
  $('#pricing_price').val(pickup_data.price);
  $('#pricing_metrics').val(pickup_data.other_metrics);
  $('#bookModal').modal('show');
};