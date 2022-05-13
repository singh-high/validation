from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from . forms import MobileRechargeForm , DthRechargeForm , ElectricityForm
from authentication.models import User 
from cust.generater import order_id
from core.models import Wallet
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from cust.generater import discount
from . models import RechargeHistory
import requests


# Create your views here.

tran_id = order_id()


# mobile recharge view
def Mobile_recharge(request):
    form = MobileRechargeForm()
    context = {'form':form}
    return render(request,'rech/mrecharge.html',context)


def success(request):
    if request.method == "POST":
        unm = request.POST['form']       
        user = User.objects.get(email = request.user)
        if request.POST['pin'] == str(user.pin):
            if unm == 'mobile':
                umob = request.POST['mobile']
                uope = request.POST['mobile_operator']
                uamo = int(request.POST['amount'])
                if uamo > user.wallet:
                    messages.warning(request,'Your Wallet Money Is Not Enoung, Please Add more Money')
                    return HttpResponseRedirect('/core/wallet/')
                else:
                    url = f"https://cyrusrecharge.in/api/recharge.aspx?memberid=AP499156&pin=93D4BDC1AF&number={umob}&operator={uope}&circle=&amount={uamo}&usertx={tran_id}&format=json"
                    response = requests.request("GET", url)
                    history = RechargeHistory(
                            history_Owner = request.user,
                            acc_num = umob,
                            operator = uope,
                            type = 'MOBILE',
                            amount = uamo,
                            recharge_status = response.json()['Status'],
                            error_message = response.json()['ErrorMessage'],
                            transition_id = response.json()['OperatorRef'] )
                    history.save()
                    if response.json()['Status'] == 'PENDING':
                        messages.warning(request,'Recharge Status Pending, Please Wait Untill Successfull Message')
                        return HttpResponseRedirect('/rec/mrecharge/')
                    elif response.json()['Status'] == 'REFUND':
                        messages.warning(request,'Recharge Not Done Your Money Will Be Refunded Within 24-48 Working Hours')
                        return HttpResponseRedirect('/rec/mrecharge/')
                    elif response.json()['Status'] == 'SUCCESS':
                        user.wallet -= uamo
                        user.save()
                        user_amount = Wallet(user = request.user ,message = 'Mobile Recharge',amount = uamo,transition_id=response.json()['OperatorRef'],
                        order_id=tran_id,payment_get_or_send='send')
                        user_amount.save()
                        messages.success(request,'Recharge Done')
                        return HttpResponseRedirect('/rec/mrecharge/')
                    else :
                        messages.warning(request,'Something Went Wrong Please Connect To Support')
                        return HttpResponseRedirect('/rec/mrecharge/')
            elif unm == 'd2h':
                umob = request.POST['customer_id']
                uope = request.POST['dish_operator']
                uamo = int(request.POST['amount'])
                if uamo > user.wallet:
                    messages.warning(request,'Your Wallet Money Is Not Enoung, Please Add more Money')
                    return HttpResponseRedirect('/core/wallet/')
                else:
                    url = f"https://cyrusrecharge.in/api/recharge.aspx?memberid=AP499156&pin=93D4BDC1AF&number={umob}&operator={uope}&circle=&amount={uamo}&usertx={tran_id}&format=json"
                    response = requests.request("GET", url)
                    history = RechargeHistory(
                            history_Owner = request.user,
                            acc_num = umob,
                            operator = uope,
                            type = 'DISH',
                            amount = uamo,
                            recharge_status = response.json()['Status'],
                            error_message = response.json()['ErrorMessage'],
                            transition_id = response.json()['OperatorRef'] )
                    history.save()
                    if response.json()['Status'] == 'PENDING':
                        messages.warning(request,'Recharge Status Pending, Please Wait Untill Successfull Message')
                        return HttpResponseRedirect('/rec/dthrecharge/')
                    elif response.json()['Status'] == 'REFUND':
                        messages.warning(request,'Recharge Not Done Your Money Will Be Refunded Within 24-48 Working Hours')
                        return HttpResponseRedirect('/rec/dthrecharge/')
                    elif response.json()['Status'] == 'SUCCESS':
                        user.wallet -= uamo
                        user.save()
                        user_amount = Wallet(user = request.user ,message = 'D2h Recharge',amount = uamo,transition_id=response.json()['OperatorRef'],
                        order_id=tran_id,payment_get_or_send='send')
                        user_amount.save()
                        messages.success(request,'Recharge Done')
                        return HttpResponseRedirect('/rec/dthrecharge/')
                    else :
                        messages.warning(request,'Something Went Wrong Please Connect To Support')
                        return HttpResponseRedirect('/rec/dthrecharge/')
        else:
            messages.warning(request,'Incorrect Pin')
            return HttpResponseRedirect('/cst/profile/')
        
    


