from django.http import HttpResponse

def demo(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return HttpResponse("Welcome to Django!")