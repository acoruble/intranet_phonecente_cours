from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import NewCallForm
from .models import Call

def is_teammember(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 1

def is_customer(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 2

# @user_passes_test(is_teammember)
# def new_call(request):
#     if request.method == 'POST':
#         form = NewCallForm(request.POST)
#         if form.is_valid():
#             form.instance.teammember = request.user.teammember
#             form.save()
#
#     else:
#         form = NewCallForm()
#     return render(
#         request,
#         'utils/form.html',
#         {
#             'title': "Nouvel Appel",
#             'form':form,
#         }
#     )

@user_passes_test(is_teammember)
def call_list(request):
    calls = Call.objects.filter(teammember = request.user.teammember).order_by("-solved", "-created")
    return render(
        request,
        'calls/call_list.html',
        {
            'calls': calls,
        }
    )

# @user_passes_test(is_teammember)
def call_edit(request, call_id=None):
    print(request.user.customer)
    current_instance = None
    if call_id:
        if request.user.user_type == 1:
            current_instance = Call.objects.get(id = call_id, teammember = request.user.teammember)
        elif request.user.user_type == 2:
            current_instance = Call.objects.get(id = call_id)
    if request.method == 'POST':
        form = NewCallForm(request.POST, instance = current_instance)
        if form.is_valid():
            if not current_instance:
                if request.user.user_type == 1:
                    form.instance.teammember = request.user.teammember
                elif request.user.user_type == 2:
                    form.instance.teammember = None
            form.save()
    else:
        form = NewCallForm(instance = current_instance)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Appel",
            'form':form,
        }
    )

@user_passes_test(is_customer)
def call_list_customer(request):
    calls = Call.objects.filter()
    return render(
        request,
        'calls/call_list.html',
        {
            'calls': calls,
        }
    )
