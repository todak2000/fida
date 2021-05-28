from django.shortcuts import render, redirect

from django.db.models import Sum, Q
from app.models import (User,Verification, Ads, Orders, Bids, Escrow, Project_Gig, Transaction, Chat)
from CustomCode import (password_functions, string_generator, validator)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

from pysendpulse.pysendpulse import PySendPulse
from decouple import config

REST_API_ID = config("REST_API_ID")
REST_API_SECRET = config("REST_API_SECRET")
TOKEN_STORAGE = config("TOKEN_STORAGE")
MEMCACHED_HOST = config("MEMCACHED_HOST")
SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

# Create your views here.

def index(request):
    try:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user_data = User.objects.get(user_id=user_id)
            if user_data.role == "artisan":

                return_data = {
                    "error": False,
                    "profileComplete": user_data.profile_complete,
                    "user_name": f"{user_data.firstname}"
                }
                return render(request,"artisan/home/home.html", return_data) 
            elif user_data.role == "client":
                return_data = {
                    "error": False,
                    "profileComplete": user_data.profile_complete,
                    "user_name": f"{user_data.firstname}"
                }
                return render(request,"client/home/home.html", return_data) 
            else:
                return render(request,"onboarding/splashscreen.html") 
    except Exception as e:
        return_data = {
            "error": True,
            "profileComplete": user_data.profile_complete,
            "user_name": f"{user_data.firstname}",
            "message": "Something went wrong!"
        }
        return render(request,"onboarding/splashscreen.html") 
    
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
            "message": "Something went wrong!"
        }
    return render(request,"artisan/home/home.html", return_data) 

def job_details_page(request):
    if 'user_id' in request.session:
        return render(request,"artisan/home/job_details.html") 
    else:
        return redirect('/login')

def gig_page(request):
    if 'user_id' in request.session:
        return render(request,"artisan/gig/gig.html") 
    else:
        return redirect('/login')
    

# def pending_bid_page(request):
#     if 'user_id' in request.session:
#         return render(request,"artisan/gig/pending_bid.html") 
#     else:
#         return redirect('/login')
    

# def winning_bid_page(request):
#     if 'user_id' in request.session:
#         return render(request,"artisan/gig/winning_bid.html")
#     else:
#         return redirect('/login')
    

# def pending_gig_page(request):
#     return render(request,"artisan/gig/pending_gig.html") 

# def ongoing_gig_page(request):
#     return render(request,"artisan/gig/ongoing_gig.html")

# def awaiting_gig_page(request):
#     return render(request,"artisan/gig/awaiting_gig.html")

# def approved_gig_page(request):
#     return render(request,"artisan/gig/approved_gig.html")

# def disputed_gig_page(request):
#     return render(request,"artisan/gig/disputed_gig.html") 

def wallet_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            user_data = User.objects.get(user_id=user_id)
            userTransactions=Transaction.objects.filter(Q(from_id__icontains=user_id) | Q(to_id__icontains=user_id)).order_by('-date_added')[:20]
            num = len(userTransactions)
            userTransactionsList = []
            for i in range(0,num):
                sender = userTransactions[i].from_id
                to = userTransactions[i].to_id
                date_added = userTransactions[i].date_added
                transaction_type  = userTransactions[i].transaction_type
                amount  = userTransactions[i].amount 
                transaction_message = userTransactions[i].transaction_message
                to_json = {
                    "sender": sender,
                    "transaction_type": transaction_type,
                    "to": to,
                    "transaction_message": transaction_message,
                    "amount": amount,
                    "date_added": date_added,
                }
                userTransactionsList.append(to_json)
            return_data = {
                "error": False,
                "walletBalance": user_data.walletBalance,
                "transaction": userTransactionsList
            }
        except Exception as e:
            return_data = {
                "error": True,
                "message": "Something went wrong!"
            }
        return render(request,"artisan/wallet/wallet.html", return_data)
    else:
        return redirect('/login')

# def top_up_page(request):
#     if 'user_id' in request.session:
#         return render(request,"artisan/wallet/top_up.html")
#     else:
#         return redirect('/login')
    

# def withdraw_page(request):
#     if 'user_id' in request.session:
#         return render(request,"artisan/wallet/withdraw.html")
#     else:
#         return redirect('/login')
    

def new_ads_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def chat_page(request):
    if 'user_id' in request.session:
        user_id = request.session["user_id"]
        try:
            project = Project_Gig.objects.filter(artisan_id=user_id).order_by('-date_added')
            if project:
                return_data = {
                    "error": False,
                    "projects": project,
                    "user": user_id,
                }
            else:
                return_data = {
                    "error": False,
                    "message": "no chat data yet!",
                }
        except Exception as e:
            return_data = {
                "error": True,
                "message": str(e)
            }
        # return JsonResponse({ 'result':return_data})
        return render(request,"artisan/chat/chat.html", return_data)
    else:
        return redirect('/login')

def individual_chat_page(request, id):
    if 'user_id' in request.session:
        user_id = request.session["user_id"]
        project = Project_Gig.objects.get(id=id)
        chat = Chat.objects.filter(project_id=project.id)
        if project and chat:
            return_data = {
                "project_details": project,
                "chat_details":chat,
                "you": user_id,
                "client":project.client_id
            }
        elif project:
            newChat = Chat(from_id=user_id,to_id=project.client_id, message= "Hi!", project_id=project.id, clientRead=False)
            newChat.save()
            chat = Chat.objects.filter(project_id=project.id)
            return_data = {
                "project_details": project,
                "chat_details":chat,
                "you": user_id,
                "client":project.client_id
            }
        return render(request,"artisan/chat/individual_chat.html", return_data)
    else:
        return redirect('/login')

