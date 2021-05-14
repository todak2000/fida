from django.shortcuts import render, redirect
import datetime
import json
import requests
import jwt

from app.models import (User,Verification, Ads, Orders, Bids, Escrow, Project_Gig, Transaction, Chat)
from CustomCode import (autentication,  password_functions,
                        string_generator, validator)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from project_fida import settings

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

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
    user_id = request.session['user_id']
    try:
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}"
        }
    except Exception as e:
        return_data = {
            "error": True,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}",
            "message": "Something went wrong!"
        }
    return render(request,"artisan/home/home.html", return_data) 

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
    user_id = request.session['user_id']
    try:
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}"
        }
    except Exception as e:
        return_data = {
            "error": True,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}",
            "message": "Something went wrong!"
        }
    return render(request,"artisan/home/new_ads.html", return_data)

def chat_page(request):
    return render(request,"artisan/chat/chat.html")

def individual_chat_page(request):
    return render(request,"artisan/chat/individual_chat.html")

def account_page(request):
    user_id = request.session['user_id']
    try:
        userData = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "user": userData
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"artisan/account/account.html", return_data)

def edit_bio_page(request):
    user_id = request.session['user_id']
    try:
        userData = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "user": userData
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"artisan/account/edit_bio.html", return_data)

def edit_account_page(request):
    user_id = request.session['user_id']
    try:
        userData = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "user": userData
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"artisan/account/edit_account.html", return_data)

def edit_password_page(request):
    return render(request,"artisan/account/edit_password.html")

def view_ads_page(request):
    user_id = request.session['user_id']
    try:
        userAds = Ads.objects.get(artisan_id=user_id)
        return_data = {
            "error": False,
            "userAds": userAds
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"artisan/account/view_ads.html" , return_data)

def edit_ads_page(request):
    user_id = request.session['user_id']
    try:
        userData = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "user": userData
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"artisan/account/edit_ads.html" , return_data)

# client pages api
def client_home_page(request):
    user_id = request.session['user_id']
    try:
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}"
        }
    except Exception as e:
        return_data = {
            "error": True,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}",
            "message": "Something went wrong!"
        }
    return render(request,"client/home/home.html", return_data) 

def ads_details_page(request):
    return render(request,"client/home/ads_details.html") 

def create_order_page(request):
    return render(request,"client/home/create_order.html")

def new_order_page(request):
    user_id = request.session['user_id']
    try:
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}"
        }
    except Exception as e:
        return_data = {
            "error": True,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}",
            "message": "Something went wrong!"
        }
    return render(request,"client/home/new_order.html", return_data)

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
    user_id = request.session['user_id']
    try:
        userData = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "user": userData
        }
    except Exception as e:
        return_data = {
            "error": True,
            "message": "Something went wrong!"
        }
    return render(request,"client/account/account.html", return_data)

# def client_edit_bio_page(request):
#     return render(request,"client/account/edit_bio.html")

# def client_edit_account_page(request):
#     return render(request,"client/account/edit_account.html")

# def client_edit_password_page(request):
#     return render(request,"client/account/edit_password.html")

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
                                user_password=encryped_password,user_address=address, user_state=state, role=role, terms_conditions=True)
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

#SIGNIN API FOR BOTH ARTISAN AND CLIENT
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

# add/edit Account details FOR BOTH ARTISAN AND CLIENT
@api_view(["PUT"])
def edit_account_ajax(request):
    user_id = request.session['user_id']
    try:
        accountName = request.data.get("edit_name",None)
        accountNumber = request.data.get("edit_number",None)
        bankName = request.data.get("edit_bank",None)
        field = [accountName,accountNumber,bankName]
        user_data = User.objects.get(user_id=user_id)
        if not None in field and not "" in field:
            user_data.account_number = accountNumber
            user_data.account_name = accountName
            user_data.bank_name = bankName
            user_data.profile_complete = True
            user_data.save()
            return_data = {
                "error": False,
                "role": user_data.role,
                "message": "Account saved Successfully!",
            }
        else:
            return_data = {
                "error": True,
                "role": user_data.role,
                "message": "One or more fields is Empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            "role": user_data.role,
            "message": str(e)
        }
    return Response(return_data)

