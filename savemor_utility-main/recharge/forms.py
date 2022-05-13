from django import forms
from . models import Recharge
from django.core import validators
# from django.core.exceptions import ValidationError


OPERATOR = [
    ('---','- - -'),
    ('JIO','Jio'),
    ('AT','Airtel'),
    ('VF','VodafoneIdea'),
    ('BSNL','BSNL TopUp'),
    ('BSS','BSNL Special (STV)'),
    ('BSV','BSNL Recharge/Validity (RCV)'),
]



DISH_OPERATOR=[
    ('---','- - -'),
    ('VDD','Videocon DTH'),
    ('TSD','Tata Play'),
    ('SD','Sun Direct'),
    ('DTD','Dish TV'),
    ('ATD','Airtel Digital TV'),
]


ELECTRICITY_OPERATOR = [
    ('- - -','- - -'),
    ('PSPCL',' Punjab State Power Corporation Limited'),
    ('NPCL','Noida Power Company Limited'),
    ('KRE','Kota Electricity Distribution - RAJASTHAN'),
    ('HPE','Himachal Pradesh State Electricity Board'),
    ('BRP','BSES Rajdhani Power Ltd - Delhi'),

]

class MobileRechargeForm(forms.ModelForm):
    form =  forms.CharField(label='',widget=forms.HiddenInput(attrs={'value':'mobile'}))
    mobile =  forms.IntegerField(validators=[validators.MinLengthValidator(10)],label='Mobile Number',required=True,label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    mobile_operator =  forms.ChoiceField(label='Operator',label_suffix="",choices=OPERATOR,widget=forms.Select(attrs={'class':'form-select '}))
    amount =  forms.IntegerField(validators=[validators.MinValueValidator(10)],label='Plan', min_value=8,required=True,label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Recharge
        fields = ['mobile','mobile_operator','amount']
        
    def clean(self):
        cleaned_data = super().clean()
        vmobile = self.cleaned_data['amount']
        if len(vmobile) == "":
            raise forms.ValidationError('Please Check Your Recharge Amount')
            

class DthRechargeForm(forms.ModelForm):
    form =  forms.CharField(label='',widget=forms.HiddenInput(attrs={'value':'d2h'}))
    customer_id = forms.CharField(label='Customer Id',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    dish_operator =  forms.ChoiceField(label='Operator',label_suffix="",choices=DISH_OPERATOR,widget=forms.Select(attrs={'class':'form-select '}))
    amount =  forms.IntegerField(label='Plan',label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Recharge
        fields = ['customer_id','dish_operator','amount']


class ElectricityForm(forms.ModelForm):
    form =  forms.CharField(label='',widget=forms.HiddenInput(attrs={'value':'electricity'}))
    electricity = forms.CharField(label='Accouont No',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    electricity_operator =  forms.ChoiceField(label='Operator',label_suffix="",choices=ELECTRICITY_OPERATOR,widget=forms.Select(attrs={'class':'form-select '}))
    amount =  forms.IntegerField(label='Plan',label_suffix="",widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Recharge
        fields = ['electricity','electricity_operator','amount']