def account_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def edit_bio_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def edit_account_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def edit_password_page(request):
    if 'user_id' in request.session:
        return render(request,"artisan/account/edit_password.html")
    else:
        return redirect('/login')
    

def view_ads_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def edit_ads_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

# client pages api
def client_home_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.get(user_id=user_id)
        try:
            
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
    else:
        return redirect('/login')

def ads_details_page(request):
    if 'user_id' in request.session:
        return render(request,"client/home/ads_details.html") 
    else:
        return redirect('/login')
    

# def create_order_page(request):
#     return render(request,"client/home/create_order.html")

def new_order_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

def project_page(request):
    if 'user_id' in request.session:
        return render(request,"client/project/project.html") 
    else:
        return redirect('/login')
    

# def pending_order_page(request):
#     if 'user_id' in request.session:
#         return render(request,"client/project/pending_order.html") 
#     else:
#         return redirect('/login')
    

# def declined_order_page(request):
#     return render(request,"client/project/declined_order.html")

# def ongoing_project_page(request):
#     return render(request,"client/project/ongoing_project.html")

# def ongoing_order_page(request):
#     return render(request,"client/project/ongoing_order.html")

# def pending_project_page(request):
#     return render(request,"client/project/pending_project.html")

# def approved_project_page(request):
#     return render(request,"client/project/approved_project.html")

# def disputed_project_page(request):
#     return render(request,"client/project/disputed_project.html") 

def client_wallet_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            user_data = User.objects.get(user_id=user_id)
            userTransactions=Transaction.objects.filter(Q(from_id__icontains=user_id) | Q(to_id__icontains=user_id)).order_by('-date_added')[:20]
            num = len(userTransactions)
            userTransactionsList = []
            for i in range(0,num):
                sender = userTransactions[i].from_id
                to = userTransactions[i].to_id
                date_added = userTransactions[i].date_added
                transaction_type  = userTransactions[i].transaction_type
                amount  = userTransactions[i].amount 
                transaction_message = userTransactions[i].transaction_message
                to_json = {
                    "sender": sender,
                    "transaction_type": transaction_type,
                    "to": to,
                    "transaction_message": transaction_message,
                    "amount": amount,
                    "date_added": date_added,
                }
                userTransactionsList.append(to_json)
            return_data = {
                "error": False,
                "walletBalance": user_data.walletBalance,
                "transaction": userTransactionsList
            }
        except Exception as e:
            return_data = {
                "error": True,
                "message": "Something went wrong!"
            }
        return render(request,"client/wallet/wallet.html", return_data)
    else:
        return redirect('/login')

def top_up_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "balance": user_data.walletBalance,
            "email": user_data.email,
            "phone": user_data.user_phone,
            "user_id": user_id,
        }
        return render(request,"client/wallet/top_up.html", return_data)
    else:
        return redirect('/login')
    

def withdraw_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.get(user_id=user_id)
        return_data = {
            "error": False,
            "balance": user_data.walletBalance,
            "bank": user_data.bank_name,
            "accountNo": user_data.account_number, 
            "user_id": user_id,
        }
        return render(request,"client/wallet/withdraw.html", return_data)
    else:
        return redirect('/login')
    

def client_chat_page(request):
    if 'user_id' in request.session:
        user_id = request.session["user_id"]
        try:
            project = Project_Gig.objects.filter(client_id=user_id).order_by('-date_added')
            
            if project:
                return_data = {
                    "error": False,
                    "projects": project,
                    "user": user_id,
                }
            else:
                return_data = {
                    "error": False,
                    "message": "",
                }
        except Exception as e:
            return_data = {
                "error": True,
                "message": str(e)
            }
        return render(request,"client/chat/chat.html", return_data)
    else:
        return redirect('/login')


def client_individual_chat_page(request, id):
    if 'user_id' in request.session:
        user_id = request.session["user_id"]
        project = Project_Gig.objects.get(id=id)
        chat = Chat.objects.filter(project_id=project.id)
        if project and chat:
            return_data = {
                "project_details": project,
                "chat_details":chat,
                "you": user_id,
                "artisan":project.artisan_id
            }
        elif project:
            newChat = Chat(from_id=user_id,to_id=project.artisan_id, message= "Hi!", project_id=project.id)
            newChat.save()
            chat = Chat.objects.filter(project_id=project.id)
            return_data = {
                "project_details": project,
                "chat_details":chat,
                "you": user_id,
                "artisan":project.artisan_id
            }
        return render(request,"client/chat/individual_chat.html", return_data)
    else:
        return redirect('/login')

