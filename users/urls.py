# coding: UTF-8
from django.urls import path

app_name = 'users'
urlpatterns = [

]

# Import du module views de l'application users
from users import views

urlpatterns = [
    path('hello/', views.hello, name="hello"),
]
