from django.shortcuts import render,redirect
from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)
from IWP_PROJECT import settings
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/afterlogin')
    return render(request,'login',{"form":form})


def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required(login_url='/login')

def afterlogin(request):
    return render(request,'afterlogin')

def progress(request):
    return render(request,'progress')

def liveprogress(request):
    return render(request,'liveprogress')

def credentials(request):
    return render(request,'credentials')