def client_account_page(request):
    if 'user_id' in request.session:
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
    else:
        return redirect('/login')

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
            "message": str(e)
            # "message": "Sorry, Verification Code is invalid!"
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
                    request.session['user_id'] = user_data.user_id
                    request.session['email'] = user_data.email
                    is_valid_password = password_functions.check_password_match(password,user_data.user_password)
                    isVerified= Verification.objects.get(user_id__user_id=user_data.user_id).isVerified
                    if is_valid_password and isVerified:
                        # request.session['user_id'] = user_data.user_id
                        # request.session['email'] = user_data.email
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
        # duration = request.data.get('duration',None)
        state = request.data.get('state',None)
        location = request.data.get('location',None)
        min_budget = request.data.get('min_budget',None)
        max_budget = request.data.get('max_budget',None)
        field = [title, description, state, location, min_budget, max_budget]
        user_data = User.objects.get(user_id=user_id)
        if not None in field and not "" in field:
            if int(max_budget) <= 0:
                return_data = {
                "error":True,
                "message": "You can't make an order with Zero budget!"
            }
            elif user_data.walletBalance >= int(max_budget):
                # newBalance = user_data.walletBalance - int(max_budget)
                # user_data.walletBalance =newBalance
                # user_data.save()
                # newTransaction = Transaction(from_id=user_id, to_id="Escrow", transaction_type="Debit", transaction_message="Payment for Work", amount=max_budget)
                # newTransaction.save()
                # newEscrow = Escrow(client_id=user_id, initial_fees=max_budget, )
                # newEscrow.save()
                newOrder = Orders(title=title,description=description,min_budget=min_budget,max_budget=max_budget,location=location,state=state,client_id=user_data, orderStatus="bidding")
                newOrder.save()
                return_data = {
                    "error": False,
                    "message": "Order Created Successfully!"
                }
            else:
               return_data = {
                "error":True,
                "message": "You have insufficient Balance. Kindly top up atleast &#8358;"+max_budget+" to let this order go through. Thanks"
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
    user_id = request.session['user_id']
    try:
        # orderData = Orders.objects.exclude(orderStatus__in=['pending', 'completed', 'accepted']).order_by('-date_added')[:20]
        orderData = Orders.objects.filter(orderStatus="bidding").order_by('-date_added')[:20]
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
    user_id = request.session['user_id']
    jobOrder = Orders.objects.get(id=job_id)
    try:
        isBidded = Bids.objects.filter(bidder=user_id, order_id__id =job_id)
        if isBidded:
            return JsonResponse({  'error': True, 'jobView':"no view",  'message':"You have bidded for this Order."})
        else:
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
    try:
        adsOrder = Ads.objects.get(id=ads_id)
        total_views = adsOrder.no_of_views + 1
        adsOrder.no_of_views = total_views
        adsOrder.save()
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
    userBalance = user.walletBalance
    try:
        field = [ads_fee]
        if not None in field and not "" in field:
            if userBalance >= int(ads_fee):
                ads = Ads.objects.get(id=ads_id)
                newOrder = Orders(client_id=user, title=ads_title, description=ads_description, min_budget=ads_min_budget, max_budget=ads_max_budget, location=ads_location, state=ads_state, service_fee=ads_fee, pitch=ads_pitch, noOfBidders = 1,winner_id=ads.artisan_id.user_id, orderStatus="pending", from_ads=True )
                newOrder.save()
                
                onlyBid = Bids(order_id=newOrder, bidder=ads.artisan_id.user_id, service_fee=ads_fee, pitch=ads_pitch)
                onlyBid.save()
                # Send mail using SMTP
                mail_subject = ads.artisan_id.firstname+'! You got a new Order from your Ad'
                email4 = {
                    'subject': mail_subject,
                    'html': '<h4>Hello, '+ads.artisan_id.firstname+'!</h4><p> You just won a bid from your ads. Kindly check via the Fida App to accept or decline the offer</p>',
                    'text': 'Hello, '+ads.artisan_id.firstname+'!\nYou just won a bid from your ads. Kindly check via the Fida App to accept or decline the offer',
                    'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                    'to': [
                        {'name': ads.artisan_id.firstname, 'email': ads.artisan_id.email}
                        # {'name': ads.artisan_id.firstname, 'email': "todak2000@gmail.com"}
                    ]
                }
                sentMail4 = SPApiProxy.smtp_send_mail(email4)
            
                if newOrder and onlyBid and sentMail4:
                    removeUserNotification = User.objects.get(user_id=user_id)
                    removeUserNotification.notification = False
                    removeUserNotification.save() 

                    addUserNotification = User.objects.get(user_id=ads.artisan_id.user_id)
                    addUserNotification.notification = True
                    addUserNotification.save() 
                    return JsonResponse({ 'message':'Order successfully sent. Kindly await Artisan response', 'error': False})
                else:
                    return JsonResponse({  'error': True, 'message':"Sorry, an error occured"})
            else:
                return JsonResponse({  'error': True, 'message':"Sorry, you have insufficient balance. Kindly top with atleast &#8358;"+ads_fee+" in order to create this order. Thanks"})
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
        # client.notification = False
        # client.save()
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
            
            total_bidders = order.noOfBidders + 1
            order.noOfBidders = total_bidders
            order.save()

            client = User.objects.get(user_id=order.client_id.user_id)
            client.notification = True
            client.save()

            newBid = Bids(order_id=order, bidder=user_id, service_fee=job_fee, pitch=job_pitch)
            newBid.save()
            # Send mail using SMTP
            mail_subject = order.client_id.firstname+'! You got a new bid for Order-'+job_id
            email = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+order.client_id.firstname+'!</h4><p> You have a new bidder for your Job offer. Kindly check via the Fida App</p>',
                'text': 'Hello, '+order.client_id.firstname+'!\nYou have a new bidder for your Job offer. Kindly check via the Fida App',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': order.client_id.firstname, 'email': order.client_id.email}
                    # {'name': order.client_id.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail = SPApiProxy.smtp_send_mail(email)
            if newBid and sentMail:
                return JsonResponse({ 'message':'Bid was successful', 'error': False})
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
        arisanBids = Bids.objects.filter(bidder=user_id, declinedOffer=False).order_by('-date_added')[:20] #| Bids.objects.filter(order_id__winner_id=user_id).order_by('-date_added')
        num = len(arisanBids)
        arisanBidsList = []
        for i in range(0,num):
            bid_id = arisanBids[i].id
            title = arisanBids[i].order_id.title 
            noOfBidders = arisanBids[i].order_id.noOfBidders
            fromAds = arisanBids[i].order_id.from_ads
            # if arisanBids[i].order_id.orderStatus == "pending" or arisanBids[i].order_id.orderStatus == "bidding":
            orderStatus  = arisanBids[i].order_id.orderStatus 
            winner_id = arisanBids[i].order_id.winner_id
            to_json = {
                "bid_id": bid_id,
                "title": title,
                "noOfBidders": noOfBidders,
                "orderStatus": orderStatus,
                "winner_id": winner_id,
                "fromAds": fromAds,
                "user_id": user_id,
            }
            arisanBidsList.append(to_json)
            # else:
            #     arisanBidsList = []
        return JsonResponse({ 'artisanBidsList':arisanBidsList, 'error': False})
    except Exception as e:
        arisanBidsList = []
        return JsonResponse({ 'artisanBidsList':arisanBidsList, 'error': True, 'message': str(e)})

