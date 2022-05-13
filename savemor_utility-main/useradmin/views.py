from django.shortcuts import render
from django.http import HttpResponseRedirect
from authentication.models import User
from cust.models import UserFunds
from . forms import Userchangeform , filter_serch
from django.contrib import messages
from django.db.models import Q
from core.models import UserKyc 
from core.forms import AdminKycForm
from recharge.models import Recharge
from datetime import datetime
# Create your views here.


# Admin panel Function
def admindisplay(request):
    if  request.user.is_superuser == True:
        # count all users
        data = User.objects.all().count()
        # pending certificate
        pending = User.objects.filter(Q(certificate_status='Premium') & Q(groups__name = 'Verify' )).count()
        #show pending approval kyc
        kyc = User.objects.filter(Q(kyc_pending = True) & Q(kyc_status = False)).count()
        # FIXED fund count 
        paid = User.objects.filter(funds__payment_status = True).count()
        # grand total of allfixed money
        amount = UserFunds.objects.values('amount').exclude(payment_status=False)
        grand_total  = 0
        for i in range(len(amount)):
            for key , val in amount[i].items():
                grand_total += int(val)
        # withdraw request
        withdraw = User.objects.filter(withdraw_status = True).count()
        wallet_money = User.objects.values('wallet')
        wallet_total  = 0
        for i in range(len(wallet_money)):
            for key , val in wallet_money[i].items():
                wallet_total += int(val)
        # recharge STATUS
        recharge = Recharge.objects.all().count()

        context = {'data':data,'pdata':pending,'withdraw': withdraw,'wallet_total':wallet_total,
         'kyc':kyc,'grand_total':grand_total,'paid':paid ,'recharge': recharge
         }
        return render(request,'uadmin/admin.html',context)  
    else:
        return HttpResponseRedirect('/cst/profile/')


# this function shows all users data to admin
def allusers(request):
    if  request.user.is_superuser == True:
        if request.method == 'POST':
            form = filter_serch(request.POST)
            if form.is_valid():
                rec = form.cleaned_data['UserSerch']
                if rec == 'kyc' :
                    data = User.objects.filter(Q(kyc_pending = True) & Q(kyc_status = False))
                elif rec == 'certificate':
                    data = User.objects.filter(Q(certificate_status='Premium') & Q(groups__name = 'Verify' ))
                elif rec == 'withdraw':
                    data = User.objects.filter(withdraw_status = True)
                elif rec == 'recharge':
                    data = User.objects.filter(Recharge_status = True)
                else:
                    data = User.objects.all()
        else:
            form = filter_serch()
            data = User.objects.all()
        context = {'data':data,'form':form}
        return render(request,'uadmin/alluser.html',context) 
    else:
        return HttpResponseRedirect('/cst/profile/')


# admin panel for edit the details of user
def admin_user_edit(request,pk):
    if  request.user.is_superuser == True:
        udata = User.objects.get(pk = pk)
        
        if request.method == 'POST':
            form = Userchangeform( request.POST ,request.FILES,instance = udata)
            if form.is_valid():
                form.save()
            if UserKyc.objects.filter(relation__pk = pk).exists():
                kycdata = UserKyc.objects.get(relation__pk = pk)
                form2 = AdminKycForm(request.POST ,request.FILES,instance = kycdata)
                if form2.is_valid():
                    form2.save()
            messages.success(request,'User Update Successfully')
            return HttpResponseRedirect('/uad/allusers/')
        else:
            form = Userchangeform(instance = udata)
            if UserKyc.objects.filter(relation__pk = pk).exists():
                kycdata = UserKyc.objects.get(relation__pk = pk)
                form2 = AdminKycForm(instance = kycdata)
            else:
                form2 = None
        return render(request,'uadmin/admin_edit.html',{'form':form,'form2':form2})   
    else:
        return HttpResponseRedirect('/cst/profile/')

 
# display all fixed deposit forms
def allforms(request):
    form = UserFunds.objects.all()
    context = {'form':form}
    return render(request,'uadmin/allforms.html',context)

# pending recharge forms
def recharge_admin(request):
    form = Recharge.objects.filter(Recharge_status = True)
    context = {'form':form}
    return render(request,'uadmin/recharge.html',context)

# recharge dine status update
def recharge_done(request,pk):
    status = Recharge.objects.get(id = pk)
    status.Recharge_status = False
    status.recharge_done = datetime.now()
    status.save()
    messages.success(request,'recharge done status update')
    return HttpResponseRedirect('/uad/recharge_admin/')


