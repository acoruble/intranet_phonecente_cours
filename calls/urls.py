# coding: UTF-8
from django.urls import path

from calls import views

app_name = 'calls'
urlpatterns = [

    path('new_call/', views.new_call, name="new_call"),


] 
