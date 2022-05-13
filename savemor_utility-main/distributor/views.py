
from django.shortcuts import render
from authentication.forms import singupform
from django.contrib import messages
from authentication.models import User
from django.http import HttpResponseRedirect , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . forms import send_money_form

# Create your views here.




# distributor user creation form
def dist(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form = singupform(request.POST)
            if form.is_valid():
                vname = form.cleaned_data['email']
                form.save()
                ref = User.objects.get(email = vname)                
                ref.refer_by = request.user.email
                ref.save()
                return HttpResponseRedirect('/')
        else:    
            form = singupform()
        context = {'form':form}
        return render(request,'dist/distributorsingup.html',context)
    else:
        return HttpResponseRedirect('/login/')


def dist_cust(request):
    data = User.objects.filter(refer_by = request.user.email)
    print(data)
    context = {'data':data}
    return render(request,'dist/list_user.html',context)




# send money to merchant
@csrf_exempt
def send_money(request):
    if request.method == 'POST':
        userdata = User.objects.get(email = request.user)
        form = send_money_form(request.POST)
        if form.is_valid():
            user = request.POST['user']
            money = int(request.POST['money'])
            pin = int(request.POST['pin'])
            if userdata.pin == pin:
                data = User.objects.get(email = user)
                wallet = userdata.wallet 
                if wallet < money:
                    messages.warning(request,'Your Wallet money is low please add more money ')
                    return HttpResponseRedirect('/core/wallet/')
                else:
                    userdata.wallet -= money
                    data.wallet += money
                    userdata.save()
                    data.save()
                    messages.success(request,'Money Has been Transfered')
                    return HttpResponseRedirect('/dist/send_money/')
            else:
                messages.warning(request,'Incorrect Pin')
                return HttpResponseRedirect('/dist/send_money/')

        else:
            messages.warning(request,'Invalid information')
            return HttpResponseRedirect('/dist/send_money/')
    form = send_money_form()
    context = {'form':form}
    return render(request,'dist/send_money.html',context)

@csrf_exempt
def fetch_data(request):
    if request.method == 'POST':
        form = send_money_form(request.POST)
        if form.is_valid():
            user = request.POST['user']        
            if User.objects.filter(email = user).exists():
                data = User.objects.get(email = user)
                return JsonResponse({'username':'Username = '+ data.username,'mobile': 'Mobile Number = '+ str(data.mobile)})
            else:
                return JsonResponse({'status':'User Not Exist'})
