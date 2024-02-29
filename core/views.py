from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect to the home page
    else:
        form = UserRegistrationForm()

    return render(request, "signup.html", {'form': form})