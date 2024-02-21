from django import forms
from .models import *

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=False)
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class FoundItemForm(forms.ModelForm):
    #pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = FoundItem
        fields = ('item_name', 'location', 'image', 'found_date')

class LostItemForm(forms.ModelForm):
    #pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = LostItem
        fields = ('item_name', 'location', 'image', 'lost_date')