def successApi(request):
    if request.method == "POST":
        unm = request.POST['form']
        user = User.objects.get(email = request.user)
        if unm == 'electricity':
            umob = request.POST['electricity']
            uope = request.POST['electricity_operator']
            uamo = int(request.POST['amount'])
            if uamo > user.wallet:
                    messages.warning(request,'Your Wallet Money Is Not Enoung, Please Add more Money')
                    return HttpResponseRedirect('/core/wallet/')
            else:
                url = f"https://cyrusrecharge.in/api/recharge.aspx?memberid=AP499156&pin=93D4BDC1AF&number={umob}&operator={uope}&circle=&amount={uamo}&usertx={tran_id}&account=&othervalue=&othervalue1=&format=json"
                response = requests.request("GET", url)
                history = RechargeHistory(
                            history_Owner = request.user,
                            acc_num = umob,
                            operator = uope,
                            type = 'ELECTRICITY',
                            amount = uamo,
                            recharge_status = response.json()['Status'],
                            error_message = response.json()['ErrorMessage'],
                            transition_id = response.json()['OperatorRef'] )
                history.save()
                if response.json()['Status'] == 'PENDING':
                        messages.warning(request,'Recharge Status Pending, Please Wait Untill Successfull Message')
                        return HttpResponseRedirect('/rec/electricityrecharge/')
                elif response.json()['Status'] == 'REFUND':
                        messages.warning(request,'Recharge Not Done Your Money Will Be Refunded Within 24-48 Working Hours')
                        return HttpResponseRedirect('/rec/electricityrecharge/')
                elif response.json()['Status'] == 'SUCCESS':
                        user.wallet -= uamo
                        user.save()
                        user_amount = Wallet(user = request.user ,message = 'D2h Recharge',amount = uamo,transition_id=response.json()['OperatorRef'],
                        order_id=tran_id,payment_get_or_send='send')
                        user_amount.save()
                        messages.success(request,'Recharge Done')
                        return HttpResponseRedirect('/rec/electricityrecharge/')
                else :
                        messages.warning(request,'Something Went Wrong Please Connect To Support')
                        return HttpResponseRedirect('/rec/electricityrecharge/')
        else:
            messages.warning(request,'Incorrect Pin')
            return HttpResponseRedirect('/rec/electricityrecharge/')
        


def Dth_Recharge(request):     
    form =    DthRechargeForm()
    context = {'form':form}
    return render(request,'rech/dthrecharge.html',context)
  
def electricityrecharge(request):     
    form =    ElectricityForm()
    context = {'form':form}    
    return render(request,'rech/elect_bill.html',context)
  





def Subscription(request):
    if request.user.is_authenticated:
        if not request.user.Premium_user:
            if request.method == 'POST':
                user = User.objects.get(email = request.user)
               
                if request.POST['pin'] == user.pin:
                    uamo = int(request.POST.get('hidden'))
                    if int(request.POST.get('hidden')) == 1000:
                        if user.wallet >= uamo:
                                user.wallet -= uamo
                                user.Premium_user = True
                                user.premium_Created = date.today()
                                user.save()
                                user_amount = Wallet(user = request.user ,amount = uamo,order_id=tran_id,payment_status=True,
                                payment_get_or_send='send' ,message='Subscribtion')
                                user_amount.save()
                                messages.success(request,'Congratulations You Are Now Our Premium User')
                                return HttpResponseRedirect('/cst/profile/')
                        else:
                            money = uamo - user.wallet
                            messages.warning(request,f'Need to add {money} more for recharge')
                            return HttpResponseRedirect('/core/wallet/')
                    else:
                        messages.warning(request,'Something Went Wrong Please Try Again')
                        return HttpResponseRedirect('/cst/profile/')
                else:
                    messages.warning(request,'Incorrect Pin')
                    return HttpResponseRedirect('/cst/profile/')
            else:
                return render(request,'rech/subscription.html')
        else:
            return HttpResponseRedirect('/cst/profile/')
    else:
        return HttpResponseRedirect('/login/')