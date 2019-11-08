# Import
from django.http import HttpResponse
from django.shortcuts import render

# View
def hello_old(request):
    print("Bonjour !")
    return HttpResponse("Hello World!")

def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': "Hello World!",
        }
    )
