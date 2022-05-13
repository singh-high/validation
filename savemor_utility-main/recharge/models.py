from django.db import models
from authentication.models import User

# Create your models here.



class Recharge(models.Model):
    recharge_Owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='r_owner')
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    mobile = models.IntegerField(null=True,blank= True)
    mobile_operator = models.CharField(max_length=40,null=True,blank= True)
    customer_id = models.CharField(max_length=70,null=True,blank= True)
    dish_operator = models.CharField(max_length=70,null=True,blank= True)
    electricity = models.CharField(max_length=70, null=True,blank=True)
    electricity_operator = models.CharField(max_length=70, null=True,blank=True)
    amount = models.IntegerField(null=True,blank= True)
    Recharge_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True, null = True)
    
class RechargeHistory(models.Model):
    history_Owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='h_owner')
    type = models.CharField(max_length=70,null=True,blank= True)
    amount = models.IntegerField(null=True,blank= True)
    acc_num = models.CharField(null=True,max_length=70,blank= True)
    operator = models.CharField(max_length=70,null=True,blank= True)
    created = models.DateTimeField(auto_now_add = True, null = True)
    recharge_status = models.CharField(max_length=70,null=True,blank= True)
    error_message = models.CharField(max_length=70,null=True,blank= True)
    transition_id = models.CharField(max_length=70,null=True,blank= True)

    


    