# Artisan bid page - pending order details to accept or delcine order
@api_view(["POST"])
def pending_order_modal(request):
    bid_id = request.POST["id"]
    pendingBid = Bids.objects.get(id=bid_id)
    try:
        if pendingBid:
            bid_id = pendingBid.id
            title = pendingBid.order_id.title 
            description = pendingBid.order_id.description
            order_id= pendingBid.order_id.id
            location = pendingBid.order_id.location
            state = pendingBid.order_id.state
            max_budget = pendingBid.order_id.max_budget
            service_fee= pendingBid.service_fee
            to_json = {
                "bid_id": bid_id,
                "title": title,
                "state": state,
                "description": description,
                "location": location,
                "order_id": order_id,
                "budget": max_budget,
                "service_fee": service_fee,
            }
            removeUserNotification = User.objects.get(user_id=pendingBid.bidder)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=pendingBid.order_id.client_id.user_id)
            addUserNotification.notification = True
            addUserNotification.save() 
            return JsonResponse({ 'bidView':to_json, 'error': False})
        else:
            return JsonResponse({  'error': False, 'message':"Sorry, Job Order no longer available!"})

    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Artisan bid page - bidable order details 
@api_view(["POST"])
def bid_list(request):
    order_id = request.POST["id"]
    try:
        order = Orders.objects.get(id=order_id)
        title = order.title 
        bids = Bids.objects.filter(order_id__id=order_id).order_by('-date_added')
        num = len(bids)
        bidList = []
        for i in range(0,num):
            order_id = order_id
            # title = bids[i].order_id.title 
            bidder = User.objects.get(user_id =bids[i].bidder)
            bidder_name = bidder.firstname+ " "+bidder.lastname
            bidder_rating = bidder.ratings
            bidder_id = bidder.user_id
            bidder_state = bidder.user_state
            service_fee = bids[i].service_fee 
            declined = bids[i].declinedOffer
            pitch = bids[i].pitch
            to_json = {
                "bid_id": order_id,
                "bidder": bidder_name,
                "bidder_id": bidder_id,
                "ratings": bidder_rating,
                "state": bidder_state,
                "service_fee": service_fee,
                "pitch": pitch,
                "decline_offer": declined, 
            }
            bidList.append(to_json)
        return JsonResponse({ 'bidList':bidList, "title": title, 'error': False})
    except Exception as e:
        bidList = []
        return JsonResponse({ 'bidList':bidList, 'error': True, 'message': str(e)})

