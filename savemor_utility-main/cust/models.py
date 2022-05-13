
from django.db import models
from authentication.models import User
# Create your models here.




class UserFunds(models.Model):
    name = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='funds')
    fd_owner = models.CharField(max_length=70 , null=True)
    address = models.CharField(max_length=300 ,null=True)
    address1 = models.CharField(max_length=300 ,null=True)
    email = models.EmailField(max_length=80,null=True)
    mobile = models.IntegerField()
    amount = models.IntegerField()
    order_id  = models.CharField(max_length=70,null=True)
    payment_id  = models.CharField(max_length=70,null=True)
    payment_status  = models.BooleanField(default=True)
    duration = models.CharField(max_length=70,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)









