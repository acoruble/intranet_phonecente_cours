from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import RegisterForm, AccountSettingsForm
from .models import UserProfile

# View
def hello_old(request):
    return HttpResponse("Hello World!")

def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': "Hello World!",
        }
    )

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:myaccount"))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['raw_password']
            user = UserProfile.objects.create_user(
                username=username,
                email=email,
                password=raw_password,
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("users:myaccount"))
    else:
        form = RegisterForm()
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("users:register"),
            'title': "Inscription",
            'form':form,
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:myaccount"))
    elif 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET['next'])
            else:
                return HttpResponseRedirect(reverse("users:myaccount"))
        else:
            return render(
                request,
                'users/login.html',
                {
                    "auth_error": True,
                }
            )
    else:
        return render(
            request,
            'users/login.html',
            {}
        )

@login_required
def myaccount(request):
    return render(
        request,
        'users/myaccount.html',
    )

@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountSettingsForm(instance=request.user)
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("users:register"),
            'title': "Inscription",
            'form':form,
        }
    )

@user_passes_test(lambda u: u.is_superuser)
def role_attribution(request):
    users = UserProfile.objects.filter(teammember__isnull=True, customer__isnull=True).order_by("-id")
    return render(
        request,
        'users/role_attribution.html',
        {
            'users': users,
        }
    )