# Artisan accept bid
@api_view(["POST"])
def artisan_accept_bid_api(request):
    user_id = request.session["user_id"]
    order_id = request.POST["job_id"]
    try:
        acceptedOrder = Orders.objects.get(id=order_id)
        acceptedOrder.orderStatus = "accepted"
        acceptedOrder.winner_accept = True
        acceptedOrder.save()
        newProject = Project_Gig(order_id=order_id,client_id=acceptedOrder.client_id.user_id, artisan_id=acceptedOrder.winner_id, project_title=acceptedOrder.title, canChat=True, projectStatus="ongoing" )
        newProject.save()
        client_data = User.objects.get(user_id=acceptedOrder.client_id.user_id)
        newBalance = int(client_data.walletBalance) - int(acceptedOrder.service_fee)
        client_data.walletBalance =newBalance
        client_data.save()
        newTransaction = Transaction(from_id=client_data.user_id, to_id="Escrow", transaction_type="Debit", transaction_message="Payment for Order "+order_id, amount=acceptedOrder.service_fee)
        newTransaction.save()
        newEscrow = Escrow(client_id=client_data.user_id, artisan_id=user_id,fees_agreed= acceptedOrder.service_fee, order_id=order_id)
        newEscrow.save()
        # Send mail using SMTP
        mail_subject = client_data.firstname+'! Acceptance update for Order-'+order_id
        email3 = {
            'subject': mail_subject,
            'html': '<h4>Hello, '+client_data.firstname+'!</h4><p> Kindly be informed the Artisan has accepted your Job Offer. Kindly reach out via the chat to keep tab on the job completion. Be also informed, NGN '+acceptedOrder.service_fee+' has been deducted from your wallet into Fida Escrow account. Upon confirmation of job completion, the Artisan would be paid. Thank you </p>',
            'text': 'Hello, '+client_data.firstname+'!\nKindly be informed the Artisan has accepted your Job Offer. Kindly reach out via the chat to keep tab on the job completion. Be also informed, NGN '+acceptedOrder.service_fee+' has been deducted from your wallet into Fida Escrow account. Upon confirmation of job completion, the Artisan would be paid. Thank you ',
            'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
            'to': [
                {'name': client_data.firstname, 'email': client_data.email}
                # {'name': client_data.firstname, 'email': "todak2000@gmail.com"}
            ]
        }
        sentMail3 = SPApiProxy.smtp_send_mail(email3)
        if sentMail3:
            return JsonResponse({ 'message': 'Lets get you started already! you can reach out to the Client via the chat if you need any details.', 'error': False})
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Artisan  decline bid
@api_view(["POST"])
def artisan_decline_bid_api(request):
    order_id = request.POST["job_id"]
    user_id = request.session['user_id']
    try:
        freeOrder = Orders.objects.get(id=order_id)
        if freeOrder.from_ads == True:
            freeOrder.winner_id = ""
            freeOrder.orderStatus = "declined"
            freeOrder.save()
            # Send mail using SMTP
            mail_subject = freeOrder.client_id.firstname+'! Sorry, Artisan Declined your Offer'
            email7 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+freeOrder.client_id.firstname+'!</h4><p> We regret to inform you, the Artisan rejected your offer for the Ads you created Order - '+order_id+' from. However, you could rather create a fresh order and accept bids to proceed with the Job.</p>',
                'text': 'Hello, '+freeOrder.client_id.firstname+'!\nWe regret to inform you, the Artisan rejected your offer for the Ads you created Order - '+order_id+' from. However, you could rather create a fresh order and accept bids to proceed with the Job.',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': freeOrder.client_id.firstname, 'email': freeOrder.client_id.email}
                    # {'name': freeOrder.client_id.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail7 = SPApiProxy.smtp_send_mail(email7)
            removeUserNotification = User.objects.get(user_id=user_id)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=freeOrder.client_id.user_id)
            addUserNotification.notification = True
            addUserNotification.save() 
        else:
            freeOrder.winner_id = ""
            freeOrder.orderStatus = "bidding"
            # newNoOfBidders = freeOrder.noOfBidders - 1
            # freeOrder.noOfBidders = newNoOfBidders
            freeOrder.save()
            removeBid = Bids.objects.get(bidder=user_id, order_id=order_id )
            removeBid.declinedOffer = True
            removeBid.save()
            # Send mail using SMTP
            mail_subject = freeOrder.client_id.firstname+'! Sorry, Artisan Declined your Offer'
            email7 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+freeOrder.client_id.firstname+'!</h4><p> We regret to inform you, the Artisan rejected your offer for the Ads you created Order - '+order_id+' from. However, you could select another Bid from the list of bids available for the Order to proceed with the Job.</p>',
                'text': 'Hello, '+freeOrder.client_id.firstname+'!\nWe regret to inform you, the Artisan rejected your offer for the Ads you created Order - '+order_id+' from. However, you could select another Bid from the list of bids available for the Order to proceed with the Job.',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': freeOrder.client_id.firstname, 'email': freeOrder.client_id.email}
                    # {'name': freeOrder.client_id.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail7 = SPApiProxy.smtp_send_mail(email7)
            removeUserNotification = User.objects.get(user_id=user_id)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=freeOrder.client_id.user_id)
            addUserNotification.notification = True
            addUserNotification.save()
        if freeOrder and sentMail7 or removeBid:
            return JsonResponse({ 'message': 'Done! Thank you', 'error': False})
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# client acceot bidder api initial
@api_view(["POST"])
def client_accept_bidder_confirmation(request):
    bid_id = request.POST["bid_id"]
    bidder_id = request.POST['bidder_id']
    bidder = request.POST['bidder']
    try:
        checkOrder = Orders.objects.get(id=bid_id)
        if checkOrder:
            to_json = {
                "bid_id": bid_id,
                "bidder": bidder,
                "bidder_id": bidder_id,
            }
            return JsonResponse({ 'bidder': to_json, 'message': 'Done! Thank you', 'error': False})
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Artisan accept bid
@api_view(["POST"])
def client_accept_bid_api(request):
    user_id = request.session["user_id"]
    bidder_name = request.POST["bidder_name"]
    order_id= request.POST["order_id"]
    bidder_id = request.POST["bidder_id"]
    try:
        acceptedOrder = Orders.objects.get(id=order_id)
        bid = Bids.objects.get(order_id=order_id, bidder=bidder_id)
        acceptedOrder.orderStatus = "pending"
        acceptedOrder.winner_id  = bidder_id
        acceptedOrder.service_fee = bid.service_fee
        acceptedOrder.save()
        bidder_data = User.objects.get(user_id=bidder_id)

        # Send mail using SMTP
        mail_subject = bidder_name+'! You won the bid for Order-'+order_id
        email = {
            'subject': mail_subject,
            'html': '<h4>Hello, '+bidder_name+'!</h4><p> You have won the bid for your Job offer with Order No '+order_id+'. Kindly check via the Fida App to accept or decline the offer immediately. Congrats once again!</p>',
            'text': 'Hello, '+bidder_name+'!\nYou have won the bid for your Job offer with Order No '+order_id+'. Kindly check via the Fida App to accept or decline the offer immediately. Congrats once again!',
            'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
            'to': [
                {'name': bidder_name, 'email': bidder_data.email}
                # {'name': bidder_name, 'email': "todak2000@gmail.com"}
            ]
        }
        sentMail2 = SPApiProxy.smtp_send_mail(email)
        
        if acceptedOrder and sentMail2:
            return JsonResponse({ 'message': 'Done! Kindly reach out to the Artisan via the chat got get startd.', 'error': False})
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# Bids section ajax page get bids/gigs
@api_view(["GET"])
def artisan_gig_main_ajax(request):
    user_id = request.session['user_id']
    try:
        arisanGigs = Project_Gig.objects.filter(artisan_id=user_id).order_by('-date_added')[:20]
        num = len(arisanGigs)
        arisanGigsList = []
        for i in range(0,num):
            project_id = arisanGigs[i].id
            title = arisanGigs[i].project_title
            is_completed = arisanGigs[i].isCompleted 
            projectStatus  = arisanGigs[i].projectStatus
            artisan_id = arisanGigs[i].artisan_id
            to_json = {
                "project_id": project_id,
                "title": title,
                "isCompleted": is_completed,
                "projectStatus": projectStatus,
                "artisan_id": artisan_id,
                "user_id": user_id,
            }
            arisanGigsList.append(to_json)
        return JsonResponse({ 'artisanGigsList':arisanGigsList, 'error': False})
    except Exception as e:
        arisanGigsList = []
        return JsonResponse({ 'artisanGigsList':arisanGigsList, 'error': True, 'message': str(e)})

