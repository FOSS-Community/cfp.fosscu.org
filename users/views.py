from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth import get_user_model
from django.conf import settings


from .models import *

from typing import Union
import secrets
import string


UserModel = get_user_model()

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            code = ''.join(secrets.choice(list(string.ascii_uppercase+'0123456789')) for n in range(6))

            request.session['code'] = code

            # request.session['code'] = code

            send_mail(
            subject="Hellooooo",
            message=f"your verification code is {code}",
            from_email=settings.DEFAULT_FROM_EMAIL, 
            recipient_list=[email], 
            fail_silently=False,       
        )  
        
            # return redirect('verify/', match)
            return redirect('verify/')
            
        else:
            return HttpResponse('User does not exist')

    return render(request, "users/screens/login.html", {})


def sign_up(response):
    if response.method == 'POST':
        first_name = response.POST.get('firstname')
        last_name = response.POST.get('lastname')
        email = response.POST.get('email')
        password = response.POST.get('password')

        if UserModel.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
        else:
            user = UserModel.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            return redirect('login_view')
    return render(response, "users/screens/signup.html", {})


def forgot_password(response):
    if response.method == 'POST':
        email = response.POST.get('email')

        if UserModel.objects.filter(email=email).exists():
            return redirect('verify/?email='+email)
    return render(response, "users/screens/forgot_password.html", {})


def verify(request):

    code_from_session = request.session.get('code')
    
    
    if request.method == 'POST':

        email_code_verification = request.POST.get('otp')

        if email_code_verification == code_from_session:
            return HttpResponse('verified')
        
        else:
            return HttpResponse('error')

    return render(request, 'users/screens/verify.html')   