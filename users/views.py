from django.shortcuts import render

# Create your views here.
def login(response):
    return render(response, "users/screens/login.html", {})

def sign_up(response):
    return render(response, "users/screens/signup.html", {})

def forgot_password(response):
    return render(response, "users/screens/forgot_password.html", {})

def verify(response):
    return render(response, "users/screens/verify.html", {})