# Bids section ajax page get bids/gigs
@api_view(["GET"])
def client_project_main_ajax(request):
    user_id = request.session['user_id']
    try:
        clientProjects = Project_Gig.objects.filter(client_id=user_id).order_by('-date_added')[:20]
        num = len(clientProjects)
        clientProjectsList = []
        for i in range(0,num):
            project_id = clientProjects[i].id
            title = clientProjects[i].project_title
            projectStatus  = clientProjects[i].projectStatus
            artisan_id = clientProjects[i].artisan_id
            client_id = clientProjects[i].client_id
            to_json = {
                "project_id": project_id,
                "title": title,
                "projectStatus": projectStatus,
                "artisan_id": artisan_id,
                "client_id": client_id,
                "user_id": user_id,
            }
            clientProjectsList.append(to_json)
        return JsonResponse({ 'clientProjectsList':clientProjectsList, 'error': False})
    except Exception as e:
        clientProjectsList = []
        return JsonResponse({ 'clientProjectsList':clientProjectsList, 'error': True, 'message': str(e)})

# Artisan bid page - pending order details to accept or delcine order
@api_view(["POST"])
def ongoing_project_modal(request):
    project_id = request.POST["id"]
    ongoingProject = Project_Gig.objects.get(id=project_id)
    projectOrder = Orders.objects.get(id=ongoingProject.order_id)
    try:
        if ongoingProject and projectOrder:
            project_id = ongoingProject.id
            title = ongoingProject.project_title 
            description = projectOrder.description
            order_id = ongoingProject.order_id
            location = projectOrder.location
            state = projectOrder.state
            service_fee= projectOrder.service_fee
            to_json = {
                "project_id": project_id,
                "order_id": order_id,
                "title": title,
                "state": state,
                "description": description,
                "location": location,
                "service_fee": service_fee,
            }
            removeUserNotification = User.objects.get(user_id=projectOrder.client_id.user_id)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=ongoingProject.artisan_id)
            addUserNotification.notification = True
            addUserNotification.save() 
            return JsonResponse({ 'projectItem':to_json, 'error': False})
        else:
            return JsonResponse({  'error': False, 'message':"Sorry, Project is no longer available!"})

    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# client end project officially
@api_view(["POST"])
def end_project_api(request):
    user_id = request.session["user_id"]
    project_id = request.POST["project_id"]
    order_id = request.POST["order_id"]
    project_status = request.POST["project_status"]  # checked reply from client
    project_rating = request.POST["project_rating"]
    try:
        endProject= Project_Gig.objects.get(id=project_id)
        projectOrder = Orders.objects.get(id=order_id)
        artisan = User.objects.get(user_id=endProject.artisan_id)
        updateEscrow = Escrow.objects.get(order_id=order_id)
        newRatings = (artisan.ratings + int(project_rating))/2
        updateEscrow.project_id = project_id
        fidaCommission = 0.20 * int(projectOrder.service_fee)
        commissionedBalance = int(projectOrder.service_fee) - fidaCommission

        # if endProject and projectOrder:
        if project_status == "completed":
            endProject.endProject = True
            message = "Thank you!"
            isSatisfied = True
            endProject.projectStatus = project_status
            endProject.save()

            artisan.ratings = newRatings
            newBalance = artisan.walletBalance + commissionedBalance
            artisan.walletBalance =newBalance
            artisan.save()

            newTransaction = Transaction(from_id="Escrow", to_id=endProject.artisan_id, transaction_type="Credit", transaction_message="Payment for Order "+project_id, amount=commissionedBalance, project_id=project_id,projectCompleted=True)
            newTransaction.save()

            updateEscrow.commission = fidaCommission
            updateEscrow.isPaid = True
            updateEscrow.save()
            # Send mail using SMTP
            mail_subject = artisan.firstname+'! Payment updates for Project-'+project_id
            email6 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+artisan.firstname+'!</h4><p> Congratulations, you just got paid for your diligent work (Order - '+order_id+'). Kindly check via the Fida App to confirm or withdraw whenever you are ready. More jobs! more money!</p>',
                'text': 'Hello, '+artisan.firstname+'!\nYou have a new bidder for your Job offer. Kindly check via the Fida App',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': artisan.firstname, 'email': artisan.email}
                    # {'name': artisan.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail6 = SPApiProxy.smtp_send_mail(email6)
        else :
            message = "We are truly sorry about your experience! We promise to look into the issue immediately. You will be redirected within seconds"
            isSatisfied = False
            artisan.ratings = newRatings
            artisan.save()

            updateEscrow.dispute = True
            updateEscrow.save()

            endProject.projectStatus = project_status
            endProject.endProject = True
            endProject.save()
            
            # Send mail using SMTP
            mail_subject = artisan.firstname+'! Payment updates for Project-'+project_id
            email6 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+artisan.firstname+'!</h4><p> We regret to inform you that payment for your work would be processed yet. This is because the client did not confirm completion of your work in positive light. The Project with project id - '+project_id+' was tagged '+project_status+'. Kindly reach out the client via the chat or the Fida admin to resolve the issue immediately or call 09088776666666.</p>',
                'text': 'Hello, '+artisan.firstname+'!\nWe regret to inform you that payment for your work would be processed yet. This is because the client did not confirm completion of your work in positive light. The Project with project id - '+project_id+' was tagged '+project_status+'. Kindly reach out the client via the chat or the Fida admin to resolve the issue immediately or call 09088776666666.',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': artisan.firstname, 'email': artisan.email}
                    # {'name': artisan.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail6 = SPApiProxy.smtp_send_mail(email6)
            
        if endProject and updateEscrow and artisan and sentMail6:
            removeUserNotification = User.objects.get(user_id=endProject.client_id)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=endProject.artisan_id)
            addUserNotification.notification = True
            addUserNotification.save() 
            return JsonResponse({ 'message': message, 'error': False, 'satisfied': isSatisfied, 'projectStatus': endProject.projectStatus})
        else:
            return JsonResponse({  'error': False, 'message':"Sorry, An error occured!"})

    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# client end project officially
