from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
 username = forms.CharField(label='Username', max_length=30 ,widget=forms.TextInput(attrs={"class" : "form-control"}))
 email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : "form-control"}))
 password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class' : "form-control"}))
 password2 = forms.CharField(label='Password (Again)',widget=forms.PasswordInput(attrs={'class' : "form-control"}))
 def clean_password2(self):
  if 'password1' in self.cleaned_data:
   password1 = self.cleaned_data['password1']
   password2 = self.cleaned_data['password2']
   if password1 == password2:
    return password2
    raise forms.ValidationError('Passwords do not match.')
 def clean_username(self):
  username = self.cleaned_data['username']
  if not re.search(r'^\w+$', username):
   raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
  try:
   User.objects.get(username=username)
  except ObjectDoesNotExist:
   return username
   raise forms.ValidationError('Username is already taken.')

class loginform(forms.Form):
 username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={"class" : "form-control"}))
 password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "form-control"}))
