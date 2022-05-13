from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField ,PasswordChangeForm 
from . models import User
from django.core import validators



# validarors
def lengthcount(value):
    if len(str(value)) < 10:
            raise forms.ValidationError('enter a valid mobile number')

# This class is for usercreation
class singupform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}))
    username =UsernameField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autocomplete':'off'}))
    class Meta:
        model = User
        fields = ['email','mobile','username']
        widgets = {          
               'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        } 
        labels={
                'email':'Email'
        }


    def clean_mobile(self):
        mobil = self.cleaned_data['mobile']
        print('---------------',mobil)
        print('---------------',type(mobil))
        if len(str(mobil)) < 10:
            raise forms.ValidationError('enter a valid mobile number')
        return mobil



# User authentication form class 
class Loginform(AuthenticationForm):
    password = forms.CharField(label_suffix="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    username = UsernameField(label_suffix="",widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))


# Class for Old password change
class Passwordform(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',label_suffix="",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',label_suffix="",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='New Password(again)',label_suffix="",widget=forms.PasswordInput(attrs={'class':'form-control'}))
