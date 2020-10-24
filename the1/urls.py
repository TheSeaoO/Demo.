from django.conf.urls import url
from django.urls import path
from the1 import views
from the1.views import *
urlpatterns = [
    path('Login/',Login, name='登录'),
    path('Register/',Register, name='注册'),
    path('psd/', psd)
]