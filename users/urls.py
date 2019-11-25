# coding: UTF-8
from django.urls import path

from users import views, cbv

app_name = 'users'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('account-settings/', views.account_settings, name="account_settings"),
    path('role-attribution/', views.role_attribution, name="role_attribution"),
    path(
        'role-attribution-teammember-<int:user_id>/',
        cbv.TeamMemberCreate.as_view(),
        name="role_attribution_teammember"
        ),
    path(
        'role-attribution-customer-<int:user_id>/',
        cbv.CustomerCreate.as_view(),
        name="role_attribution_customer"
        ),

]
