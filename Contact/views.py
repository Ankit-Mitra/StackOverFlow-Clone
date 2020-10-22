from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'Contact/home.html')


def error_404_view(request, exception):
    return render(request,'Contact/404.html')

def landing(request):
    return render (request,'Contact/landing.html')
    
def signupuser(request):
    return render (request,'Authentication/signupuser.html')

def login(request):
    return render (request,'Authentication/loginuser.html')

def contact(request):
    return render (request,'Contact/contact.html')