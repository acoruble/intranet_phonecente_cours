from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import RegisterForm
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
        return HttpResponseRedirect(reverse("users:hello"))
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
            return HttpResponseRedirect(reverse("users:hello"))
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
