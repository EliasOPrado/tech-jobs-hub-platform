from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup_user(request):
    return render(request, "sigup.html")