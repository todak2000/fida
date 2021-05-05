from django.shortcuts import render, redirect
import datetime
import json
import requests
import jwt

from app.models import (User,Verification)
from CustomCode import (autentication,  password_functions,
                        string_generator, validator)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from project_fida import settings

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.http import HttpResponse

from pysendpulse.pysendpulse import PySendPulse
from decouple import config

REST_API_ID = config("REST_API_ID")
REST_API_SECRET = config("REST_API_SECRET")
TOKEN_STORAGE = config("TOKEN_STORAGE")
MEMCACHED_HOST = config("MEMCACHED_HOST")
SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

# Create your views here.

def index(request):
    return render(request,"onboarding/splashscreen.html") 

def register_page(request):
    return render(request,"onboarding/register.html")

# signout api     
def logout_page(request):
    if 'email' in request.session:
        del request.session['email']
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/login')

def login_page(request):
    return render(request,"onboarding/login.html") 

def verify_page(request):
    user_email = request.session['email']
    return_data = {
        "email":user_email,
    }
    return render(request,"onboarding/verify.html", return_data) 

def verify_password_page(request):
    user_email = request.session['email']
    return_data = {
        "email":user_email,
    }
    return render(request,"onboarding/verify_password.html", return_data) 

def forget_password_page(request):
    return render(request,"onboarding/forget_password.html") 

def reset_password_page(request):
    return render(request,"onboarding/reset_password.html")

def artisan_home_page(request):
    return render(request,"artisan/home/home.html") 

def job_details_page(request):
    return render(request,"artisan/home/job_details.html") 

def gig_page(request):
    return render(request,"artisan/gig/gig.html") 

def pending_bid_page(request):
    return render(request,"artisan/gig/pending_bid.html") 

def winning_bid_page(request):
    return render(request,"artisan/gig/winning_bid.html")

def pending_gig_page(request):
    return render(request,"artisan/gig/pending_gig.html") 

def ongoing_gig_page(request):
    return render(request,"artisan/gig/ongoing_gig.html")

def awaiting_gig_page(request):
    return render(request,"artisan/gig/awaiting_gig.html")

def approved_gig_page(request):
    return render(request,"artisan/gig/approved_gig.html")

def disputed_gig_page(request):
    return render(request,"artisan/gig/disputed_gig.html") 

def wallet_page(request):
    return render(request,"artisan/wallet/wallet.html")

def top_up_page(request):
    return render(request,"artisan/wallet/top_up.html")

def withdraw_page(request):
    return render(request,"artisan/wallet/withdraw.html")

def new_ads_page(request):
    return render(request,"artisan/home/new_ads.html")

def chat_page(request):
    return render(request,"artisan/chat/chat.html")

def individual_chat_page(request):
    return render(request,"artisan/chat/individual_chat.html")

def account_page(request):
    return render(request,"artisan/account/account.html")

def edit_bio_page(request):
    return render(request,"artisan/account/edit_bio.html")

def edit_account_page(request):
    return render(request,"artisan/account/edit_account.html")

def edit_password_page(request):
    return render(request,"artisan/account/edit_password.html")

def view_ads_page(request):
    return render(request,"artisan/account/view_ads.html")

def edit_ads_page(request):
    return render(request,"artisan/account/edit_ads.html")

# client pages api
def client_home_page(request):
    return render(request,"client/home/home.html") 

def ads_details_page(request):
    return render(request,"client/home/ads_details.html") 

def create_order_page(request):
    return render(request,"client/home/create_order.html")

def new_order_page(request):
    return render(request,"client/home/new_order.html")

def project_page(request):
    return render(request,"client/project/project.html") 

def pending_order_page(request):
    return render(request,"client/project/pending_order.html") 

def declined_order_page(request):
    return render(request,"client/project/declined_order.html")

def ongoing_project_page(request):
    return render(request,"client/project/ongoing_project.html")

def ongoing_order_page(request):
    return render(request,"client/project/ongoing_order.html")

def pending_project_page(request):
    return render(request,"client/project/pending_project.html")

def approved_project_page(request):
    return render(request,"client/project/approved_project.html")

def disputed_project_page(request):
    return render(request,"client/project/disputed_project.html") 

def client_wallet_page(request):
    return render(request,"client/wallet/wallet.html")

def client_top_up_page(request):
    return render(request,"client/wallet/top_up.html")

def client_withdraw_page(request):
    return render(request,"client/wallet/withdraw.html")

def client_chat_page(request):
    return render(request,"client/chat/chat.html")

def client_individual_chat_page(request):
    return render(request,"client/chat/individual_chat.html")

def client_account_page(request):
    return render(request,"client/account/account.html")

def client_edit_bio_page(request):
    return render(request,"client/account/edit_bio.html")

def client_edit_account_page(request):
    return render(request,"client/account/edit_account.html")

def client_edit_password_page(request):
    return render(request,"client/account/edit_password.html")

