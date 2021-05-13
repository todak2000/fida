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
                
            }, 6000);
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
                            
                        }, 6000);
                        
                    }
                    else{
                        document.getElementById('server_message_success').classList.add("alert-primary");
                        document.getElementById('server_message_success').innerHTML = response.message;
                        document.getElementById("server_message_success").style.display = "block";
                        setTimeout(function(){ 
                            document.getElementById("server_message_success").style.display = "none"; 
                            window.location.href = '/verify';
                        }, 3000);
                    }
                    console.log(response);
                },
                error:function(e){
                    console.log(e);
                },
            });
        }
    });
});

// VERIFY API
$(function(){
    $('#verify_submit').on('click', function (e) {
        e.preventDefault();
        // let code = document.getElementById("code").value;
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
                        
                    }, 3000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    // document.getElementById("email").value= response.email;
                    document.getElementById("verify_form").reset()
                    setTimeout(function(){ 
                        document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/login';
                    }, 6000);
                }
                console.log(response);
            },
            error:function(e){
                console.log(e);
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
                    }, 6000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/verify_password';
                    }, 3000);
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
        // let code = document.getElementById("code").value;
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
                        
                    }, 6000);
                    
                }
                else{
                    // document.getElementById('server_message_success').classList.add("alert-primary");
                    // document.getElementById('server_message_success').innerHTML = response.message;
                    // document.getElementById("server_message_success").style.display = "block";
                    // document.getElementById("email").value= response.email;
                    document.getElementById("verify_form").reset()
                    setTimeout(function(){ 
                        document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/reset_password';
                    }, 2000);
                }
                console.log(response);
            },
            error:function(e){
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
                    }, 6000);
                    
                }
                else{
                    document.getElementById('server_message_success').classList.add("alert-primary");
                    document.getElementById('server_message_success').innerHTML = response.message;
                    document.getElementById("server_message_success").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("server_message_success").style.display = "none"; 
                        window.location.href = '/login';
                    }, 3000);
                }
                console.log(response);
            },
            error:function(e){
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
        
        // let edit_first = document.getElementById("edit_first").value;
        // let edit_last = document.getElementById("edit_last").value;
        // let edit_email = document.getElementById("edit_email").value;
        let edit_address = document.getElementById("edit_address").value;
        let edit_state = document.getElementById("edit_state").value;
        let edit_phone = document.getElementById("edit_phone").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url:'/edit_bio_ajax',
            type:'PUT',
            headers:{"X-CSRFToken": $crf_token},
            data:{
                // edit_first: edit_first,
                // edit_last: edit_last,
                edit_phone: edit_phone,
                // edit_email: edit_email,
                edit_address: edit_address,
                edit_state: edit_state
            },
            success:function(response){
                console.log(response);
                if(response.error == false){
                    document.getElementById("bio_message_success").style.display = "block";
                    document.getElementById("bio_message_success").classList.add("alert-primary");
                    document.getElementById('bio_message_success').innerHTML = response.message;
                    
                    setTimeout(function(){ 
                        document.getElementById("bio_message_success").style.display = "none";
                        if (response.role == "artisan"){
                            window.location.href = '/account'; 
                        }
                        else{
                            window.location.href = '/client_account'; 
                        }
                        
                    }, 2000);
                    
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 5000);
                }
            },
            error:function(e){
                console.log(e);
            },
        });
    });
});

// edit account REUEST API
$(function(){
    $('#edit_account_submit').on('click', function (e) {
        e.preventDefault();
        
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
                if(response.error == false){
                    document.getElementById("bio_message_success").classList.add("alert-primary");
                    document.getElementById('bio_message_success').innerHTML = response.message;
                    document.getElementById("bio_message_success").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("bio_message_success").style.display = "none";
                        if (response.role == "artisan"){
                            window.location.href = '/account'; 
                        }
                        else{
                            window.location.href = '/client_account'; 
                        } 
                    }, 2000);
                    
                }
                else{
                    document.getElementById("bio_message_fail").classList.add("alert-danger");
                    document.getElementById('bio_message_fail').innerHTML = response.message;
                    document.getElementById("bio_message_fail").style.display = "block";
                    setTimeout(function(){ 
                        document.getElementById("bio_message_fail").style.display = "none"; 
                    }, 5000);
                }
            },
            error:function(e){
                console.log(e);
            },
        });
    });
});

