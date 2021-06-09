// SIGN UP API
$(function(){
    $('#signup_submit').on('click', function (e) {
        e.preventDefault();
        let firstname = document.getElementById("firstname").value;
        let lastname = document.getElementById("lastname").value;
        let email = document.getElementById("email").value;
        let phonenumber = document.getElementById("phonenumber").value;
        let password = document.getElementById("password").value;
        let address = document.getElementById("address").value;
        let role = document.getElementById("role").value;
        let terms_conditions = document.getElementById("terms_conditions");
        let state = document.getElementById("state").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        if (terms_conditions.checked == false){
            console.log(terms_conditions.value)
            document.getElementById("spinner").style.display = "none";
            document.getElementById('server_message_error').classList.add("alert-danger");
            document.getElementById('server_message_error').innerHTML = "Sorry! you need to agree to the Terms and Conditions to proceed.";
            document.getElementById("server_message_error").style.display = "block";
            setTimeout(function(){ 
                document.getElementById("server_message_error").style.display = "none"; 
                
            }, 2000);
        }
        else{
            $.ajax({
                url:'/register_api',
                type:'POST',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    firstname: firstname,
                    lastname: lastname,
                    email: email,
                    phonenumber: phonenumber,
                    password: password,
                    address: address,
                    role: role,
                    state: state,
                },
                success:function(response){
                    document.getElementById("spinner").style.display = "none";
                    if(response.error == true){
                        document.getElementById('server_message_error').classList.add("alert-danger");
                        document.getElementById('server_message_error').innerHTML = response.message;
                        document.getElementById("server_message_error").style.display = "block";
                        setTimeout(function(){ 
                            document.getElementById("server_message_error").style.display = "none"; 
                            
                        }, 2000);
                        
                    }
                    else{
                        document.getElementById('server_message_success').classList.add("alert-primary");
                        document.getElementById('server_message_success').innerHTML = response.message;
                        document.getElementById("server_message_success").style.display = "block";
                        setTimeout(function(){ 
                            // document.getElementById("server_message_success").style.display = "none"; 
                            window.location.href = '/verify';
                        }, 1000);
                    }
                    console.log(response);
                },
                error:function(e){
                    console.log(e);
                    $("#spinner").hide();
                },
            });
        }
    });
});

// VERIFY API
$(function(){
    $('#verify_submit').on('click', function (e) {
        e.preventDefault();
        let code = document.getElementById("code").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        $.ajax({
            url:'/activate',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                code: code,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                if(response.error == true){
                    document.getElementById('server_message_error').classList.add("alert-danger");
                    document.getElementById('server_message_error').innerHTML = response.message;
                    document.getElementById("server_message_error").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_error").style.display = "none";    
                    }, 2000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    // document.getElementById("email").value= response.email;
                    document.getElementById("verify_form").reset()
                    setTimeout(function(){ 
                        // document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/login';
                    }, 2000);
                }
                console.log(response);
            },
            error:function(e){
                console.log(e);
                $("#spinner").hide();
            },
        });
        
        
    });
});

// RESEND CODE API
$(function(){
    $('#resend_submit').on('click', function (e) {
        e.preventDefault();
        let email = document.getElementById("email").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        $.ajax({
            url:'/resend_code',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                email: email,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                if(response.error == true){
                    document.getElementById('server_message_error').classList.add("alert-danger");
                    document.getElementById('server_message_error').innerHTML = response.message;
                    document.getElementById("server_message_error").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_error").style.display = "none"; 
                    }, 3000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    document.getElementById("verify_form").reset()
                    setTimeout(function(){ 
                        document.getElementById("server_message_success").style.display = "none"; 
                    }, 3000);
                }
                console.log(response);
            },
            error:function(e){
                $("#spinner").hide();
                console.log(e);
            },
        });
    });
});

// FORGOT- SEND RESED CODE CODE API
$(function(){
    $('#forgot_submit').on('click', function (e) {
        e.preventDefault();
        let email = document.getElementById("email").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        $.ajax({
            url:'/forgot_code',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                email: email,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                if(response.error == true){
                    document.getElementById('server_message_error').classList.add("alert-danger");
                    document.getElementById('server_message_error').innerHTML = response.message;
                    document.getElementById("server_message_error").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_error").style.display = "none"; 
                    }, 3000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    setTimeout(function(){ 
                        // document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/verify_password';
                    }, 1000);
                }
                console.log(response);
            },
            error:function(e){
                console.log(e);
            },
        });
        
        
    });
});

// VERIFY PASSOWRD CHANGE API
$(function(){
    $('#verify_password_submit').on('click', function (e) {
        e.preventDefault();
        let codeOne = document.getElementById("codeOne").value;
        let codeTwo = document.getElementById("codeTwo").value;
        let codeThree = document.getElementById("codeThree").value;
        let codeFour = document.getElementById("codeFour").value;
        let code = codeOne+""+codeTwo+""+codeThree+""+codeFour;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        $.ajax({
            url:'/activate',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                code: code,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                if(response.error == true){
                    document.getElementById('server_message_error').classList.add("alert-danger");
                    document.getElementById('server_message_error').innerHTML = response.message;
                    document.getElementById("server_message_error").style.display = "block";
                    // document.getElementById("email").value= response.email;
                    setTimeout(function(){ 
                        document.getElementById("server_message_error").style.display = "none"; 
                        
                    }, 2000);
                    
                }
                else{
                    document.getElementById("verify_form").reset()
                    window.location.href = '/reset_password';
                }
                console.log(response);
            },
            error:function(e){
                $("#spinner").hide();
                console.log(e);
            },
        });
        
        
    });
});

// CHANGE PASSWORD API
$(function(){
    $('#change_password_submit').on('click', function (e) {
        e.preventDefault();
        let password = document.getElementById("password").value;
        let confirm_password = document.getElementById("confirm_password").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
        $.ajax({
            url:'/change_password',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                password: password,
                confirm_password: confirm_password,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                if(response.error == true){
                    document.getElementById('server_message_error').classList.add("alert-danger");
                    document.getElementById('server_message_error').innerHTML = response.message;
                    document.getElementById("server_message_error").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_error").style.display = "none"; 
                    }, 3000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    setTimeout(function(){ 
                        // document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/login';
                    }, 3000);
                }
                console.log(response);
            },
            error:function(e){
                $("#spinner").hide();
                console.log(e);
            },
        });
        
        
    });
});
// ************
//edit bio REUEST API
$(function(){
    $('#bio_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let edit_address = document.getElementById("edit_address").value;
        let edit_state = document.getElementById("edit_state").value;
        let edit_phone = document.getElementById("edit_phone").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/edit_bio_ajax',
            type:'PUT',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                edit_phone: edit_phone,
                edit_address: edit_address,
                edit_state: edit_state
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("bio_message_success").style.display = "block";
                    document.getElementById("bio_message_success").classList.add("alert-primary");
                    document.getElementById('bio_message_success').innerHTML = response.message;
                    
                    setTimeout(function(){ 
                        // document.getElementById("bio_message_success").style.display = "none";
                        if (response.role == "artisan"){
                            window.location.href = '/account'; 
                        }
                        else{
                            window.location.href = '/client_account'; 
                        }
                        
                    }, 1000); 
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 2000);
                }
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
    });
});

