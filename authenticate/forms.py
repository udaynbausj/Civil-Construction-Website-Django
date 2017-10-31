from django import forms
from django.shortcuts import render
from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)

user = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("Wrong Credentials")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError('This User is no longer active')
        return super(UserLoginForm,self).clean(*args,**kwargs)