//edit password REUEST API
$(function(){
    $('#password_submit').on('click', function (e) {
        e.preventDefault();
        
        let old_password = document.getElementById("old_password").value;
        let new_password = document.getElementById("new_password").value;
        let confirm_new_password = document.getElementById("confirm_new_password").value;
       if (new_password != confirm_new_password){
            document.getElementById("bio_message_fail").classList.add("alert-danger");
            document.getElementById('bio_message_fail').innerHTML = "Sorry! New Password do not match";
            document.getElementById("bio_message_fail").style.display = "block";
            setTimeout(function(){ 
                document.getElementById("bio_message_fail").style.display = "none"; 
            }, 5000);
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
                    if(response.error == false){
                        document.getElementById("bio_message_success").classList.add("alert-primary");
                        document.getElementById('bio_message_success').innerHTML = response.message;
                        document.getElementById("bio_message_success").style.display = "block";
                        setTimeout(function(){ 
                            document.getElementById("bio_message_success").style.display = "none"; 
                            if (response.role == "artisan"){
                                window.location.href = '/account'; 
                            }
                            else{
                                window.location.href = '/client_account'; 
                            } 
                        }, 2000);
                        
                    }
                    else{
                        document.getElementById("bio_message_fail").classList.add("alert-danger");
                        document.getElementById('bio_message_fail').innerHTML = response.message;
                        document.getElementById("bio_message_fail").style.display = "block";
                        setTimeout(function(){ 
                            document.getElementById("bio_message_fail").style.display = "none"; 
                        }, 5000);
                    }
                },
                error:function(e){
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
        
        let title = document.getElementById("title").value;
        let description = document.getElementById("description").value;
        let duration = document.getElementById("duration").value;
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
                duration: duration,
                state: state,
                location: location,
                min_budget: min_budget,
                max_budget: max_budget,
            },
            success:function(response){
                // console.log(response);
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
                    }, 5000);
                }
            },
            error:function(e){
                console.log(e);
            },
        });
        
    });
});

//new Ads REUEST API
$(function(){
    $('#new_ads_submit').on('click', function (e) {
        e.preventDefault();
        
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
                // console.log(response);
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
                    }, 5000);
                }
            },
            error:function(e){
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

$.ajax({
    url:'/client_home_ajax',
    type:'GET',
    success:function(response){
        // console.log(response);
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
        console.log(e);
    },
});

//GET ORDERS ARTISAN HOME REUEST API

$.ajax({
    url:'/artisan_home_ajax',
    type:'GET',
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
            $('#artisan_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">Sorry there are no Orders yet!</div>');
        }
    },
    error:function(e){
        console.log(e);
    },
});

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
                        '<input type="button" value="Bid" class="form-control job-button" id="id="'+element.order_id+'" onClick="job_view(this.id)"></div>'
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
                        '<input type="button" value="Create Order" class="form-control job-button" id="id="'+element.order_id+'" onClick="ads_view(this.id)"></div>'
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
            if(jobView){
                console.log(response);
                document.getElementById('job_title').value = jobView.title;
                document.getElementById('job_description').value = jobView.description;
                document.getElementById('job_duration').value = jobView.duration;
                document.getElementById('job_max_budget').value = "NGN"+jobView.max_budget;
                document.getElementById('job_location').value = jobView.location;
                document.getElementById('job_state').value = jobView.state;

                document.getElementById('job_id').value = jobView.job_id;
                $('#jobDetailsModal').modal('show');
            }
            if(response.error == true){
                console.log(response)
                // $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(jobView.length <= 0){
                console.log(response)
                // $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">'+response.message+'</div>');
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
                document.getElementById('ads_duration').value = adsView.duration;
                document.getElementById('ads_max_budget').value = "NGN"+adsView.max_budget;
                document.getElementById('ads_min_budget').value = "NGN"+adsView.min_budget;
                document.getElementById('ads_location').value = adsView.location;
                document.getElementById('ads_state').value = adsView.state;

                document.getElementById('ads_id').value = adsView.ads_id;
                $('#createOrderModal').modal('show');
            }
            if(response.error == true){
                console.log(response)
                // $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">An error occured. Try again!</div>');
            }
            if(jobView.length <= 0){
                console.log(response)
                // $('#client_screen').append('<div class="text-center" style="color: #448AC9; margin-top:50px;">'+response.message+'</div>');
            }
        },
        error:function(e){
            console.log(e);
        },
    });
}