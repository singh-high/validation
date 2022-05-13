from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager
# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=50,blank = True, null = True)
    mobile = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=100,default='I love Investments')
    profile_pic = models.ImageField(default='profile/profile.png',upload_to = 'profile')
    email = models.EmailField(unique=True)

    # wallet money
    wallet = models.FloatField(default=0)

    # kyc status
    kyc_status = models.BooleanField(default=False)
    kyc_pending = models.BooleanField(default=False)
    terms = models.BooleanField(default=False)

    # distubutor status
    distibutor_status = models.BooleanField(default=False)
    pin = models.IntegerField(null=True, blank= True)

    # certificate status
    certificate_status = models.CharField(max_length=80,default='Regular')

    # withdraw amount status
    withdraw_amount = models.IntegerField(null=True)
    withdraw_status = models.BooleanField(default=False)

    # premium user fields
    Premium_user = models.BooleanField(default=False)
    premium_Created = models.DateField(null = True)

    # refer for distibutor
    refer_by = models.CharField(null=True,blank=True,max_length=70)



    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []


