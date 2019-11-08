# Import
from django.http import HttpResponse

# View
def hello(request):
    print("Bonjour !")
    return HttpResponse("Hello World!")