# add/edit bIO details FOR BOTH ARTISAN AND CLIENT
@api_view(["PUT"])
def edit_bio_ajax(request):
    user_id = request.session['user_id']
    try:
        # update_first_name = request.data.get("edit_first",None)
        # update_last_name = request.data.get("edit_last",None)
        # update_email = request.data.get("edit_email",None)
        update_phone = request.data.get("edit_phone",None)
        update_address = request.data.get("edit_address",None)
        # update_council = request.data.get("edit_lga",None)
        update_state = request.data.get("edit_state",None)
        user_data = User.objects.get(user_id=user_id)
        field = [update_phone,update_address,update_state]
        if not None in field and not "" in field:
            
            # user_data.firstname = update_first_name
            # user_data.lastname = update_last_name
            user_data.user_phone = update_phone
            # user_data.email = update_email
            user_data.user_address = update_address
            user_data.user_state = update_state
            # user_data.user_council_area = update_council
            user_data.save()
            return_data = {
                "error": False,
                "role": user_data.role,
                "message": "Bio-Data  Updated Successfully!",
            }
        else:
            return_data = {
                "error": True,
                "role": user_data.role,
                "message": "One or more fields is Empty!"
            }
    except Exception as e:
        return_data = {
            "error": True,
            "role": user_data.role,
            "message": str(e)
        }
    return Response(return_data)

# update password
@api_view(["PUT"])
def edit_password_ajax(request):
    
    try:
        user_id = request.session['user_id']
        old_password = request.data.get("old_password",None)
        new_password = request.data.get("new_password",None)
        field = [old_password,new_password]
        user_data = User.objects.get(user_id=user_id)
        if not None in field and not "" in field:
            is_valid_password = password_functions.check_password_match(old_password,user_data.user_password)
            if is_valid_password == False:
                return_data = {
                    "error": True,
                    "role": user_data.role,
                    "message": "Old Password is Incorrect"
                }
            else:
                #decrypt password
                encryptpassword = password_functions.generate_password_hash(new_password)
                user_data.user_password = encryptpassword
                user_data.save()
                return_data = {
                    "error": False,
                    "role": user_data.role,
                    "message": "Password Changed Successfully! "
                }
    except Exception as e:
        return_data = {
                "error": True,
                "role": user_data.role,
                "message": str(e)
        }
    return Response(return_data)


