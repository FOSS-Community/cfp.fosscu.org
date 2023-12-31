from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail

from .models import *

import secrets
import string


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('verify')
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
            UserModel.objects.create(
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
    code = ''.join(secrets.choice(
        list(string.ascii_uppercase+'0123456789')) for n in range(6))
    email = request.GET.get('email')

    return render(request, "users/screens/verify.html", {"email": email})
