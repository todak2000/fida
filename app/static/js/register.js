$(document).ready(function(){
document.getElementById('sign_up_form').reset();
$("#form-part-two").hide();
document.getElementById("back_img").style.display = "none";
document.getElementById("complete").style.display = "none";

    $("#signup_next").click(function(){
        let password = document.getElementById("password").value;
        let confirm_password = document.getElementById("confirm_password").value;
        let firstname = document.getElementById("firstname").value;
        let lastname = document.getElementById("lastname").value;
        let phonenumber = document.getElementById("phonenumber").value;
        let email = document.getElementById("email").value;

        if (password =="" || confirm_password == "" || lastname == "" || firstname == "" || phonenumber == "" || email == ""){
        document.getElementById("message_one").style.display = "block";
        }
        else{
            if (password != confirm_password){
                document.getElementById("message").style.display = "block";
                document.getElementById("message_one").style.display = "none";
                // 
            }
            else{
            $("#form-part-one").hide();
            document.getElementById("message_one").style.display = "none";
            document.getElementById("message").style.display = "none";
            document.getElementById("back_img").style.display = "block";
            document.getElementById("form-part-two").style.display = "block";
            document.getElementById("complete").style.display = "block";
            document.getElementById("lets-get").style.display = "none";
            $("#form-part-two").show();
            }
        }
        
    });
    $("#back_img").click(function(){
        $("#form-part-one").show();
        document.getElementById("message_one").style.display = "none";
        document.getElementById("message").style.display = "none";
        $("#form-part-two").hide();
        // document.getElementById("server_message_success").style.display = "none";
        document.getElementById("back_img").style.display = "none";
        // document.getElementById("back_writeup").style.display = "none";
        // document.getElementById("back_writeup1").style.display = "block";
        // document.getElementById("server_message_error").style.display = "none";
        
        
    });

    
});
// show password
function showPassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}
// show password at login
function showPassword_login() {
    var x = document.getElementById("password_login");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


$(function(){
    $('#upload-icon').click(function(){
        $('#uploadme').click();
    });
});