@api_view(["POST"])
def end_gig_api(request):
    project_id = request.POST["gig_id"]
    order_id = request.POST["order_id"]
    is_completed = request.POST["is_completed"]  # checked reply from client
    endProject= Project_Gig.objects.get(id=project_id)
    # projectOrder = Orders.objects.get(id=order_id)
    updateEscrow = Escrow.objects.get(order_id=order_id)
    client  = User.objects.get(user_id=endProject.client_id)
    try:
        if is_completed == "completed":
            endProject.isCompleted = True
            endProject.save()
            message = "Weldone!"
            # Send mail using SMTP
            mail_subject = client.firstname+'! Job Completion updates for Project-'+project_id
            email9 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+client.firstname+'!</h4><p> You job order with (Order - '+order_id+') has been certified completed by the Artisan. Kindly confirm you are satisfied or otherwise with the work via the Fida App by clicking on end project. This is to enable the Artisan get paid immediately from the Escrow account if you confirm or allow Fida representative to attend to the issues you might concerning the job.</p>',
                'text': 'Hello, '+client.firstname+'!\nYou job order with (Order - '+order_id+') has been certified completed by the Artisan. Kindly confirm you are satisfied or otherwise with the work via the Fida App by clicking on end project. This is to enable the Artisan get paid immediately from the Escrow account if you confirm or allow Fida representative to attend to the issues you might concerning the job.',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    # {'name': client.firstname, 'email': order.client_id.email}
                    {'name': client.firstname, 'email': client.email}
                    # {'name': client.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail9 = SPApiProxy.smtp_send_mail(email9)
        else:
            endProject.isCompleted = False
            endProject.save()
            message = "We trust you will do better next time. You will be redirected in seconds"

            newBalance = client.walletBalance + float(updateEscrow.fees_agreed)
            client.walletBalance =newBalance
            client.save()

            newTransaction = Transaction(from_id="Escrow", to_id=client.user_id, transaction_type="Credit", transaction_message="Refund for Order"+project_id, amount=float(updateEscrow.fees_agreed), project_id=project_id)
            newTransaction.save()

            updateEscrow.commission = 0
            updateEscrow.save()

            # Send mail using SMTP
            mail_subject = client.firstname+'! Job Completion updates for Project-'+project_id
            email9 = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+client.firstname+'!</h4><p> We regret to inform you that the Artisan could not complete the job for (Order - '+order_id+'). We sincerely apologise and kindly ask that you create a new Job order to get the job done. However, be rest assured, your fund - &#8358;'+updateEscrow.fees_agreed+' has been returned to your wallet.</p>',
                'text': 'Hello, '+client.firstname+'!\nYou job order with (Order - '+order_id+') has been certified completed by the Artisan. Kindly confirm you are satisfied or otherwise with the work via the Fida App by clicking on end project. This is to enable the Artisan get paid immediately from the Escrow account if you confirm or allow Fida representative to attend to the issues you might concerning the job.',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': client.firstname, 'email': client.email}
                    # {'name': client.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail9 = SPApiProxy.smtp_send_mail(email9)
        if endProject and sentMail9 or updateEscrow or newTransaction or client:
            removeUserNotification = User.objects.get(user_id=endProject.artisan_id)
            removeUserNotification.notification = False
            removeUserNotification.save() 

            addUserNotification = User.objects.get(user_id=endProject.client_id)
            addUserNotification.notification = True
            addUserNotification.save()  
            return JsonResponse({ 'message': message, 'error': False, 'satisfied': endProject.isCompleted})
    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})


@api_view(["GET"])
def get_notification(request):
    user_id = request.session["user_id"]
    try:
        user_data = User.objects.get(user_id=user_id)
        if user_data.notification == True:
            return JsonResponse({ 'notify':True, 'error': False})
        else:
            return JsonResponse({ 'notify':False, 'error': False})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

@api_view(["GET"])
def get_artisan_chat(request):
    user_id = request.session["user_id"]
    project_id = request.POST["project_id"]
    try:
        chatHistory = Chat.objects.get(project_id=project_id)
        if chatHistory:
            return JsonResponse({ 'ArtisanChat':chatHistory, 'error': False})
        else:
            return JsonResponse({ 'ArtisanChat': "no chat yet!", 'error': False})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

@api_view(["POST"])
def artisan_send_message(request):
    user_id = request.session["user_id"]
    project_id = request.POST["project_id"]
    newMessage = request.POST["message"]
    sender = request.POST["sender"]
    reciever = request.POST["reciever"]
    try:
        newChat = Chat(from_id=sender, to_id=reciever,project_id=project_id, message=newMessage, clientRead=False)
        newChat.save()
        chatHistory = Chat.objects.filter(project_id=project_id)
        client = User.objects.get(user_id=reciever)
        artisan = User.objects.get(user_id=sender)
        project = Project_Gig.objects.get(id=project_id)
        if newChat and chatHistory:
            # Send mail using SMTP
            mail_subject = client.firstname+'! You got a new message for Project-'+project_id
            email = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+client.firstname+'!</h4><p> '+artisan.firstname+' send you a message for the Project: '+project.project_title+'. Kindly check via the Fida App to reply immmediately</p>',
                'text': 'Hello, '+client.firstname+'!\n'+artisan.firstname+' send you a message for the Project: '+project.project_title+'. Kindly check via the Fida App to reply immmediately',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': client.firstname, 'email': client.email}
                    # {'name': client.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail = SPApiProxy.smtp_send_mail(email)
            num = len(chatHistory)
            chatHistoryList = []
            for i in range(0,num):
                project_id = chatHistory[i].project_id
                from_id = chatHistory[i].from_id
                to_id  = chatHistory[i].to_id
                message = chatHistory[i].message
                date_added = chatHistory[i].date_added
                to_json = {
                    "project_id": project_id,
                    "from_id": from_id,
                    "to_id": to_id,
                    "message": message,
                    "date_added": date_added,
                    "artisan": sender,
                }
                chatHistoryList.append(to_json)
            return JsonResponse({ 'chatHistoryList':chatHistoryList, 'error': False})
        else:
            return JsonResponse({ 'chatHistoryList': "no chat yet!", 'error': False})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

