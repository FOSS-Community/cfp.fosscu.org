from django.shortcuts import render,redirect
from .models import *
from .authentication import EmailAuthBackend
from django.contrib.auth import logout,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
import secrets, string


def Login(response):
    if response.method=='POST':
        email=response.POST.get('email')
        password=response.POST.get('password')
        user=EmailAuthBackend.authenticate(response,email,password,backend='users.authentication.EmailAuthBackend')
        print(user)
        if user is not None:
            if user.is_active:
                login(response,user)
                return redirect('verify/?email='+email)
            else:
                return HttpResponse('User is not active')
        else:
            return redirect('login', {email: email})
        
        
    return render(response, "users/screens/login.html")



def sign_up(response):
    if response.method=='POST':
        first_name=response.POST.get('firstname')
        last_name=response.POST.get('lastname')
        email=response.POST.get('email')
        password=response.POST.get('password')
        
        if UserModel.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
        else:
            UserModel.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                )
            return redirect('login')
    return render(response, "users/screens/signup.html", {})

def forgot_password(response):
    if response.method=='POST':
        email = response.POST.get('email')
        
        if UserModel.objects.filter(email=email).exists():
            return redirect('verify')
    return render(response, "users/screens/forgot_password.html", {})


def verify(request):
    code = ''.join(secrets.choice(list(string.ascii_uppercase+'0123456789')) for n in range(6))
    email = request.GET.get('email')
            
    return render(request, "users/screens/verify.html", { "email": email})