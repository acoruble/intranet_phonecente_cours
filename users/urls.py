# coding: UTF-8
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('register/', views.register, name="register"),
]
