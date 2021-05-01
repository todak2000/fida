from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"onboarding/splashscreen.html") 

def register_page(request):
    return render(request,"onboarding/register.html")

def login_page(request):
    return render(request,"onboarding/login.html") 

def verify_page(request):
    return render(request,"onboarding/verify.html") 

def forget_password_page(request):
    return render(request,"onboarding/forget_password.html") 

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

# def pending_gig_page(request):
#     return render(request,"artisan/gig/pending_gig.html")
#  
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

# def view_ads_page(request):
#     return render(request,"artisan/account/view_ads.html")

# def edit_ads_page(request):
#     return render(request,"artisan/account/edit_ads.html")