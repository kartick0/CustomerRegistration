from .models import CustomerRegistration
from django.forms import ModelForm
from django import forms
class CustomerRegistrationForm(forms.Form):
    cname=forms.CharField(max_length=50, error_messages={'required':'Name cannot be blanked.'})
    age=forms.CharField(max_length=200,error_messages={'required': 'Age cannot be blanked'})
    address=forms.CharField(max_length=200,error_messages={'required': 'Address cannot be blanked'})
    phoneNumber=forms.CharField(max_length=200,error_messages={'required': 'Phone Number cannot be blanked'})
    email=forms.EmailField(max_length=200,error_messages={'required': 'Email cannot be blanked'})
    
    
    
    # def clean_cname(self):
    #     name=self.cleaned_data.get('cname')
    #     if name is None:
    #         raise forms.ValidationError('Customer name cannot be blanked')
    
    
    # def clean(self):
    #     cleaned_data=super().clean()
    #     name=cleaned_data.get('cname')
        
    #     age=cleaned_data.get('age')
    #     address=cleaned_data.get('address')
    #     phoneNumber=cleaned_data.get('phoneNumber')
    #     email=cleaned_data.get('email')
        
    #     if name is None:
    #         raise forms.ValidationError('Customer name cannot be blanked')