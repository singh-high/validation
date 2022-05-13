from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from . forms import Loginform ,singupform ,Passwordform
# Create your views here.


# tHE function for user login page 
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Loginform(request=request , data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname ,password = upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/cst/profile/')
        else:
            form = Loginform()
        context = {'form':form}
        return render(request,'auth/login.html',context)
    else:
        return HttpResponseRedirect('/cst/profile/')
        

# terms and conditions
def terms(request):
    return render(request,'auth/terms.html')



# the function for user creation 
def usersingup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = singupform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login/')
        else:    
            form = singupform()
        context = {'form':form}
        return render(request,'auth/singup.html',context)
    else:
        return HttpResponseRedirect('/cst/profile/')

# User logout function
def userlogout(request):
    if  request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')


# Change password with old password
def userpwdchange(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = Passwordform(user = request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect('/')
        else:
            form = Passwordform(user=request.user)
        context = {'form':form}
        return render(request,'auth/password.html',context)
    else:
        return HttpResponseRedirect('/login/')