# *******************ONBOARDING APIS*********************************************
# SIGN UP API
@api_view(["POST"])
def register_api(request):
    try:
        firstName = request.data.get('firstname',None)
        lastName = request.data.get('lastname',None)
        phoneNumber = request.data.get('phonenumber',None)
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        address = request.data.get('address',None)
        state = request.data.get('state',None)
        role = request.data.get('role',None)
        reg_field = [firstName,lastName,phoneNumber,email,password,address, role]
        if not None in reg_field and not "" in reg_field:
            if User.objects.filter(user_phone =phoneNumber).exists() or User.objects.filter(email =email).exists():
                return_data = {
                    "error": True,
                    "message": "User Exists, Kindly login"
                }
            elif validator.checkmail(email) == False:
                return_data = {
                    "error": True,
                    "message": "Email is Invalid"
                }
            else:
                #generate user_id
                if role == "artisan":
                    userRandomId = "ART"+string_generator.numeric(4)
                else:
                    userRandomId = "CLT"+string_generator.numeric(4)
                #encrypt password
                encryped_password = password_functions.generate_password_hash(password)
                #Save user_data
                new_userData = User(user_id=userRandomId,firstname=firstName,lastname=lastName,
                                email=email,user_phone=phoneNumber,
                                user_password=encryped_password,user_address=address, user_state=state, role=role)
                new_userData.save()
                #Generate OTP
                code = string_generator.numeric(4)
                #Save OTP
                user_OTP =Verification(user_id=new_userData,code=code, isVerified=False)
                user_OTP.save()
                # Send mail using SMTP
                mail_subject = 'Activate your Fida account.'
                email = {
                    'subject': mail_subject,
                    'html': '<h4>Hello, '+firstName+'!</h4><p>Kindly use the Verification Code below to activate your Fida Account</p> <h1>'+code+'</h1>',
                    'text': 'Hello, '+firstName+'!\nKindly use the Verification Code below to activate your Fida Account',
                    'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                    'to': [
                        {'name': firstName, 'email': email}
                    ]
                }
                SPApiProxy.smtp_send_mail(email)
                request.session['email'] = new_userData.email
                return_data = {
                    "error": False,
                    "message": "Registrated successfully. Kind check your email to activate your account.",
                    }
        else:
            return_data = {
                "error":True,
                "message": "One or more fields is empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            "message": str(e)
            # "message": "Something went wrong!"
        }
    return Response(return_data)

# email activation
@api_view(["POST"]) 
def activate(request):
    try:
        code = request.data.get('code',None)
        field = [code]
        user_email = request.session['email']
        if not None in field and not "" in field:
            userVerificationCode = Verification.objects.get(code=code)  
            if userVerificationCode:
                userVerificationCode.isVerified = True
                userVerificationCode.save()
                return_data = {
                    "error": False,
                    "message": 'Your Account is now verified. Kindly login!.'
                }
            else:
                return_data = {
                    "error": True,
                    "message": 'Sorry, Verification Code is invalid!'
                }
        else:
            return_data = {
                "error":True,
                "message": "The input field is empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            # "message": str(e)
            "message": "Sorry, Verification Code is invalid!"
        }
    return Response(return_data)


# RESEND VERIFICATION CODE API
@api_view(["POST"])
def resend_code_api(request):
    try:
        email = request.data.get('email',None)
        field = [email]
        if not None in field and not "" in field:
            if User.objects.filter(email =email).exists():
                verificationData = Verification.objects.get(user_id__email = email)
                userData = User.objects.get(email=email)
                firstName = userData.firstname
                code = verificationData.code
                if code:
                    # Resend mail using SMTP
                    mail_subject = 'Activate Code Sent again for your Fida account.'
                    resentEmail = {
                        'subject': mail_subject,
                        'html': '<h4>Hello, '+firstName+'!</h4><p>Kindly find the Verification Code below sent again to activate your Fida Account</p> <h1>'+code+'</h1>',
                        'text': 'Hello, '+firstName+'!\nKindly find the Verification Code below sent againto activate your Fida Account',
                        'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                        'to': [
                            {'name': firstName, 'email': email}
                        ]
                    }
                    SPApiProxy.smtp_send_mail(resentEmail)
                    return_data = {
                        "error": False,
                        "message": "Verfication Code sent again!"
                    }
                else:
                    return_data = {
                        "error": False,
                        "message": "We could not retrieve your Verification Code. Kindly register!"
                    }
            elif validator.checkmail(email) == False:
                return_data = {
                    "error": True,
                    "message": "Email is Invalid"
                }
        else:
            return_data = {
                "error":True,
                "message": "One or more fields is empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            "message": str(e)
            # "message": "Something went wrong!"
        }
    return Response(return_data)

