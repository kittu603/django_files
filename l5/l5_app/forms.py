from l5_app.models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms

#create form with basic User model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password','first_name')


#create form with UserProfileInfo model

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')


