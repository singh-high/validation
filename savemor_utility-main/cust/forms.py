from django import forms
from . models import  UserFunds  
from authentication.models import User




# detail change panel for nuser
class UserEditform(forms.ModelForm):
    password = None
    username = forms.CharField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name = forms.CharField(label_suffix="",required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    email = forms.EmailField(label_suffix="", disabled=True ,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'name@example.com'}))
    mobile = forms.IntegerField(label_suffix="", disabled=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    status =  forms.CharField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Status'}))
    profile_pic = forms.ImageField(label_suffix="" ,widget=forms.FileInput(attrs={'class':'form-control w-100'}))
    
    class Meta:
        model =User
        fields = ['username','first_name','last_name','mobile','email','status','profile_pic']
       


# class for fd details of User
class UserFdDataForm(forms.ModelForm):
    fd_owner  = forms.CharField(label='Benificary Name' , label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control'}) )
    address  = forms.CharField(label='Address' , label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control'}) )
    address1  = forms.CharField(label='Landmark' , label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control'}) )
    email  = forms.EmailField(label='Email' , label_suffix="" ,widget=forms.EmailInput(attrs={'class':'form-control'}) )
    mobile  = forms.IntegerField(label='Mobile' , label_suffix="" ,widget=forms.NumberInput(attrs={'class':'form-control'}) )
    amount  = forms.IntegerField(label='Amount' , label_suffix="" ,widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserFunds
        fields = '__all__'
        exclude=['name','order_id','payment_id','payment_status','duration',"certificate_status"]
