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
        let state = document.getElementById("state").value;
        let $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        document.getElementById("spinner").style.display = "block";
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