# SEND PASSWORD LINK (FOROGT PASSWORD PAGE) API
@api_view(["POST"])
def forgot_code_api(request):
    try:
        email = request.data.get('email',None)
        field = [email]
        if not None in field and not "" in field:
            if User.objects.filter(email =email).exists():
                verificationData = Verification.objects.get(user_id__email = email)
                userData = User.objects.get(email=email)
                firstName = userData.firstname
                code = verificationData.code
                request.session['email'] = userData.email
                if code:
                    # Resend mail using SMTP
                    mail_subject = 'Reset your Fida account Password Confirmation.'
                    resentEmail = {
                        'subject': mail_subject,
                        'html': '<h4>Hi, '+firstName+'!</h4><p>Kindly find the Reset Code below to confirm that intend to change your Fida Account Password</p> <h1>'+code+'</h1>',
                        'text': 'Hello, '+firstName+'!\nKindly find the Reset Code below to confirm that intend to change your Fida Account Password',
                        'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                        'to': [
                            {'name': firstName, 'email': email}
                        ]
                    }
                    SPApiProxy.smtp_send_mail(resentEmail)
                    return_data = {
                        "error": False,
                        "message": "Reset Code sent!"
                    }
                else:
                    return_data = {
                        "error": False,
                        "message": "Sorry! try again"
                    }
            elif validator.checkmail(email) == False:
                return_data = {
                    "error": True,
                    "message": "Email is Invalid"
                }
            else:
                return_data = {
                    "error": True,
                    "message": "Email does not exist in our database"
                }
        else:
            return_data = {
                "error":True,
                "message": "One or more fields is empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            # "message": str(e)
            "message": "Something went wrong!"
        }
    return Response(return_data)

# CHANGE PASSWORD API
@api_view(["POST"])
def change_password(request):
    try:
        user_email = request.session['email']
        new_password = request.data.get("password",None)
        confirm_new_password = request.data.get("confirm_password",None)
        user_data = User.objects.get(email=user_email)  
        
        if user_data:
            if new_password != confirm_new_password:
                return_data = {
                    "error": True,
                    "message": "Password dont match!"
                }
            else:
                encryptpassword = password_functions.generate_password_hash(new_password)
                user_data.user_password = encryptpassword
                user_data.save()
                return_data = {
                    "error": False,
                    "message": "Password Changed Successfully! Kindly login"
                }

        else:
            return_data = {
                "error": True,
                "message": 'Sorry, You are not Authorized to access this link!'
            }
    except Exception as e:
        return_data = {
                "error": True,
                # "message": str(e)
                "message": 'Sorry, Something went wrong!'
            }
    return Response(return_data)

#SIGNIN API
@api_view(["POST"])
def login_api(request):
    try:
        email = request.data.get("email",None)
        password = request.data.get("password",None)
        field = [email,password]
        if not None in field and not '' in field:
            validate_mail = validator.checkmail(email)
            if validate_mail == True:
                if User.objects.filter(email =email).exists() == False:
                    return_data = {
                        "error": True,
                        "message": "User does not exist"
                    }
                else: 
                    user_data = User.objects.get(email=email)
                    is_valid_password = password_functions.check_password_match(password,user_data.user_password)
                    isVerified= Verification.objects.get(user_id__user_id=user_data.user_id).isVerified
                    if is_valid_password and isVerified:
                        request.session['user_id'] = user_data.user_id
                        request.session['email'] = user_data.email
                        if user_data.role == "artisan":
                            return_data = {
                            "error": False,
                            "profileComplete": user_data.profile_complete,
                            "user_name": f"{user_data.firstname}"
                            }
                            return render(request,"artisan/home/home.html", return_data)
                        else:
                            return_data = {
                            "error": False,
                            "profileComplete": user_data.profile_complete,
                            "user_name": f"{user_data.firstname}"
                            }
                            return render(request,"client/home/home.html", return_data)
                    elif isVerified == False:
                        user_email = request.session['email']
                        return_data = {
                            "error" : True,
                            "email":user_email,
                            "message": "Sorry, Your account is not yet activated. Click on Resend code to get new Activation codes",
                        }
                        return render(request,"onboarding/verify.html", return_data)
                    else:
                        return_data = {
                            "error" : True,
                            "message" : "Wrong Password"
                        }
            else:
                return_data = {
                    "error": True,
                    "message": "Email is Invalid"
                }
        else:
            return_data = {
                "error" : True,
                "message" : "Invalid Parameters"
                }
    except Exception as e:
        return_data = {
            "error": True,
            "message": str(e)
        }
    return render(request,"onboarding/login.html", return_data)

# @api_view(["GET"])
# def dashboard(request):
#     try:
#         user_id = request.session['user_id']
#         if user_id != None and user_id != '':
#             #get user info
#             user_data = User.objects.get(user_id=user_id)
#             footprint = user_data.minedCoins*0.03
#             return_data = {
#                 "error": False,
#                 "message": "Sucessfull",
#                 "user_details": 
#                     {
#                         "firstname": f"{user_data.firstname}",
#                         "lastname": f"{user_data.lastname}",
#                         "email": f"{user_data.email}",
#                         "phonenumber": f"{user_data.user_phone}",
#                         "address": f"{user_data.user_address}",
#                         "carbon_footprint": footprint
#                     }
#             }
#         else:
#             return_data = {
#                 "error": True,
#                 "message": "Invalid Parameter"
#             }
#     except Exception as e:
#         return_data = {
#             "error": True,
#             "message": str(e)
#         }
#     return render(request,"user/dashboard.html", return_data)
