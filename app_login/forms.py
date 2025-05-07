from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app_login import models
from django.contrib.auth.models import User

class UserInfoform(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta: 
        model = User
        fields = ('username','email','password1','password2')

class UserChangeInfo(UserChangeForm):
    class Meta: 
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password')

class Profile_pic_add(forms.ModelForm):
    class Meta:
        model = models.Userprofile
        fields = ['profile_pic']