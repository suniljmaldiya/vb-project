from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")
def contactus(request):
    return render(request,"contactus.html")
def faq(request):
    return render(request,"faq.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def services(request):
    return render(request,"services.html")

def dashboard(request):
    return render(request,"dashboard.html")



# def vitran(request):
#     return HttpResponse("Welcome to VitranBox")