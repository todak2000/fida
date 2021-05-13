from django.urls import path

from . import views

urlpatterns = [
    # ONBOARDING
    path('', views.index, name='index'),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("register", views.register_page, name="register"),
    path("verify", views.verify_page, name="verify"),
    path("verify_password", views.verify_password_page, name="verify_password"),
    path("forget_password", views.forget_password_page, name="forget_password"),
    path("reset_password", views.reset_password_page, name="reset_password"),
    # ARTISAN PAGES
    path("artisan_home", views.artisan_home_page, name="artisan_home"),
    path("wallet", views.wallet_page, name="wallet"),
    path("job_details", views.job_details_page, name="job_details"),
    path("gig", views.gig_page, name="gig"),
    path("pending_bid", views.pending_bid_page, name="pending_bid"),
    path("winning_bid", views.winning_bid_page, name="winning_bid"),
    path("pending_gig", views.pending_gig_page, name="pending_gig"),
    path("ongoing_gig", views.ongoing_gig_page, name="ongoing_gig"),
    path("awaiting_gig", views.awaiting_gig_page, name="awaiting_gig"),
    path("approved_gig", views.approved_gig_page, name="approved_gig"),
    path("disputed_gig", views.disputed_gig_page, name="disputed_gig"),
    path("top_up", views.top_up_page, name="top_up"),
    path("withdraw", views.withdraw_page, name="withdraw"),
    path("new_ads", views.new_ads_page, name="new_ads"),
    path("chat", views.chat_page, name="chat"),
    path("individual_chat", views.individual_chat_page, name="individual_chat"),
    path("account", views.account_page, name="account"),
    path("job_view", views.job_view, name="job_view"),
    
    
    path("edit_ads", views.edit_ads_page, name="edit_ads"),
    path("view_ads", views.view_ads_page, name="view_ads"),

    # SHARED APIS
    path("edit_bio_ajax", views.edit_bio_ajax, name="edit_bio_ajax"),
    path("edit_account_ajax", views.edit_account_ajax, name="edit_account_ajax"),
    path("edit_password_ajax", views.edit_password_ajax, name="edit_password_ajax"),
    
    # SHARED PAGES
    path("edit_bio", views.edit_bio_page, name="edit_bio"),
    path("edit_account", views.edit_account_page, name="edit_account"),
    path("edit_password", views.edit_password_page, name="edit_password"),
    # CLIENT PAGES
    path("client_home", views.client_home_page, name="client_home"),
    path("client_wallet", views.client_wallet_page, name="client_wallet"),
    path("ads_details", views.ads_details_page, name="ads_details"),
    path("create_order", views.create_order_page, name="create_order"),
    path("new_order", views.new_order_page, name="new_order"),
    path("project", views.project_page, name="project"),
    path("pending_order", views.pending_order_page, name="pending_order"),
    path("declined_order", views.declined_order_page, name="declined_order"),
    path("pending_project", views.pending_project_page, name="pending_project"),
    path("ongoing_order", views.ongoing_order_page, name="ongoing_order"),
    path("ongoing_project", views.ongoing_project_page, name="ongoing_project"),
    path("approved_project", views.approved_project_page, name="approved_project"),
    path("disputed_project", views.disputed_project_page, name="disputed_project"),
    path("client_top_up", views.client_top_up_page, name="client_top_up"),
    path("client_withdraw", views.client_withdraw_page, name="client_withdraw"),
    path("client_chat", views.client_chat_page, name="client_chat"),
    path("client_individual_chat", views.client_individual_chat_page, name="client_individual_chat"),
    path("client_account", views.client_account_page, name="client_account"),

    # CLIENT APIS
    path("new_order_ajax", views.new_order_api, name="new_order_ajax"),
    path("client_home_ajax", views.client_home_ajax, name="client_home_ajax"),
    path("ads_search", views.ads_search, name="ads_search"),
    path("ads_view", views.ads_view, name="ads_view"),
    
    # ARTISANS APIS
    path("new_ads_ajax", views.new_ads_api, name="new_ads_ajax"),
    path("ads_list_ajax", views.ads_list_ajax, name="ads_list_ajax"),
    path("artisan_home_ajax", views.artisan_home_ajax, name="artisan_home_ajax"),
    path("order_search", views.order_search, name="order_search"),

    # ONBOARDING APIS
    path("login_api", views.login_api, name="login_api"),
    path("register_api", views.register_api, name="register_api"),
    path('activate', views.activate, name='activate'),
    path('resend_code', views.resend_code_api, name='resend_code'),
    path('forgot_code', views.forgot_code_api, name='forgot_code'),
    path('change_password', views.change_password, name='change_password'),
]