# CLIENT NEW ORDER API
@api_view(["POST"])
def new_order_api(request):
    user_id = request.session['user_id']
    try:
        title = request.data.get('title',None)
        description = request.data.get('description',None)
        duration = request.data.get('duration',None)
        state = request.data.get('state',None)
        location = request.data.get('location',None)
        min_budget = request.data.get('min_budget',None)
        max_budget = request.data.get('max_budget',None)
        field = [title, description, duration, state, location, min_budget, max_budget]
        user_data = User.objects.get(user_id=user_id)
        if not None in field and not "" in field:
            newOrder = Orders(title=title,description=description,duration=duration,min_budget=min_budget,max_budget=max_budget,location=location,state=state,client_id=user_data, orderStatus="bidding")
            newOrder.save()
            return_data = {
                "error": False,
                "message": "Order Created Successfully!"
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

# ARTISAN NEW ADS API
@api_view(["POST"])
def new_ads_api(request):
    user_id = request.session['user_id']
    try:
        title = request.data.get('title',None)
        description = request.data.get('description',None)
        # duration = request.data.get('duration',None)
        state = request.data.get('state',None)
        location = request.data.get('location',None)
        min_budget = request.data.get('min_budget',None)
        pitch = request.data.get('pitch',None)
        max_budget = request.data.get('max_budget',None)
        field = [title, description, state, location, min_budget, max_budget]
        user_data = User.objects.get(user_id=user_id)
        if not None in field and not "" in field:
            newAds = Ads(title=title,description=description,min_budget=min_budget,max_budget=max_budget,location=location,state=state,artisan_id=user_data,other_info=pitch)
            newAds.save()
            return_data = {
                "error": False,
                "message": "Ads Created Successfully!"
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

# Ads List for Artisan Accoutn view
@api_view(["GET"])
def ads_list_ajax(request):
    user_id = request.session['user_id']
    try:
        user_data = User.objects.get(user_id=user_id)
        adsData = Ads.objects.filter(artisan_id=user_data) 
        num = len(adsData)
        adsList = []
        for i in range(0,num):
            ads_id = adsData[i].id
            title = adsData[i].title 
            no_of_views = adsData[i].no_of_views
            to_json = {
                "ads_id": ads_id,
                "title": title,
                "views": no_of_views,

            }
            adsList.append(to_json)
        return JsonResponse({ 'adsList':adsList, 'error': False})
    except Exception as e:
        adsList = []
        return JsonResponse({ 'adsList':adsList, 'error': True, 'message': str(e)})

# Ads List for Client Home
@api_view(["GET"])
def client_home_ajax(request):
    try:
        adsData = Ads.objects.all().order_by('-date_added')[:20]
        num = len(adsData)
        adsList = []
        for i in range(0,num):
            ads_id = adsData[i].id
            title = adsData[i].title 
            state = adsData[i].state
            min_budget = adsData[i].min_budget 
            max_budget = adsData[i].max_budget
            to_json = {
                "ads_id": ads_id,
                "title": title,
                "state": state,
                "min_budget": min_budget,
                "max_budget": max_budget,
            }
            adsList.append(to_json)
        return JsonResponse({ 'adsList':adsList, 'error': False})
    except Exception as e:
        adsList = []
        return JsonResponse({ 'adsList':adsList, 'error': True, 'message': str(e)})

# Ads List for Client Home
@api_view(["GET"])
def artisan_home_ajax(request):
    try:
        orderData = Orders.objects.all().order_by('-date_added')[:20]
        num = len(orderData)
        orderList = []
        for i in range(0,num):
            order_id = orderData[i].id
            title = orderData[i].title 
            state = orderData[i].state
            min_budget = orderData[i].min_budget 
            max_budget = orderData[i].max_budget
            to_json = {
                "order_id": order_id,
                "title": title,
                "state": state,
                "min_budget": min_budget,
                "max_budget": max_budget,
            }
            orderList.append(to_json)
        return JsonResponse({ 'orderList':orderList, 'error': False})
    except Exception as e:
        orderList = []
        return JsonResponse({ 'orderList':orderList, 'error': True, 'message': str(e)})

# Orders Search by Artisan
@api_view(["POST"])
def order_search(request):
    query_raw = request.POST["orders_search_query"]
    query = query_raw.capitalize()
    orderData = Orders.objects.filter(title__icontains=query) or  Orders.objects.filter(state__icontains=query) or Orders.objects.filter(description__icontains=query)
    orderList = []
    try:
        if len(orderData) > 0:
            num = len(orderData)
            for i in range(0,num):
                order_id = orderData[i].id
                title = orderData[i].title 
                state = orderData[i].state
                min_budget = orderData[i].min_budget 
                max_budget = orderData[i].max_budget
                to_json = {
                    "order_id": order_id,
                    "title": title,
                    "state": state,
                    "min_budget": min_budget,
                    "max_budget": max_budget,
                }
            orderList.append(to_json)
            return JsonResponse({ 'orderList':orderList, 'error': False})
        else:
            return JsonResponse({ 'orderList':orderList, 'error': False, 'message':"Sorry! No results for your Search"})

    except Exception as e:
        return JsonResponse({ 'orderList':orderList, 'error': True, 'message': str(e)})

# Ads Search by Client
@api_view(["POST"])
def ads_search(request):
    query_raw = request.POST["ads_search_query"]
    query = query_raw.capitalize()
    adsData = Ads.objects.filter(title__icontains=query) or  Ads.objects.filter(state__icontains=query) or Ads.objects.filter(description__icontains=query)
    adsList = []
    try:
        if len(adsData) > 0:
            num = len(adsData)
            for i in range(0,num):
                ads_id = adsData[i].id
                title = adsData[i].title 
                state = adsData[i].state
                min_budget = adsData[i].min_budget 
                max_budget = adsData[i].max_budget
                to_json = {
                    "ads_id": ads_id,
                    "title": title,
                    "state": state,
                    "min_budget": min_budget,
                    "max_budget": max_budget,
                }
            adsList.append(to_json)
            return JsonResponse({ 'adsList':adsList, 'error': False})
        else:
            return JsonResponse({ 'adsList':adsList, 'error': False, 'message':"Sorry! No results for your Search"})

    except Exception as e:
        return JsonResponse({ 'adsList':adsList, 'error': True, 'message': str(e)})

# JOb Veiw (Artisan) by Client
@api_view(["POST"])
def job_view(request):
    job_id = request.POST["id"]
    jobOrder = Orders.objects.get(id=job_id)
    try:
        if jobOrder:
            job_id = jobOrder.id
            title = jobOrder.title 
            description = jobOrder.description
            duration = jobOrder.duration
            location = jobOrder.location
            state = jobOrder.state
            max_budget = jobOrder.max_budget
            to_json = {
                "job_id": job_id,
                "title": title,
                "state": state,
                "description": description,
                "location": location,
                "duration": duration,
                "max_budget": max_budget,
            }
            return JsonResponse({ 'jobView':to_json, 'error': False})
        else:
            return JsonResponse({  'error': False, 'message':"Sorry, Job Order no longer available!"})

    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Ads Search by Client
@api_view(["POST"])
def ads_view(request):
    ads_id = request.POST["id"]
    adsOrder = Ads.objects.get(id=ads_id)
    try:
        if adsOrder:
            ads_id = adsOrder.id
            title = adsOrder.title 
            description = adsOrder.description
            duration = adsOrder.duration
            location = adsOrder.location
            state = adsOrder.state
            max_budget = adsOrder.max_budget
            min_budget = adsOrder.min_budget
            to_json = {
                "ads_id": ads_id,
                "title": title,
                "state": state,
                "description": description,
                "location": location,
                "duration": duration,
                "max_budget": max_budget,
                "min_budget": min_budget,
            }
            return JsonResponse({ 'adsView':to_json, 'error': False})
        else:
            return JsonResponse({  'error': False, 'message':"Sorry, Job Order no longer available!"})

    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Submit Order for a specific Artisan Ads by Client
@api_view(["POST"])
def submit_order_specific_artisan(request):
    user_id = request.session['user_id']
    ads_id = request.POST["ads_id"]
    ads_fee = request.POST["ads_fee"]
    ads_pitch = request.POST["ads_pitch"]

    ads_title = request.POST["ads_title"]
    ads_description = request.POST["ads_description"]
    ads_min_budget = request.POST["ads_min_budget"]
    ads_max_budget= request.POST["ads_max_budget"]
    ads_location = request.POST["ads_location"]
    ads_state = request.POST["ads_state"]
    user = User.objects.get(user_id=user_id)
    try:
        field = [ads_fee]
        if not None in field and not "" in field:
            ads = Ads.objects.get(id=ads_id)
            newOrder = Orders(client_id=user, title=ads_title, description=ads_description, min_budget=ads_min_budget, max_budget=ads_max_budget, location=ads_location, state=ads_state, service_fee=ads_fee, pitch=ads_pitch, noOfBidders = 1,winner_id=ads.artisan_id.user_id, orderStatus="pending" )
            newOrder.save()
            
            onlyBid = Bids(order_id=newOrder, bidder="No bid process", service_fee=ads_fee, pitch=ads_pitch)
            onlyBid.save()
            if newOrder and onlyBid:
                return JsonResponse({ 'message':'Order successfully sent. Kindly await Artisan response', 'error': False})
            else:
                return JsonResponse({  'error': True, 'message':"Sorry, an error occured"})
        else:
            return JsonResponse({'error': True, "message": "Kindly add the service fee.Thanks!"})
            
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Project ajax page get orders/projects
@api_view(["GET"])
def client_project_ajax(request):
    user_id = request.session['user_id']
    client = User.objects.get(user_id=user_id)
    try:
        clientOrders = Orders.objects.filter(client_id=client).order_by('-date_added')[:20]
        num = len(clientOrders)
        clientOrdersList = []
        for i in range(0,num):
            order_id = clientOrders[i].id
            title = clientOrders[i].title 
            noOfBidders = clientOrders[i].noOfBidders
            orderStatus  = clientOrders[i].orderStatus 
            to_json = {
                "order_id": order_id,
                "title": title,
                "noOfBidders": noOfBidders,
                "orderStatus": orderStatus,

            }
            clientOrdersList.append(to_json)
        return JsonResponse({ 'clientOrdersList':clientOrdersList, 'error': False})
    except Exception as e:
        clientOrdersList = []
        return JsonResponse({ 'clientOrdersList':clientOrdersList, 'error': True, 'message': str(e)})

# SUbmit bid for an Order by Artisan
@api_view(["POST"])
def submit_bid(request):
    user_id = request.session['user_id']
    job_id = request.POST["job_id"]
    job_fee = request.POST["job_fee"]
    job_pitch = request.POST["job_pitch"]
    # user = User.objects.get(user_id=user_id)
    try:
        field = [job_fee]
        if not None in field and not "" in field:
            order = Orders.objects.get(id=job_id)
            newBid = Bids(order_id=order, bidder=user_id, service_fee=job_fee, pitch=job_pitch)
            newBid.save()
            if newBid:
                return JsonResponse({ 'message':'Bid was successfully', 'error': False})
            else:
                return JsonResponse({  'error': True, 'message':"Sorry, an error occured"})
        else:
            return JsonResponse({'error': True, "message": "Kindly add the service fee.Thanks!"})
            
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Bids section ajax page get bids/gigs
@api_view(["GET"])
def artisan_gig_ajax(request):
    user_id = request.session['user_id']
    try:
        arisanBids = Bids.objects.filter(bidder=user_id).order_by('-date_added')[:20] | Bids.objects.filter(order_id__winner_id=user_id).order_by('-date_added')
        num = len(arisanBids)
        arisanBidsList = []
        for i in range(0,num):
            bid_id = arisanBids[i].id
            title = arisanBids[i].order_id.title 
            noOfBidders = arisanBids[i].order_id.noOfBidders
            orderStatus  = arisanBids[i].order_id.orderStatus 
            winner_id = arisanBids[i].order_id.winner_id
            to_json = {
                "bid_id": bid_id,
                "title": title,
                "noOfBidders": noOfBidders,
                "orderStatus": orderStatus,
                "winner_id": winner_id,
                "user_id": user_id,
            }
            arisanBidsList.append(to_json)
        return JsonResponse({ 'artisanBidsList':arisanBidsList, 'error': False})
    except Exception as e:
        arisanBidsList = []
        return JsonResponse({ 'artisanBidsList':arisanBidsList, 'error': True, 'message': str(e)})

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
