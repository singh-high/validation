from django import forms
from django.contrib.auth.forms import  UserChangeForm
from authentication.models import User


# detail change panel for adminuser
class Userchangeform(UserChangeForm):
    password = None
    username = forms.CharField(label_suffix="",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label_suffix="",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label_suffix="",widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_joined = forms.DateTimeField(label_suffix="",widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    last_login = forms.DateTimeField(label_suffix="" ,disabled=True,widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    premium_Created = forms.DateField(label_suffix="" ,required=False,widget=forms.DateInput(attrs={'class':'form-control'}))
    wallet = forms.IntegerField(label='Wallet' ,label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    withdraw_amount = forms.IntegerField(label='withdraw_amount',required=False ,label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    # premium_count = forms.IntegerField(label='subscribtion count',required=False ,label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    kyc_status = forms.BooleanField(label_suffix="",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    kyc_pending = forms.BooleanField(label_suffix="",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    distibutor_status = forms.BooleanField(label_suffix="",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    distibutor_apply = forms.BooleanField(label_suffix="",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    is_active = forms.BooleanField(label_suffix="",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    withdraw_status = forms.BooleanField(label_suffix="", required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    Premium_user = forms.BooleanField(label_suffix="", required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch'}))
    
    class Meta:
        model =User
        fields = '__all__'
        exclude = ['user_permissions','password','certificate_status','is_superuser','is_staff','refer_by']
        widgets = {
            'groups':forms.SelectMultiple(attrs={'class':'form-select w-25'})
        }

FIELD = [
    ('Choose Field','Choose Field'),
    ('kyc','kyc'),
    ('certificate','certificate'),
    ('withdraw','withdraw'),
]


class filter_serch(forms.Form):
    UserSerch = forms.ChoiceField(label='',label_suffix="",choices=FIELD,widget=forms.Select(attrs={'class':'form-select w-50 mt-5 '}))