@api_view(["POST"])
def client_send_message(request):
    user_id = request.session["user_id"]
    project_id = request.POST["project_id"]
    newMessage = request.POST["message"]
    sender = request.POST["sender"]
    reciever = request.POST["reciever"]
    try:
        newChat = Chat(from_id=sender, to_id=reciever,project_id=project_id, message=newMessage,artisanRead=False)
        newChat.save()
        chatHistory = Chat.objects.filter(project_id=project_id)
        client = User.objects.get(user_id=sender)
        artisan = User.objects.get(user_id=reciever)
        project = Project_Gig.objects.get(id=project_id)
        if newChat and chatHistory:
            # Send mail using SMTP
            mail_subject = artisan.firstname+'! You got a new message for Project-'+project_id
            email = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+artisan.firstname+'!</h4><p> '+client.firstname+' send you a message for the Project: '+project.project_title+'. Kindly check via the Fida App to reply immmediately</p>',
                'text': 'Hello, '+artisan.firstname+'!\n'+client.firstname+' send you a message for the Project: '+project.project_title+'. Kindly check via the Fida App to reply immmediately',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': artisan.firstname, 'email': artisan.email}
                    # {'name': artisan.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail = SPApiProxy.smtp_send_mail(email)
            num = len(chatHistory)
            chatHistoryList = []
            for i in range(0,num):
                project_id = chatHistory[i].project_id
                from_id = chatHistory[i].from_id
                to_id  = chatHistory[i].to_id
                message = chatHistory[i].message
                date_added = chatHistory[i].date_added
                to_json = {
                    "project_id": project_id,
                    "from_id": from_id,
                    "to_id": to_id,
                    "message": message,
                    "date_added": date_added,
                    "client": sender,
                }
                chatHistoryList.append(to_json)
            return JsonResponse({ 'chatHistoryList':chatHistoryList, 'error': False})
        else:
            return JsonResponse({ 'chatHistoryList': "no chat yet!", 'error': False})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

@api_view(["POST"])
def top_up_api(request):
    user_id = request.POST["user_id"]
    amount = request.POST["amount"]
    try: 
        user_data = User.objects.get(user_id=user_id)
        newBalance = user_data.walletBalance + float(amount)
        user_data.walletBalance = newBalance
        user_data.save()

        newTransaction = Transaction(from_id="Fida", to_id=user_id, transaction_type="Credit", transaction_message="Top-up - Paystack", amount=float(amount))
        newTransaction.save()
        if user_data and newTransaction:
            # Send mail using SMTP
            mail_subject = user_data.firstname+'! Fida Top-up Update'
            email = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+user_data.firstname+'!</h4><p> You payment of N'+amount+ ' to your Fida wallet was successful</p>',
                'text': 'Hello, '+user_data.firstname+'!\n You payment of N'+amount+ ' to your Fida wallet was successful',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': user_data.firstname, 'email': user_data.email}
                    # {'name': user_data.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail = SPApiProxy.smtp_send_mail(email)
            return_data = {
                "error": False,
                "role": user_data.role,
            }
            return JsonResponse({ 'data':return_data, 'error': False})
        else:
            return JsonResponse({ 'message': "something went wrong!", 'error': True})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})

# widthrawal api
@api_view(["POST"])
def withdrawal_api(request):
    user_id = request.session['user_id']
    amount = request.POST["amount"]
    try: 
        user_data = User.objects.get(user_id=user_id)
        newBalance = user_data.walletBalance - float(amount)
        user_data.walletBalance = newBalance
        user_data.save()

        newTransaction = Transaction(from_id=user_id, to_id="Fida", transaction_type="Debit", transaction_message="Withdrawal - Cashout", amount=float(amount))
        newTransaction.save()
        if user_data and newTransaction:
            # Send mail using SMTP
            mail_subject = user_data.firstname+'! Fida Top-up Update'
            email = {
                'subject': mail_subject,
                'html': '<h4>Hello, '+user_data.firstname+'!</h4><p> Your Withdrawal request for N'+amount+ ' is being processed and would be sent to your account within 24 hours. Thanks</p>',
                'text': 'Hello, '+user_data.firstname+'!\n You payment of N'+amount+ ' to your Fida wallet was successful',
                'from': {'name': 'Fida Synergy', 'email': 'donotreply@wastecoin.co'},
                'to': [
                    {'name': user_data.firstname, 'email': user_data.email}
                    # {'name': user_data.firstname, 'email': "todak2000@gmail.com"}
                ]
            }
            sentMail = SPApiProxy.smtp_send_mail(email)
            return_data = {
                "error": False,
                "role": user_data.role,
            }
            return JsonResponse({ 'data':return_data, 'error': False})
        else:
            return JsonResponse({ 'message': "something went wrong!", 'error': True})


    except Exception as e:
        return JsonResponse({ 'error': True, 'message': str(e)})