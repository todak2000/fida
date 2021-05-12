from django.contrib import admin

# Register your models here.
from .models import User, Verification, Ads, Orders, Bids, Escrow, Project_Gig, Transaction, Chat

# Register your models here.
admin.site.register(User)
admin.site.register(Verification)
admin.site.register(Ads)
admin.site.register(Orders)
admin.site.register(Bids)
admin.site.register(Escrow)
admin.site.register(Project_Gig)
admin.site.register(Transaction)
admin.site.register(Chat)