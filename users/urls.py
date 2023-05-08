from django.urls import path
from . import views
urlpatterns = [
    path("", views.Login, name='login'),
    path("sign_up/", views.sign_up, name='sign_up'),
    path("forgot_password/", views.forgot_password, name='forgot_password'),
    path("verify/", views.verify, name="verify"),
]