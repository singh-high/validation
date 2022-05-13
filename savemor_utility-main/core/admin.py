from django.contrib import admin
from . models import Wallet , UserKyc
# Register your models here.


@admin.register(Wallet)
class Adminuserprofile (admin.ModelAdmin):
    list_display = ['user','message','date','amount','transition_id','payment_status']

admin.site.register(UserKyc)