// edit account REUEST API
$(function(){
    $('#edit_account_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let edit_name = document.getElementById("edit_name").value;
        let edit_bank = document.getElementById("edit_bank").value;
        let edit_number = document.getElementById("edit_number").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/edit_account_ajax',
            type:'PUT',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                edit_name: edit_name,
                edit_bank: edit_bank,
                edit_number: edit_number
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("bio_message_success").classList.add("alert-primary");
                    document.getElementById('bio_message_success').innerHTML = response.message;
                    document.getElementById("bio_message_success").style.display = "block";
                    setTimeout(function(){ 
                        // document.getElementById("bio_message_success").style.display = "none";
                        if (response.role == "artisan"){
                            window.location.href = '/account'; 
                        }
                        else{
                            window.location.href = '/client_account'; 
                        } 
                    }, 1000);
                    
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 2000);
                }
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
    });
});

//edit password REUEST API
$(function(){
    $('#password_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let old_password = document.getElementById("old_password").value;
        let new_password = document.getElementById("new_password").value;
        let confirm_new_password = document.getElementById("confirm_new_password").value;
       if (new_password != confirm_new_password){
            document.getElementById("spinner").style.display = "none";
            document.getElementById("bio_message_fail").classList.add("alert-danger");
            document.getElementById('bio_message_fail').innerHTML = "Sorry! New Password do not match";
            document.getElementById("bio_message_fail").style.display = "block";
            setTimeout(function(){ 
                document.getElementById("bio_message_fail").style.display = "none"; 
            }, 2000);
       }
       else{
            let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
            $.ajax({
                url:'/edit_password_ajax',
                type:'PUT',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    old_password: old_password,
                    new_password: new_password,
                },
                success:function(response){
                    // console.log(response);
                    document.getElementById("spinner").style.display = "none";
                    if(response.error == false){
                        document.getElementById("bio_message_success").classList.add("alert-primary");
                        document.getElementById('bio_message_success').innerHTML = response.message;
                        document.getElementById("bio_message_success").style.display = "block";
                        setTimeout(function(){ 
                            // document.getElementById("bio_message_success").style.display = "none"; 
                            if (response.role == "artisan"){
                                window.location.href = '/account'; 
                            }
                            else{
                                window.location.href = '/client_account'; 
                            } 
                        }, 1000);
                        
                    }
                    else{
                        document.getElementById("bio_message_fail").classList.add("alert-danger");
                        document.getElementById('bio_message_fail').innerHTML = response.message;
                        document.getElementById("bio_message_fail").style.display = "block";
                        setTimeout(function(){ 
                            document.getElementById("bio_message_fail").style.display = "none"; 
                        }, 2000);
                    }
                },
                error:function(e){
                    document.getElementById("spinner").style.display = "none";
                    console.log(e);
                },
            });
       }
        
    });
});

//new job order REUEST API
$(function(){
    $('#job_order_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let title = document.getElementById("title").value;
        let description = document.getElementById("description").value;
        let min_budget = document.getElementById("min_budget").value;
        let max_budget = document.getElementById("max_budget").value;
        let location = document.getElementById("location").value;
        let state = document.getElementById("state").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/new_order_ajax',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                title: title,
                description: description,
                state: state,
                location: location,
                min_budget: min_budget,
                max_budget: max_budget,
            },
            success:function(response){
                // console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("server_message").style.display = "block";  
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    console.log(response)
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 2000);
                }
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});

