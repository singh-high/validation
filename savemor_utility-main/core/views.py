from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from authentication.models import User
from . models import Wallet , UserKyc 
from . forms  import WalletForm , UserKycForm , WithdrawForm
import razorpay
from cust.generater import order_id
# Create your views here.



# GLOBAL VARIABLES
tran_id = order_id()


# wallet money 
def wallet(request):
    print('--------',request.user)
    history = Wallet.objects.filter(user__email = request.user).exclude(payment_status = False).order_by('-date')[:10]
    balance = request.user.wallet     
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            uamo = int(form.cleaned_data['amount'] * 100)
            uamount = form.cleaned_data['amount'] 
            umsg = form.cleaned_data['message']
            client =razorpay.Client(auth=('rzp_test_Vq2wtgCcPJuQaB','S78FPRPrEB8KPHQkHYWqMlEz'))
            payment = client.order.create({'amount':uamo,'currency':'INR','payment_capture':'1'})
            user_amount = Wallet(user = request.user ,message = 'Razorpay'+umsg,amount = uamount,transition_id=payment['id'],
            order_id=tran_id,payment_get_or_send='get',)
            user_amount.save()
            context = {'payment':payment,'form':form,'balance':balance,'history':history}
            return render(request,'core/wallet.html',context)           
    else:
        form = WalletForm()
        context = {'form':form,'balance':balance,'history':history}
    return render(request,'core/wallet.html',context)



def kyc(request):
    if request.method == 'POST':
            form = UserKyc(request.POST, request.FILES)
            uname = request.POST.get('name')
            upan = request.POST.get('pancard')
            uadhr = request.POST.get('adharcard')
            uacc = request.POST.get('account')
            uaccv = request.POST.get('account_verify')
            uifsc = request.POST.get('ifsc_code')
            upanf = request.FILES.get('pancard_front')
            uadhf = request.FILES.get('adharcard_front')
            uadhb = request.FILES.get('adharcard_backside')
            using = request.FILES.get('user_signature')
            user = UserKyc(relation = request.user ,name =uname ,pancard =upan ,adharcard = uadhr,
            account=uacc ,account_verify =uaccv ,ifsc_code =uifsc ,pancard_front =upanf,
            adharcard_front =uadhf ,adharcard_backside =uadhb ,user_signature=using
             )
            user.save()
            status = User.objects.get(email = request.user)
            status.kyc_pending = True
            status.save()
            messages.success(request,'Your kyc Has been send for review this will update ASAP')
            return HttpResponseRedirect('/')
    else:
        form = UserKycForm()
        form.order_fields(field_order=['name','pancard','adharcard','account','account_verify','ifsc_code',
        'pancard_front','adharcard_front','adharcard_back','user_signature'])
        context ={'form':form}
        return render(request,'core/kyc.html',context)






# raz will send you post request
@csrf_exempt
def handelrequest(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            order_id = ""
            for key, value in data.items():
                if key == 'razorpay_order_id':
                    order_id = value
                    print(request.user)
                    break
            status = Wallet.objects.filter(transition_id = order_id).first()   
            status.payment_status = True
            status.save()
            balance = Wallet.objects.filter(user__email = request.user).last()
            user_wallet = User.objects.get(email = request.user)
            if balance.payment_status == True:
                user_wallet.wallet += balance.amount
                user_wallet.save()
        return HttpResponseRedirect('/core/wallet/')
    else:
        return HttpResponseRedirect('/login/')

# Withdraw request
def withdraw(request):
       
        if request.method == 'POST':
            form = WithdrawForm(request.POST,request.FILES)
            if form.is_valid():
                uamo = form.cleaned_data['withdraw_amount']
                wdraw = User.objects.get(email = request.user)
                wdraw.withdraw_amount = uamo
                wdraw.withdraw_status = True
                wdraw.save()
                messages.success(request,'Withdraw request has been sent. your money will be transfer within 2-3 working days')
                return HttpResponseRedirect('/cst/profile/')
        else:    
            form = WithdrawForm()
        context = {'form':form}
        return render(request,'core/withdraw.html',context)

# contact to support function
def contactus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        text = request.POST.get('text')
        
        send_mail(
            # subject
            'Contact Us Support',
            # msg
            text,
            # from email
            settings.EMAIL_HOST_USER,
            # TO
            [email]

        )
    return render(request,'core/contactus.html')

# about us function 
def aboutus(request):
    return render(request,'core/aboutus.html')

