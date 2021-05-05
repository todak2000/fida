from django.contrib import admin

# Register your models here.
from .models import User, Verification

# Register your models here.
admin.site.register(User)
admin.site.register(Verification)
# admin.site.register(HubLocation)