//new Ads REUEST API
$(function(){
    $('#new_ads_submit').on('click', function (e) {
        document.getElementById("spinner").style.display = "block";
        let title = document.getElementById("title").value;
        let description = document.getElementById("description").value;
        let min_budget = document.getElementById("min_budget").value;
        let max_budget = document.getElementById("max_budget").value;
        let location = document.getElementById("location").value;
        let state = document.getElementById("state").value;
        let pitch = document.getElementById("pitch").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/new_ads_ajax',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                title: title,
                description: description,
                state: state,
                location: location,
                min_budget: min_budget,
                pitch: pitch,
                max_budget: max_budget,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                // console.log(response);
                if(response.error == false){
                    document.getElementById("server_message").style.display = "block"; 
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    console.log(response)
                    button.innerHTML = "Submit";
                    button.disabled = false;
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 2000);
                }
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});


//GET ADS LIST FOR AD VIEW (ARTISAN) REUEST API

$.ajax({
    url:'/ads_list_ajax',
    type:'GET',
    success:function(response){
        // console.log(response);
        let adsList = response.adsList;
        if(adsList.length > 0){
            adsList.forEach((element) => {
                $('#ads_div').append(
                    '<div class="bid-card mt-3">'+
                        '<p style="font-size:1rem; line-height:35px;">'+element.title+'</p>'+
                        '<div style="text-align: center;">'+
                        '<i class="fas fa-eye" style="color: #ccc;" ></i>'+
                        '<p style="color:#005FD8;">'+element.views+' views</p>'+
                        '</div></div>'
                );
            });
        }
        if(response.error == true){
            $('#ads_div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
        }
        if(adsList.length <= 0){
            $('#ads_div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">You dont have any Ads yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

//GET ADS CLIENT HOMEREUEST API

// var getNewAdsForClients = window.setInterval(function(){
    $.ajax({
        url:'/client_home_ajax',
        type:'GET',
        success:function(response){
            // console.log(response);
            document.getElementById('client_screen').innerHTML = ""
            let adsList = response.adsList;
            if(adsList.length > 0){
                adsList.forEach((element) => {
                    $('#client_screen').append(
                        '<div class="job-card">'+
                        '<div class="job-inner">'+
                            '<p>'+element.state+'</p>'+
                            '<i class="fas fa-laptop fa-2x" style="color: #097685;"></i>'+
                            '<p>'+element.title+'</p>'+
                            '<p class="job-amount">&#8358;'+element.min_budget+' - &#8358;'+element.max_budget+'</p></div>'+
                        '<input type="button" value="Create Order" class="form-control job-button" id="'+element.ads_id+'" onClick="ads_view(this.id)"></div>'
                    );
                });
            }
            if(response.error == true){
                $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(adsList.length <= 0){
                $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Ads yet!</div>');
            }
        },
        error:function(e){
            // console.log(e);
        },
    });
// }, 500);

//GET ORDERS ARTISAN HOME REUEST API
// var getNewOrdersForArtisans = window.setInterval(function(){
    $.ajax({
        url:'/artisan_home_ajax',
        type:'GET',
        success:function(response){
            // console.log(response);
            document.getElementById('artisan_screen').innerHTML = ""
            let orderList = response.orderList;
            if(orderList.length > 0){
                orderList.forEach((element) => {
                    $('#artisan_screen').append(
                        '<div class="job-card">'+
                        '<div class="job-inner">'+
                            '<p>'+element.state+'</p>'+
                            '<i class="fas fa-laptop fa-2x" style="color: #267DED;"></i>'+
                            '<p>'+element.title+'</p>'+
                            '<p class="job-amount">&#8358;'+element.min_budget+' - &#8358;'+element.max_budget+'</p></div>'+
                        '<input type="button" value="Bid" class="form-control job-button" id="'+element.order_id+'" onClick="job_view(this.id)"></div>'
                    );
                });
            }
            if(response.error == true){
                $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(orderList.length <= 0){
                $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Orders yet!</div>');
            }
        },
        error:function(e){
            // console.log(e);
        },
    });
    
// }, 500);


// ARTISAN ORDER SEARCH API
function search_orders(e) {
    // console.log(e.value);
    document.getElementById('artisan_screen').innerHTML = "";
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/order_search',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            orders_search_query: e.value,
        },
        success:function(response){
            // console.log(response);
            let orderList = response.orderList;
            if(orderList.length > 0){
                orderList.forEach((element) => {
                    $('#artisan_screen').append(
                        '<div class="job-card">'+
                        '<div class="job-inner">'+
                            '<p>'+element.state+'</p>'+
                            '<i class="fas fa-laptop fa-2x" style="color: #267DED;"></i>'+
                            '<p>'+element.title+'</p>'+
                            '<p class="job-amount">&#8358;'+element.min_budget+' - &#8358;'+element.max_budget+'</p></div>'+
                        '<input type="button" value="Bid" class="form-control job-button" id="'+element.order_id+'" onClick="job_view(this.id)"></div>'
                    );
                });
            }
            if(response.error == true){
                $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(orderList.length <= 0){
                $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">'+response.message+'</div>');
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

// CLIENT ADS SEARCH API
function search_ads(e) {
    // console.log(e.value);
    document.getElementById('client_screen').innerHTML = "";
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/ads_search',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            ads_search_query: e.value,
        },
        success:function(response){
            // console.log(response);
            let adsList = response.adsList;
            if(adsList.length > 0){
                adsList.forEach((element) => {
                    $('#client_screen').append(
                        '<div class="job-card">'+
                        '<div class="job-inner">'+
                            '<p>'+element.state+'</p>'+
                            '<i class="fas fa-laptop fa-2x" style="color: #267DED;"></i>'+
                            '<p>'+element.title+'</p>'+
                            '<p class="job-amount">&#8358;'+element.min_budget+' - &#8358;'+element.max_budget+'</p></div>'+
                        '<input type="button" value="Create Order" class="form-control job-button" id="'+element.ads_id+'" onClick="ads_view(this.id)"></div>'
                    );
                });
            }
            if(response.error == true){
                $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(adsList.length <= 0){
                $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">'+response.message+'</div>');
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

// BID click and Job details view
function job_view(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/job_view',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            
            let jobView = response.jobView;
            if(response.error == false){
                console.log(response);
                document.getElementById('job_title').value = jobView.title;
                document.getElementById('job_description').value = jobView.description;
                // document.getElementById('job_duration').value = jobView.duration;
                document.getElementById('job_max_budget').value = jobView.max_budget;
                document.getElementById('job_location').value = jobView.location;
                document.getElementById('job_state').value = jobView.state;

                document.getElementById('job_id').value = jobView.job_id;
                $('#jobDetailsModal').modal('show');
            }
            if(response.error == true){
                console.log(response)
                document.getElementById(id).value = "Bidded";
                document.getElementById(id).disabled = true;
                document.getElementById(id).style.background = "#EFF2FD";
                document.getElementById(id).style.color = "black";
                document.getElementById(id).style.border = "1px solid #267DED00";
            }
            if(jobView.length <= 0){
                console.log(response)
            }

        },
        error:function(e){
            console.log(e);
        },
    });
}

// BID click and Job details view
function ads_view(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/ads_view',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            
            let adsView = response.adsView;
            if(adsView){
                console.log(response);
                document.getElementById('ads_title').value = adsView.title;
                document.getElementById('ads_description').value = adsView.description;
                document.getElementById('ads_max_budget').value = "NGN"+adsView.max_budget;
                document.getElementById('ads_min_budget').value = "NGN"+adsView.min_budget;
                document.getElementById('ads_location').value = adsView.location;
                document.getElementById('ads_state').value = adsView.state;

                document.getElementById('ads_id').value = adsView.ads_id;
                $('#createOrderModal').modal('show');
            }
            if(response.error == true){
                console.log(response)
            }
            if(adsView.length <= 0){
                console.log(response)
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

// Submit Order for a specific Artisan Ads by Client
$(function(){
    $('#client_orders_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let ads_title = document.getElementById("ads_title").value;
        let ads_description = document.getElementById("ads_description").value;
        let ads_min_budget = document.getElementById("ads_min_budget").value;
        let ads_max_budget = document.getElementById("ads_max_budget").value;
        let ads_location = document.getElementById("ads_location").value;
        let ads_state = document.getElementById("ads_state").value;
        let ads_pitch = document.getElementById("ads_pitch").value;
        let ads_fee = document.getElementById("ads_fee").value;
        let ads_id = document.getElementById("ads_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/submit_order_specific_artisan',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                ads_title: ads_title,
                ads_description: ads_description,
                ads_state: ads_state,
                ads_location: ads_location,
                ads_min_budget: ads_min_budget,
                ads_pitch: ads_pitch,
                ads_max_budget: ads_max_budget,
                ads_fee: ads_fee,
                ads_id: ads_id,
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("bio_message").classList.add("alert-primary");
                    document.getElementById("bio_message").innerHTML= response.message; 
                    document.getElementById("bio_message").style.display = "block";
                    setTimeout(function(){ 
                        // document.getElementById("bio_message").classList.remove("alert-primary");
                        // document.getElementById('bio_message').innerHTML = "";
                        window.location.href = '/client_home';
                    }, 1000);
                }
                else{
                    document.getElementById("bio_message").classList.add("alert-danger");
                    document.getElementById('bio_message').innerHTML = response.message;
                    document.getElementById("bio_message").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById('bio_message').innerHTML = "";
                        document.getElementById("bio_message").classList.remove("alert-danger");
                        document.getElementById("bio_message").style.display = "none";
                    }, 2000);
                }
                
            },
            error:function(e){
                console.log(e);
            },
        });
        
    });
});

$.ajax({
    url:'/client_project_ajax',
    type:'GET',
    success:function(response){
        console.log(response);

        let clientOrdersList = response.clientOrdersList;
        if(clientOrdersList.length > 0){
            clientOrdersList.forEach((element) => {
                if (element.orderStatus == "pending") {
                    $('#order-div').append(
                        '<div class="bid-card mt-3" onClick="awaiting_artisan(this.id)">'+
                            '<p style="width: 70%;">'+element.title+'</p>'+
                            '<i class="fas fa-dot-circle  " style="color: #D0BC0A;" ></i>'+
                            '</div>'
                    );
                }
                if (element.orderStatus == "accepted") {
                }
                if (element.orderStatus == "bidding") {
                    $('#order-div').append(
                        '<div class="bid-card mt-3" id="'+element.order_id+'" onClick="bid_list(this.id)">'+
                        '<p style="width: 70%;">'+element.title+'</p>'+
                          '<div class="text-center">'+
                            '<i class="fas fa-user-plus " style="color: #40DA86;" ></i>'+
                          '<p style="font-size: 0.5rem; color:#0069F0;">'+element.noOfBidders+' bidders</p>'+
                          '</div>'+
                      '</div>'
                    );
                }
                if (element.orderStatus == "declined") {
                    $('#order-div').append(
                        '<div class="bid-card mt-3">'+
                        '<p style="width: 70%;">'+element.title+'</p>'+
                        '<i class="fas fa-times-circle  " style="color: #C91B30;" ></i>'+
                      '</div>'
                    );
                }
                
            });
        }
        if(response.error == true){
            $('#order-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
        }
        if(clientOrdersList.length <= 0){
            $('#order-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Orders yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

  

$(function(){
    $('#bidder_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let job_pitch = document.getElementById("job_pitch").value;
        let job_fee = document.getElementById("bidding_fee").value;
        let job_id = document.getElementById("job_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/submit_bid',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                job_pitch: job_pitch,
                job_fee: job_fee,
                job_id: job_id,
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("bio_message").classList.add("alert-primary");
                    document.getElementById("bio_message").innerHTML= response.message; 
                    document.getElementById("bio_message").style.display = "block";
                    setTimeout(function(){ 
                        // document.getElementById("bio_message").classList.remove("alert-primary");
                        // document.getElementById('bio_message').innerHTML = "";
                        window.location.href = '/artisan_home';
                    }, 1000);
                }
                else{
                    document.getElementById("bio_message").classList.add("alert-danger");
                    document.getElementById('bio_message').innerHTML = response.message;
                    document.getElementById("bio_message").style.display = "block";
                    
                }
                
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});

$.ajax({
    url:'/artisan_gig_ajax',
    type:'GET',
    success:function(response){
        console.log(response);
        let artisanBidsList = response.artisanBidsList;
        if(artisanBidsList.length > 0){
            artisanBidsList.forEach((element) => {
                if (element.orderStatus == "pending" && element.fromAds == false ) {  // awaiting artisan's acceptance
                    $('#bidder-div').append(
                        '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="pending_order(this.id)">'+ 
                            '<p style="width: 70%;">'+element.title+'</p>'+
                            '<i class="fas fa-dot-circle  " style="color: #D0BC0A;" ></i>'+
                            '</div>'
                    );
                }
                if (element.orderStatus == "pending" && element.fromAds == true) {  // awaiting artisan's acceptance
                    $('#bidder-div').append(
                        '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="pending_order(this.id)">'+ 
                            '<p style="width: 70%;">'+element.title+'</p>'+
                            '<i class="fas fa-dot-circle  " style="color: #D0BC0A;" ></i>'+
                            '</div>'
                    );
                }
                if (element.orderStatus == "bidding" && element.winner_id =="" || element.winner_id == null) {  // oder still accepting bids
                    $('#bidder-div').append(
                        '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="bidding_ongoing(this.id)">'+ 
                        '<p style="width: 70%;">'+element.title+'</p>'+
                          '<div class="text-center">'+
                            '<i class="fas fa-user-plus " style="color: #40DA86;" ></i>'+
                          '<p style="font-size: 0.5rem; color:#0069F0;"> You and '+parseInt(element.noOfBidders - 1)+' bidder(s)</p>'+
                          '</div>'+
                      '</div>'
                    );
                }
                else {
                    // $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are new Orders yet. However check the Gig section </div>');
                }
                
            });
        }
        if(response.error == true){
            $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
        }
        if(artisanBidsList.length <= 0){
            $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Bids for you yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

// Artisan bid page - pending order details to accept or delcine order
function pending_order(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/pending_order_modal',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            console.log(response)
            // console.log('hi')
            let bidView = response.bidView;
            if(bidView){
                console.log(response);
                document.getElementById('bid_title').value = bidView.title;
                document.getElementById('bid_description').value = bidView.description;
                document.getElementById('bid_budget').value = bidView.budget;
                // document.getElementById('bid_duration').value = bidView.duration
                document.getElementById('bid_location').value = bidView.location;
                document.getElementById('bid_state').value = bidView.state;
                document.getElementById('bid_fee').value = "NGN "+bidView.service_fee;
                document.getElementById('bid_id2').value = bidView.order_id;
                $('#pendingOrder').modal('show');
            }
            if(response.error == true){
                console.log(response)
            }
            if(bidView.length <= 0){
                console.log(response)
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

function bidding_ongoing(id) {
    console.log(id);
    document.getElementById('bid_bid').value = id;
    $('#bidderModal').modal('show');
}
// Client orderpage - pending order awaiting artisan
function awaiting_artisan(id) {
    console.log(id);
    document.getElementById('order_order').value = id;
    $('#waitModal').modal('show');
}
// Client Order Bidders list
function bid_list(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/bid_list',
        type:'post',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            let bidList = response.bidList;
            console.log(response);
            document.getElementById('bidder_title2').value = response.title;
            if(bidList.length > 0){
                bidList.forEach((element) => {
                    if (!element.decline_offer){
                        $('#bidders_form').append(
                            '<form><div class="bidder-div mb-2">'+
                                '<div class="bidder-top">'+
                                '<div class="bidder-inner">'+
                                    '<i class="fas fa-user-circle fa-alter" style="color: #005FD850;"  ></i>'+
                                    '<div class="ml-2 mt-1">'+
                                    '<p style="color:#829CC580; font-weight:700; font-size:0.9rem;" id="bidder_bidder_name'+element.bidder_id+'">'+element.bidder+'</p> <input id="bidder_bid_id'+element.bidder_id+'" value="'+element.bidder_id+'" hidden/>'+
                                    '<p style="color:#005FD8;">'+element.state+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="mt-1">'+
                                    '<p style="color:#005FD8; font-size:0.9rem;">&#8358;' +element.service_fee+'</p>'+
                                    '<p>Ratings: '+element.ratings+'</p>'+
                                '</div>'+
                                '</div>'+
                                '<div class="bidder-bottom mt-2"> <input id="bid_id'+element.bid_id+'" value="'+element.bid_id+'" hidden/>'+
                                '<p style="color:#005FD880; font-weight:700; font-size:0.7rem;">Bid Pitch</p>'+
                                '<p style="color:#829CC580;">'+element.pitch+'</p>'+
                                '</div>'+
                                '<p class="'+element.bidder_id+'" id="'+element.bid_id+'" onClick="client_accept_bidder_confirmation(this.id, this.className)" style="text-align:right; color:#F7B222;">Accept Bid</p>'+
                                // '<button type="button" class="bidder-accept text-right" >Accept Bid</button>'+
                            '</div></form>'
                            
                        );
                    }
                    else{
                        $('#bidders_form').append(
                            '<div class="bidder-div mb-2">'+
                                '<div class="bidder-top">'+
                                '<div class="bidder-inner">'+
                                    '<i class="fas fa-user-circle fa-alter" style="color: #005FD850;"  ></i>'+
                                    '<div class="ml-2 mt-1">'+
                                    '<p style="color:#829CC580; font-weight:700; font-size:0.9rem;" id="bidder_bidder_name'+element.bidder_id+'">'+element.bidder+'</p> <input id="bidder_bid_id'+element.bidder_id+'" value="'+element.bidder_id+'" hidden/>'+
                                    '<p style="color:#005FD8;">'+element.state+'</p>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="mt-1">'+
                                    '<p style="color:#005FD8; font-size:0.9rem;">&#8358;' +element.service_fee+'</p>'+
                                    '<p>Ratings: '+element.ratings+'</p>'+
                                '</div>'+
                                '</div>'+
                                '<div class="bidder-bottom mt-2"> <input id="bid_id'+element.bidder_id+'" value="'+element.bid_id+'" hidden/>'+
                                '<p style="color:#005FD880; font-weight:700; font-size:0.7rem;">Bid Pitch</p>'+
                                '<p style="color:#829CC580;">'+element.pitch+'</p>'+
                                '</div>'+
                                '<p class="bidder-accept text-right" style="color:red;" type="button" id="'+element.bidder_id+'" >Declined</p>'+
                            '</div>'
                            
                        );
                    }
                    
                });
            }
            if(bidList.length = 0){
                $('#bidders_forms').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Bids yet for your Offer!</div>');
            }
            if(response.error == true){
                $('#bidders_form').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            
            $('#biddersList').modal('show');
        },
        error:function(e){
            console.log(e);
        },
    });
}
function back2project() {
    window.location.href = '/project';
}

// artisan accept offer API
$(function(){
    $('#job_accept_submit_initial').on('click', function (e) {
        e.preventDefault();
        let bid_id2 = document.getElementById("bid_id2").value;
        document.getElementById("accept_order_id").value= bid_id2;
        $('#acceptModal').modal('show');
        
    });
});

// $(function(){
//     $('.bidder-accept').on('click', function (e) {
//         e.preventDefault();
//         console.log('hi')
        
//     });
// });


function client_accept_bidder_confirmation(bidd_id, bidder_id) {
    let bid_id = document.getElementById("bid_id"+bidd_id).value;
    let bidder = document.getElementById("bidder_bidder_name"+bidder_id).innerHTML;
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/client_accept_bidder_confirmation',
        type:'POST',
        headers:{"X-CSRFToken": $crf_token},
        data:{
            bid_id: bid_id,
            bidder_id: bidder_id,
            bidder: bidder, 
        },
        success:function(response){
            console.log(response);
            if(response.error == false){
                document.getElementById('client_accept_order_id').value = response.bidder.bid_id;
                document.getElementById('client_bidder_id').value = response.bidder.bidder_id;
                document.getElementById('client_bidder_name').innerHTML = response.bidder.bidder;
                $('#acceptClientModal').modal('show');
                
            }
            else{
                console.log(response.message)
                
            }
        },
        error:function(e){
            console.log(e);
        },
    });
    
}

// artisan decline offer API
$(function(){
    $('#job_decline_submit_initial').on('click', function (e) {
        e.preventDefault();
        let bid_id2 = document.getElementById("bid_id2").value;
        document.getElementById("decline_order_id").value= bid_id2;
        $('#declineModal').modal('show');
        
    });
});

$(function(){
    $('#accept_order_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let job_order_id = document.getElementById("accept_order_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/artisan_accept_bid_api',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                job_id: job_order_id,
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("cover").style.display = "none";
                    document.getElementById("accept_message").classList.add("text-primary");
                    document.getElementById("accept_message").innerHTML= response.message; 
                    document.getElementById("accept_message").style.display = "block";
                    
                }
                else{
                    document.getElementById("cover").style.display = "none";
                    document.getElementById("accept_message").classList.add("text-danger");
                    document.getElementById('accept_message').innerHTML = response.message;
                    document.getElementById("accept_message").style.display = "block";
                    
                }
                setTimeout(function(){ 
                    // document.getElementById("accept_message").classList.remove("text-primary");
                    // document.getElementById("accept_message").classList.remove("text-danger");
                    // document.getElementById('accept_message').innerHTML = "";
                    window.location.href = '/gig';
                    // document.getElementById("accept_message").style.display = "none";
                }, 1000);
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});
$(function(){
    $('#order_decline_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let job_order_id = document.getElementById("decline_order_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/artisan_decline_bid_api',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                job_id: job_order_id,
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("decline_message").classList.add("alert-primary");
                    document.getElementById("decline_message").innerHTML= response.message; 
                    document.getElementById("decline_message").style.display = "block";
                    
                }
                else{
                    document.getElementById("decline_message").classList.add("alert-danger");
                    document.getElementById('decline_message').innerHTML = response.message;
                    document.getElementById("decline_message").style.display = "block";
                    
                }
                setTimeout(function(){ 
                    // document.getElementById("decline_message").classList.remove("alert-primary");
                    // document.getElementById('decline_message').innerHTML = "";
                    // document.getElementById("decline_message").classList.remove("alert-danger");
                    window.location.href = '/gig';
                    // document.getElementById("decline_message").style.display = "none";
                }, 1000);
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});

$(function(){
    $('#confirm_acceptance_submit').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        let client_bidder_name = document.getElementById("client_bidder_name").innerHTML;
        let client_accept_order_id = document.getElementById("client_accept_order_id").value;
        let client_bidder_id = document.getElementById("client_bidder_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/client_accept_bid_api',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                bidder_name: client_bidder_name,
                order_id: client_accept_order_id,
                bidder_id: client_bidder_id,
            },
            success:function(response){
                console.log(response);
                document.getElementById("spinner").style.display = "none";
                if(response.error == false){
                    document.getElementById("cover").style.display = "none";
                    document.getElementById("accept_message").classList.add("text-primary");
                    document.getElementById("accept_message").innerHTML= response.message; 
                    document.getElementById("accept_message").style.display = "block";
                    
                }
                else{
                    document.getElementById("cover").style.display = "none";
                    document.getElementById("accept_message").classList.add("text-danger");
                    document.getElementById('accept_message').innerHTML = response.message;
                    document.getElementById("accept_message").style.display = "block";
                    
                }
                setTimeout(function(){ 
                    // document.getElementById('accept_message').innerHTML = "";
                    window.location.href = '/project';
                    // document.getElementById("accept_message").style.display = "none";
                }, 1000);
            },
            error:function(e){
                document.getElementById("spinner").style.display = "none";
                console.log(e);
            },
        });
        
    });
});


$.ajax({
    url:'/artisan_gig_main_ajax',
    type:'GET',
    success:function(response){
        console.log(response);
        let artisanGigsList = response.artisanGigsList;
        if(artisanGigsList.length > 0){
            artisanGigsList.forEach((element) => {
                if (element.projectStatus == "ongoing" && element.isCompleted == false) {  // ongoing project after artisan accept offer
                    $('#gigger-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'" onClick="ongoing_gig(this.id)">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-envelope " style="color: #0069F0;" ></i>'+
                            '<i class="fas fa-dot-circle " style="color: #D0BC0A;" ></i>'+
                        '</div>'
                    );
                }
                if (element.projectStatus == "completed") {  // order completed
                    $('#gigger-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-check-circle  " style="color: #14E2CA;" ></i>'+
                        '</div>'
                    );
                }

                if (element.projectStatus == "disputed") {  // order disputed
                    $('#gigger-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-question-circle  " style="color: #C4C4C4;" ></i>'+
                        '</div>'
                    );
                }
                if (element.projectStatus == "cancelled") {  // order cancelled
                    $('#gigger-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-times-circle  " style="color: #C91B30;" ></i>'+
                        '</div>'
                    );
                }
                if (element.projectStatus == "ongoing" && element.isCompleted == true) {  // order completed by artisan awaiting client confirmation
                    $('#gigger-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'" data-toggle="modal" data-target="#artisanWaitModal">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-dot-circle " style="color: #14E2CA;" ></i>'+
                        '</div>'
                    );
                }
                
            });
        }
        if(response.error == true){
            $('#gigger-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
        }
        if(artisanGigsList.length <= 0){
            $('#gigger-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Gigs for you yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

$.ajax({
    url:'/client_project_main_ajax',
    type:'GET',
    success:function(response){
        console.log(response);
        let clientProjectsList = response.clientProjectsList;
        if(clientProjectsList.length > 0){
            clientProjectsList.forEach((element) => {
                if (element.projectStatus == "ongoing" ) {  // ongoing project after artisan accept offer
                    $('#project-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'" onClick="ongoing_project(this.id)">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-envelope " style="color: #0069F0;" ></i>'+
                            '<i class="fas fa-dot-circle " style="color: #D0BC0A;" ></i>'+
                        '</div>'
                    );
                }
                if (element.projectStatus == "completed") {  // order completed
                    $('#project-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-check-circle  " style="color: #14E2CA;" ></i>'+
                        '</div>'
                    );
                }

                if (element.projectStatus == "disputed") {  // order completed
                    $('#project-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-question-circle  " style="color: #C4C4C4;" ></i>'+
                        '</div>'
                    );
                }
                if (element.projectStatus == "cancelled") {  // order completed
                    $('#project-div').append(
                        '<div class="bid-card mt-3" id="'+element.project_id+'">'+
                            '<p>'+element.title+'</p>'+
                            '<i class="fas fa-times-circle  " style="color: #C91B30;" ></i>'+
                        '</div>'
                    );
                }
                
            });
        }
        if(response.error == true){
            $('#project-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
        }
        if(clientProjectsList.length <= 0){
            $('#project-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Projects yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

// Client click to end project or check project status
function ongoing_project(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/ongoing_project_modal',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            console.log(response)
            // console.log('hi')
            let projectItem= response.projectItem;
            if(projectItem){
                console.log(response);
                document.getElementById('project_title').value = projectItem.title;
                document.getElementById('project_description').value = projectItem.description;
                // document.getElementById('bid_budget').value = bidView.budget;
                document.getElementById('project_order_id2').value = projectItem.order_id
                document.getElementById('project_location').value = projectItem.location;
                document.getElementById('project_state').value = projectItem.state;
                document.getElementById('project_fee').value = "NGN"+projectItem.service_fee;
                document.getElementById('project_id2').value = projectItem.project_id;
                $('#ongoingProject').modal('show');
            }
            if(response.error == true){
                console.log(response)
            }
            if(projectItem.length <= 0){
                console.log(response)
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

// Client click to end project or check project status
function ongoing_gig(id) {
    let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url:'/ongoing_project_modal',
        type:'POST',
        headers:{
            "X-CSRFToken": $crf_token,
        },
        data:{
            id: id,
        },
        success:function(response){
            console.log(response)
            // console.log('hi')
            let projectItem= response.projectItem;
            if(projectItem){
                console.log(response);
                document.getElementById('gigs_title').value = projectItem.title;
                document.getElementById('gigs_description').value = projectItem.description;
                // document.getElementById('bid_budget').value = bidView.budget;
                document.getElementById('gigs_order_id2').value = projectItem.order_id
                document.getElementById('gigs_location').value = projectItem.location;
                document.getElementById('gigs_state').value = projectItem.state;
                document.getElementById('gigs_fee').value = "NGN"+projectItem.service_fee;
                document.getElementById('gigs_id2').value = projectItem.project_id;
                $('#ongoingGig').modal('show');
            }
            if(response.error == true){
                console.log(response)
            }
            if(projectItem.length <= 0){
                console.log(response)
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}

// artisan complete job initial  API
$(function(){
    $('#job_complete_submit_initial').on('click', function (e) {
        e.preventDefault();
        
        let gigs_id = document.getElementById("gigs_id2").value;
        let gigs_order_id = document.getElementById("gigs_order_id2").value;
        document.getElementById("gig_gigs_id").value= gigs_id;
        document.getElementById("gig_order_id").value= gigs_order_id;
        $('#endGigModal').modal('show');
        
    });
});

// client confirm complete job initial  API
$(function(){
    $('#project_submit_initial').on('click', function (e) {
        e.preventDefault();
        
        let projects_id = document.getElementById("project_id2").value;
        let project_order_id = document.getElementById("project_order_id2").value;
        document.getElementById("project_projects_id").value= projects_id ;
        document.getElementById("project_order_id").value= project_order_id;
        $('#endProjectModal').modal('show');
        
    });
});

function onlyOneCheckbox(checkbox) {
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}
$(function(){
     
// star rating
$('#star_one').on('click', function (e) {
    e.preventDefault();
    console.log("star_one");
    document.getElementById("star_one").style.color = "orange";
    document.getElementById("rating").value =1;

    // make them unclicable 
    document.getElementById("star_one").style.pointerEvents = "none";
    document.getElementById("star_two").style.pointerEvents = "none";
    document.getElementById("star_three").style.pointerEvents = "none";
    document.getElementById("star_four").style.pointerEvents = "none";
    document.getElementById("star_five").style.pointerEvents = "none";
});
$('#star_two').on('click', function (e) {
    e.preventDefault();
    console.log("star_two");
    document.getElementById("star_one").style.color = "orange";
    document.getElementById("star_two").style.color = "orange";
    document.getElementById("rating").value =2;

    // make them unclicable 
    document.getElementById("star_one").style.pointerEvents = "none";
    document.getElementById("star_two").style.pointerEvents = "none";
    document.getElementById("star_three").style.pointerEvents = "none";
    document.getElementById("star_four").style.pointerEvents = "none";
    document.getElementById("star_five").style.pointerEvents = "none";
});
$('#star_three').on('click', function (e) {
    e.preventDefault();
    console.log("star_three");
    document.getElementById("star_one").style.color = "orange";
    document.getElementById("star_two").style.color = "orange";
    document.getElementById("star_three").style.color = "orange";
    document.getElementById("rating").value =3;

    // make them unclicable 
    document.getElementById("star_one").style.pointerEvents = "none";
    document.getElementById("star_two").style.pointerEvents = "none";
    document.getElementById("star_three").style.pointerEvents = "none";
    document.getElementById("star_four").style.pointerEvents = "none";
    document.getElementById("star_five").style.pointerEvents = "none";
});
$('#star_four').on('click', function (e) {
    e.preventDefault();
    console.log("star_four");
    document.getElementById("star_one").style.color = "orange";
    document.getElementById("star_two").style.color = "orange";
    document.getElementById("star_three").style.color = "orange";
    document.getElementById("star_four").style.color = "orange";
    document.getElementById("rating").value =4;

    // make them unclicable 
    document.getElementById("star_one").style.pointerEvents = "none";
    document.getElementById("star_two").style.pointerEvents = "none";
    document.getElementById("star_three").style.pointerEvents = "none";
    document.getElementById("star_four").style.pointerEvents = "none";
    document.getElementById("star_five").style.pointerEvents = "none";
});
$('#star_five').on('click', function (e) {
    e.preventDefault();
    console.log("star_five");
    document.getElementById("star_one").style.color = "orange";
    document.getElementById("star_two").style.color = "orange";
    document.getElementById("star_three").style.color = "orange";
    document.getElementById("star_four").style.color = "orange";
    document.getElementById("star_five").style.color = "orange";
    document.getElementById("rating").value =5;

    // make them unclicable 
    document.getElementById("star_one").style.pointerEvents = "none";
    document.getElementById("star_two").style.pointerEvents = "none";
    document.getElementById("star_three").style.pointerEvents = "none";
    document.getElementById("star_four").style.pointerEvents = "none";
    document.getElementById("star_five").style.pointerEvents = "none";
});
});
$(function(){
    $('#end_project_submitting').on('click', function (e) {
        e.preventDefault();
        const button = document.getElementById("end_project_submitting");
        button.innerHTML = "ending Project...";
        button.disabled = true;
        // $('#endProjectModal').modal('hide');
        let project_id = document.getElementById("project_projects_id").value;
        let order_id = document.getElementById("project_order_id").value;
        let project_rating  = document.getElementById("rating").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        checked = $("input[type=checkbox]:checked").length;
        
        let project_status = $("input[type=checkbox]:checked").attr('value');
        console.log(project_rating);
        console.log(project_status);
        if(!checked) {
            let checkbox_error = document.getElementById("checkbox_error")
            checkbox_error.innerHTML = "You must check at least one checkbox."
            button.innerHTML = "End Project";
            button.disabled = false; 
        }
        else if (project_rating == ""){
            let rating_error = document.getElementById("rating_error")
            rating_error.innerHTML = "Sorry! you are yet to rate the Artisan!"
            checkbox_error.innerHTML = ""
            button.innerText = "End Project";
            button.disabled = false; 
        }

        else{
            $.ajax({
                url:'/end_project_api',
                type:'POST',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    project_id: project_id,
                    order_id: order_id,
                    project_status: project_status,
                    project_rating: project_rating 
                },
                success:function(response){
                    console.log(response);
                    if(response.error == false && response.satisfied == true){
                        document.getElementById("initial").style.display = "none";
                        document.getElementById("final").style.display = "block";
                        
                    }
                    if(response.error == false && response.satisfied == false){
                        document.getElementById("final_error").style.display = "block";
                        document.getElementById("initial").style.display = "none";
                        document.getElementById('final_error_message').innerHTML = response.message;
                        
                    }
                    setTimeout(function(){ 
                        window.location.href = '/project';
                    }, 1000);
                },
                error:function(e){
                    console.log(e);
                },
            });
        }
        
        
    });
});

$(function(){
    $('#end_gig_submitting').on('click', function (e) {
        e.preventDefault();
        const button = document.getElementById("end_gig_submitting");
        button.innerHTML = "ending Gig...";
        button.disabled = true;
        // $('#endProjectModal').modal('hide');
        let gig_id = document.getElementById("gig_gigs_id").value;
        let order_id = document.getElementById("gig_order_id").value;
        // let project_rating  = document.getElementById("rating").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        checked = $("input[type=checkbox]:checked").length;
        
        let is_completed = $("input[type=checkbox]:checked").attr('value');
        console.log(is_completed);
        if(!checked) {
            let checkbox_error = document.getElementById("checkbox_error2")
            checkbox_error.innerHTML = "You must check at least one checkbox."
            button.innerHTML = "End Gig";
            button.disabled = false;
        }
        else{
            $.ajax({
                url:'/end_gig_api',
                type:'POST',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    gig_id: gig_id,
                    order_id: order_id,
                    is_completed: is_completed,
                },
                success:function(response){
                    console.log(response);
                    if(response.error == false && response.satisfied == true){
                        document.getElementById("initial_gig").style.display = "none";
                        document.getElementById("final_gig").style.display = "block";
                        
                    }
                    if(response.error == false && response.satisfied == false){
                        document.getElementById("final_error_gig").style.display = "block";
                        document.getElementById("initial_gig").style.display = "none";
                        document.getElementById('final_error_message_gig').innerHTML = response.message;
                        
                    }
                    setTimeout(function(){ 
                        window.location.href = '/gig';
                    }, 1000);
                },
                error:function(e){
                    console.log(e); 
                },
            });
        }
        
        
    });
});





$(function(){
    $('#send_chat_message_submit').on('click', function (e) {
        e.preventDefault();
        let project_id = document.getElementById("project_id").value;
        let message = document.getElementById("message").value;
        let sender = document.getElementById("sender").value;
        let reciever = document.getElementById("reciever").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

        if (message == ""){}
        else{
            $.ajax({
                url:'/artisan_send_message',
                type:'POST',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    project_id: project_id,
                    message: message,
                    sender: sender,
                    reciever:reciever,
                },
                success:function(response){
                    console.log(response);
                    document.getElementById("message").value = "";
                    let chat_div = document.getElementById("chat_container").innerHTML = "";
                    
                    let chatHistoryList = response.chatHistoryList;
                    if(chatHistoryList.length > 0){
                        chatHistoryList.forEach((element) => {
                            if (element.from_id == element.artisan ) {  // ongoing project after artisan accept offer
                                $('#chat_container').append(
                                    '<div class="mt-3">'+
                                    '<p class="text-left">You</p>'+
                                    '<div  class="you-chat">'+
                                        '<p>'+element.message+'</p>'+
                                        '<p class="text-right">'+element.date_added+'</p>'+
                                    '</div>'+
                                    '</div>'
                                );
                            }
                            else {  // order completed
                                $('#chat_container').append(
                                    '<div class="mt-3">'+
                                    '<p class="text-right">Client</p>'+
                                    '<div  class="client-chat">'+
                                        '<p>'+element.message+'</p>'+
                                        '<p class="text-right">'+element.date_added+'</p>'+
                                    '</div>'+
                                    '</div>'
                                );
                            }
    
                            
                        });
                    }
                    if(response.error == true){
                        $('#chat_container').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
                    }
                    if(chatHistoryList.length <= 0){
                        $('#chat_container').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no chats yet!</div>');
                    }
                    // chat_div.scrollTop = "100vh";
                    let Height = document.getElementById("chat_container").scrollHeight;
                    document.getElementById("chat_container").scrollTop = Height;
                    console.log(Height)
                },
                error:function(e){
                    console.log(e);
                },
            });
            
        }
        
    });
});

$(function(){
    $('#client_send_chat_message_submit').on('click', function (e) {
        e.preventDefault();
        let project_id = document.getElementById("client_project_id").value;
        let message = document.getElementById("client_message").value;
        let reciever = document.getElementById("client_reciever").value;
        let sender = document.getElementById("client_sender").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

        $.ajax({
            url:'/client_send_message',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                project_id: project_id,
                message: message,
                sender: sender,
                reciever:reciever,
            },
            success:function(response){
                document.getElementById("client_message").value = "";
                console.log(response);
                document.getElementById("client_chat_container").innerHTML = "";
                
                let chatHistoryList = response.chatHistoryList;
                if(chatHistoryList.length > 0){
                    chatHistoryList.forEach((element) => {
                        if (element.from_id == element.client ) {  // ongoing project after artisan accept offer
                            $('#client_chat_container').append(
                                '<div class="mt-3">'+
                                '<p class="text-left">You</p>'+
                                '<div  class="you-chat">'+
                                    '<p>'+element.message+'</p>'+
                                    '<p class="text-right">'+element.date_added+'</p>'+
                                '</div>'+
                                '</div>'
                            );
                        }
                        else {  // order completed
                            $('#client_chat_container').append(
                                '<div class="mt-3">'+
                                '<p class="text-right">Client</p>'+
                                '<div  class="client-chat">'+
                                    '<p>'+element.message+'</p>'+
                                    '<p class="text-right">'+element.date_added+'</p>'+
                                '</div>'+
                                '</div>'
                            );
                        }

                        
                    });
                }
                if(response.error == true){
                    $('#client_chat_container').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
                }
                if(chatHistoryList.length <= 0){
                    $('#client_chat_container').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no chats yet!</div>');
                }
                // chat_div.scrollTop = "100vh";
                let Height = document.getElementById("client_chat_container").scrollHeight;
                document.getElementById("client_chat_container").scrollTop = Height;
                console.log(Height)
            },
            error:function(e){
                console.log(e);
            },
        });
        
        
    });
});



// const intervalArtisanGigs = setInterval(function() {
//     document.getElementById("gigger-div").innerHTML = ""; 
//     $.ajax({
//         url:'/artisan_gig_main_ajax',
//         type:'GET',
//         success:function(response){
//             // console.log(response);
//             let artisanGigsList = response.artisanGigsList;
//             if(artisanGigsList.length > 0){
//                 artisanGigsList.forEach((element) => {
//                     if (element.projectStatus == "ongoing" && element.isCompleted == false) {  // ongoing project after artisan accept offer
//                         $('#gigger-div').append(
//                             '<div class="bid-card mt-3" id="'+element.project_id+'" onClick="ongoing_gig(this.id)">'+
//                                 '<p>'+element.title+'</p>'+
//                                 '<i class="fas fa-envelope " style="color: #0069F0;" ></i>'+
//                                 '<i class="fas fa-dot-circle " style="color: #D0BC0A;" ></i>'+
//                             '</div>'
//                         );
//                     }
//                     if (element.projectStatus == "completed") {  // order completed
//                         $('#gigger-div').append(
//                             '<div class="bid-card mt-3" id="'+element.project_id+'">'+
//                                 '<p>'+element.title+'</p>'+
//                                 '<i class="fas fa-check-circle  " style="color: #14E2CA;" ></i>'+
//                             '</div>'
//                         );
//                     }
    
//                     if (element.projectStatus == "disputed") {  // order disputed
//                         $('#gigger-div').append(
//                             '<div class="bid-card mt-3" id="'+element.project_id+'">'+
//                                 '<p>'+element.title+'</p>'+
//                                 '<i class="fas fa-question-circle  " style="color: #C4C4C4;" ></i>'+
//                             '</div>'
//                         );
//                     }
//                     if (element.projectStatus == "cancelled") {  // order cancelled
//                         $('#gigger-div').append(
//                             '<div class="bid-card mt-3" id="'+element.project_id+'">'+
//                                 '<p>'+element.title+'</p>'+
//                                 '<i class="fas fa-times-circle  " style="color: #C91B30;" ></i>'+
//                             '</div>'
//                         );
//                     }
//                     if (element.projectStatus == "ongoing" && element.isCompleted == true) {  // order completed by artisan awaiting client confirmation
//                         $('#gigger-div').append(
//                             '<div class="bid-card mt-3" id="'+element.project_id+'" data-toggle="modal" data-target="#artisanWaitModal">'+
//                                 '<p>'+element.title+'</p>'+
//                                 '<i class="fas fa-dot-circle " style="color: #14E2CA;" ></i>'+
//                             '</div>'
//                         );
//                     }
                    
//                 });
//             }
//             if(response.error == true){
//                 $('#gigger-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
//             }
//             if(artisanGigsList.length <= 0){
//                 $('#gigger-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Gigs for you yet!</div>');
//             }
//         },
//         error:function(e){
//             console.log(e);
//         },
//     });
    
//   }, 5000);

//   const intervalArtisanBids = setInterval(function() {
//     $.ajax({
//         url:'/artisan_gig_ajax',
//         type:'GET',
//         success:function(response){
//             // console.log(response);
//             let artisanBidsList = response.artisanBidsList;
//             if(artisanBidsList.length > 0){
//                 artisanBidsList.forEach((element) => {
//                     if (element.orderStatus == "pending" && element.fromAds == false ) {  // awaiting artisan's acceptance
//                         $('#bidder-div').append(
//                             '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="pending_order(this.id)">'+ 
//                                 '<p style="width: 70%;">'+element.title+'</p>'+
//                                 '<i class="fas fa-dot-circle  " style="color: #D0BC0A;" ></i>'+
//                                 '</div>'
//                         );
//                     }
//                     if (element.orderStatus == "pending" && element.fromAds == true) {  // awaiting artisan's acceptance
//                         $('#bidder-div').append(
//                             '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="pending_order(this.id)">'+ 
//                                 '<p style="width: 70%;">'+element.title+'</p>'+
//                                 '<i class="fas fa-dot-circle  " style="color: #D0BC0A;" ></i>'+
//                                 '</div>'
//                         );
//                     }
//                     if (element.orderStatus == "bidding" && element.winner_id =="" || element.winner_id == null) {  // oder still accepting bids
//                         $('#bidder-div').append(
//                             '<div class="bid-card mt-3" id="'+element.bid_id+'" onClick="bidding_ongoing(this.id)">'+ 
//                             '<p style="width: 70%;">'+element.title+'</p>'+
//                               '<div class="text-center">'+
//                                 '<i class="fas fa-user-plus " style="color: #40DA86;" ></i>'+
//                               '<p style="font-size: 0.5rem; color:#0069F0;"> You and '+parseInt(element.noOfBidders - 1)+' bidder(s)</p>'+
//                               '</div>'+
//                           '</div>'
//                         );
//                     }
//                     else {
//                         // $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are new Orders yet. However check the Gig section </div>');
//                     }
                    
//                 });
//             }
//             if(response.error == true){
//                 $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
//             }
//             if(artisanBidsList.length <= 0){
//                 $('#bidder-div').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Bids for you yet!</div>');
//             }
//         },
//         error:function(e){
//             console.log(e);
//         },
//     });
    
// }, 5000);
// const intervalArtisanHome = setInterval(function() {
//     $.ajax({
//         url:'/artisan_home_ajax',
//         type:'GET',
//         success:function(response){
//             // console.log(response);
//             document.getElementById('artisan_screen').innerHTML = ""
//             let orderList = response.orderList;
//             if(orderList.length > 0){
//                 orderList.forEach((element) => {
//                     $('#artisan_screen').append(
//                         '<div class="job-card">'+
//                         '<div class="job-inner">'+
//                             '<p>'+element.state+'</p>'+
//                             '<i class="fas fa-laptop fa-2x" style="color: #267DED;"></i>'+
//                             '<p>'+element.title+'</p>'+
//                             '<p class="job-amount">&#8358;'+element.min_budget+' - &#8358;'+element.max_budget+'</p></div>'+
//                         '<input type="button" value="Bid" class="form-control job-button" id="'+element.order_id+'" onClick="job_view(this.id)"></div>'
//                     );
//                 });
//             }
//             if(response.error == true){
//                 $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
//             }
//             if(orderList.length <= 0){
//                 $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Orders yet!</div>');
//             }
//         },
//         error:function(e){
//             // console.log(e);
//         },
//     });
// }, 500);
const intervalClientOrders = setInterval(function() {
}, 5000);
const intervalClientProjects = setInterval(function() {
}, 5000);
const intervalClientHome = setInterval(function() {
}, 5000);

// top-up api (paystack callback function)
$(function(){
    $('#verify_payment_button').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        document.getElementById("verify_payment_button").style.display = "none";
        let amount = document.getElementById("tt_amount").value;
        let user_id = document.getElementById("tt_id").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        // console.log(e);
        $.ajax({
            url:'/top_up_api',
            type:'POST',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                user_id: user_id,
                amount: amount,
            },
            success:function(response){
                document.getElementById("spinner").style.display = "none";
                console.log(response.data.role);
                if(response.error == true){
                    document.getElementById("failure_div").style.display = "block";
                }
                if(response.error == false){
                  document.getElementById("success_div").style.display = "block";          
                }
                setTimeout(function(){ 
                  if(response.data.role == "artisan"){
                    window.location.href = '/wallet';
                  }else{
                    window.location.href = '/client_wallet';
                  }
                    
                }, 2000);
            },
            error:function(e){
                console.log(e);
            },
        });
        
    });
});

// withdrawal function
$(function(){
    $('#withdrawal_button').on('click', function (e) {
        e.preventDefault();
        document.getElementById("spinner").style.display = "block";
        document.getElementById("withdrawal_button").style.display = "none";
        let amount = document.getElementById("w_amount").value;
        let balance = document.getElementById("w_balance").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        if ( parseFloat(amount) > parseFloat(balance)){
            document.getElementById("spinner").style.display = "none";
            document.getElementById("withdrawal_button").style.display = "block";
            document.getElementById("error_p2").innerHTML = "Sorry! you have Insufficient Balance";
            setTimeout(function(){ 
                document.getElementById("error_p2").innerHTML = "";
              }, 2000);
        }
        else if (parseFloat(amount) <= 0 || amount ==""){
            document.getElementById("withdrawal_button").style.display = "block";
            document.getElementById("spinner").style.display = "none";
            document.getElementById("error_p2").innerHTML = "Sorry! Kindly enter a non-zero amount";
            setTimeout(function(){ 
                document.getElementById("error_p2").innerHTML = "";
              }, 2000);
        }
        else{
            $.ajax({
                url:'/withdrawal_api',
                type:'POST',
                headers:{"X-CSRFToken": $crf_token},
                data:{
                    // user_id: user_id,
                    amount: amount,
                },
                success:function(response){
                    document.getElementById("spinner").style.display = "none";
                    console.log(response);
                    if(response.error == true){
                        document.getElementById("verification_div2").style.display = "block";
                        document.getElementById("failure_div2").style.display = "block";
                        document.getElementById("error_p").innerHTML = response.message;
                    }
                    if(response.error == false){
                        document.getElementById("verification_div2").style.display = "block";
                      document.getElementById("success_div2").style.display = "block";          
                    }
                    setTimeout(function(){ 
                      if(response.data.role == "artisan"){
                        window.location.href = '/wallet';
                      }else{
                        window.location.href = '/client_wallet';
                      }
                        
                    }, 2000);
                },
                error:function(e){
                    console.log(e);
                },
            });
            
        }
        // console.log(e);
        
    });
});