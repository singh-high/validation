from django.shortcuts import render
from django.contrib import messages

from certificate.settings import CACHE_TTL
from .forms import UserFdDataForm , UserEditform   
from django.http import HttpResponseRedirect , HttpResponse

from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.views import View
from . models import  UserFunds , User 
from . generater import render_to_pdf , order_id 
from core.models import Wallet
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from . generater import order_id
from datetime import date


# GLOBAL VARIABLES
CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)
tran_id = order_id()



# This is coustmer profile page
def profile(request):
    if request.user.is_authenticated:
        return render(request,'cust/dashboard.html')
    else:
        return HttpResponseRedirect('/login/')





# fd apply form page
def applyFd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserFdDataForm(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['fd_owner']
                uadd = form.cleaned_data['address']
                uemail = form.cleaned_data['email']
                uamount = form.cleaned_data['amount'] 
                umob = form.cleaned_data['mobile']
                Orderid = order_id()
                if request.user.kyc_status == True:
                    user = User.objects.get(email = request.user)
                    if int(request.POST['pin']) == user.pin:
                        if uamount  <= request.user.wallet:
                            deduction = User.objects.get(email = request.user)
                            deduction.wallet  -= uamount
                            order = UserFunds(name = request.user,fd_owner=uname ,address=uadd ,email = uemail,amount = uamount,mobile=umob,order_id = Orderid)
                            order.save()
                            user_amount = Wallet(user = request.user ,amount = uamount,order_id=tran_id,payment_status=True,
                            payment_get_or_send='send',message = 'High Returns')
                            user_amount.save()
                            messages.success(request,'Thanks For Choosing High Returns')
                            return HttpResponseRedirect('/cst/userfdform/')
                        else:
                            messages.warning(request,'Your wallet money is lessthan your investment amount please add money first ')
                            return HttpResponseRedirect('/core/wallet/')
                    else:
                        messages.warning(request,'Incorrect Pin')
                        return HttpResponseRedirect('/core/applyFd/')
                else:
                    messages.warning(request,'KYC is mendatory to access premium feactures')
                    return HttpResponseRedirect('/core/kyc/')
                
        else:
            form = UserFdDataForm()
        context = {'form':form}
        return render(request,'cust/applyfd.html',context) 
    else:
        return HttpResponseRedirect('/login/')


#  customer settings
def setting(request):
    if request.user.is_authenticated:
        return render(request,'cust/setting.html')
    else:
        return HttpResponseRedirect('/login/')




#  customer profile edit
def editprofile(request):
    if request.method == 'POST':
        form = UserEditform( request.POST ,request.FILES ,instance=request.user )
        if form.is_valid():
            form.save()
    else:
        form = UserEditform(instance=request.user)
    context = {'form':form }
    return render(request,'cust/editprofile.html',context)



# shows all fd that user have filled 
def userfdform(request):
    data = UserFunds.objects.filter(name__email = request.user.email)
    context = {'data':data}
    return render(request,'cust/userfdform.html',context)


# shows all fd that user have filled 
def applyForDistributor(request):
    messages.success(request,'Request has been sent for Distributor ')
    return HttpResponseRedirect('/cst/profile/')



    
