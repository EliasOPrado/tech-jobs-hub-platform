from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:index")
    else:
        form = UserRegistrationForm()

    return render(request, "signup.html", {"form": form})


def set_login(request):
    """A view that manages the login form"""
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = authenticate(
                username=user_form.cleaned_data["username_or_email"],
                password=user_form.cleaned_data["password"]
            )
            if user:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                next_url = request.GET.get("next", "")
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect("core:index")
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        user_form = UserLoginForm()

    args = {"form": user_form, "next": request.GET.get("next", "")}
    return render(request, "login.html", args)


def set_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse("core:index"))


def chose_entity(request):
    return render(request, "entity_type.html")
