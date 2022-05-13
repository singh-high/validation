from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here.




class Wallet(models.Model):
    user = models.ForeignKey(User,null=True,related_name='user', on_delete=models.CASCADE)
    message = models.CharField(null=True,max_length=300)
    date = models.DateTimeField(auto_now_add = True,null=True)
    amount = models.IntegerField()
    transition_id  = models.CharField(max_length=70,null=True,blank=True)
    order_id  = models.CharField(max_length=70, null=True,blank=True)
    payment_status  = models.BooleanField(default=False)
    payment_get_or_send = models.CharField(null = True,max_length=40)



class UserKyc(models.Model):
    relation = models.OneToOneField(User,related_name='name',on_delete=models.CASCADE)
    # document images
    pancard_front = models.ImageField(null = True,blank = True,upload_to = 'document/pancard')
    adharcard_front = models.ImageField(null = True,blank = True,upload_to = 'document/adharcard')
    adharcard_backside = models.ImageField(null = True,blank = True,upload_to = 'document/adharcard')
    user_signature = models.ImageField(null = True,blank = True,upload_to = 'document/signature')
    # document  data
    name = models.CharField(max_length=50,null = True,blank = True)
    pancard = models.CharField(max_length=80,null = True,blank = True)
    adharcard = models.CharField(max_length=80,null = True,blank = True)
    account = models.IntegerField(null = True,blank = True)
    account_verify = models.IntegerField(null = True,blank = True)
    ifsc_code  = models.CharField(max_length=100,null = True,blank = True)




     
  