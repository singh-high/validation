from django import forms




class send_money_form(forms.Form):
    user = forms.CharField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'form-control','id':'user'}))
    money = forms.IntegerField(label_suffix="" ,required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'money'}))
    # pin = forms.IntegerField(label_suffix="" ,required=False,widget=forms.PasswordInput(attrs={'class':'form-control','id':'pin','oninput':'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);','maxlength':'4','pattern':'[0-9]{4}'}))

    def clean(self):
        cleaned_data = super().clean()
        vmoney = cleaned_data['money']
        if vmoney == '':
            raise forms.ValidationError('Please Enter Amount To transfer')