from django import forms
from django.forms import ModelForm
from .models import Account

class AccountRegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']


    def clean(self):
        cleaned_data = super(AccountRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
            'Passwords do not match!'
        )


    def __init__(self, *args, **kwargs):
        super(AccountRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


