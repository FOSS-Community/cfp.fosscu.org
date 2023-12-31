from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name='login_view'),
    path("sign_up/", views.sign_up, name='sign_up'),
    path("forgot_password/", views.forgot_password, name='forgot_password'),
    path("verify/", views.verify, name="verify"),
]
