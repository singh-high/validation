from django import forms
from . models import Wallet , UserKyc 
from authentication.models import User



# User wallet balance form
class WalletForm(forms.ModelForm):
    message = forms.CharField(required=False,widget =forms.TextInput(attrs={'placeholder':'Any message(optional)','class':"form-control" }))
    class Meta:
        model = Wallet
        fields = ['amount','message']
        widgets = {
            'amount':forms.NumberInput(attrs={'placeholder':'Amount','class':"form-control" }),
                  }

# User kyc form
class UserKycForm(forms.ModelForm):
    name = forms.CharField(label='Name',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    pancard = forms.CharField(label='Pancard',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    adharcard = forms.CharField(label='Aadhaar Card',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    account = forms.IntegerField(label='Account Number',label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    account_verify = forms.IntegerField(label='Account Number(again)',label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    ifsc_code = forms.CharField(label='IFSC Code',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    pancard_front = forms.ImageField(label='Pancard (Front)',label_suffix="",widget=forms.FileInput(attrs={'class':'form-control'}))
    adharcard_front = forms.ImageField(label='Aadharcard(Front)',label_suffix="",widget=forms.FileInput(attrs={'class':'form-control'}))
    adharcard_backside = forms.ImageField(label='Aadharcard(Back)',label_suffix="",widget=forms.FileInput(attrs={'class':'form-control'}))
    user_signature = forms.ImageField(label='Signature',label_suffix="",widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserKyc
        fields = '__all__'
        exclude = ['relation','account']
    def clean(self):
        cleaned_data = super().clean()
        vname = self.cleaned_data['name']
        for i in range(len(vname)):
            if i.isdigit() :
                raise forms.ValidationError('Name must be in alphabetic')
        




class AdminKycForm(forms.ModelForm):
    name = forms.CharField(label='Name',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    pancard = forms.CharField(label='Pancard',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    adharcard = forms.CharField(label='Aadhaar Card',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    account = forms.CharField(label='Account Number',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    account_verify = forms.CharField(label='Account Number(again)',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    ifsc_code = forms.CharField(label='IFSC Code',label_suffix="",widget=forms.TextInput(attrs={'class':'form-control'}))
    pancard_front = forms.ImageField(label='Pancard (Front)',label_suffix="")
    adharcard_front = forms.ImageField(label='Aadharcard(Front)',label_suffix="")
    adharcard_backside = forms.ImageField(label='Aadharcard(Back)',label_suffix="")
    user_signature = forms.ImageField(label='Signature',label_suffix="")
    class Meta:
        model = UserKyc
        fields = '__all__'
        exclude = ['relation']


# Withdraw request
class WithdrawForm(forms.ModelForm):
    withdraw_amount = forms.IntegerField(label='Amount',label_suffix="",required=False,widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['withdraw_amount']
