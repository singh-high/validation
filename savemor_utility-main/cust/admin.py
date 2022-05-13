from django.contrib import admin
from .  models  import  User ,UserFunds 

@admin.register(UserFunds)
class Adminuserdata(admin.ModelAdmin):
    list_display = ['payment_status','name','fd_owner','address','mobile','email','amount','payment_id','date_created']


admin.site.register(User)

