from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if username != password:


            return redirect('/button')

        else:
            messages.info(request,"")
            return redirect('/login')
    return render(request,"login.html")








def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            return redirect('/login')
        else:

            messages.info(request, "password not matching")





    return render(request,'register.html')


def button(request):



    return render(request, 'button.html')


def form(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['mail id']
        if username != password:


            messages.info(request, "order confirmed")

        else:
            messages.info(request, "")





    return render(request,'form.html')








