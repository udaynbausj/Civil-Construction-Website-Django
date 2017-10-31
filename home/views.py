from django.shortcuts import render


def home(request):
    return render(request,'index')
def about(request):
    return render(request,'about')
