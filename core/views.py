from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserLoginForm, CompanyForm, ApplicantForm
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
            #TODO: When creating the user, add a checkbox 
            # - to make user set as part of a already created company.
            return redirect("core:chose-entity")
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
    entity_type = request.GET.get('entity_type', None)

    if entity_type:
        return redirect(reverse("core:create-entity", kwargs={'entity_type': entity_type}))
    
    return render(request, "entity_type.html")

def create_entity(request, entity_type):
    if request.method == "POST":
        if entity_type == "company":
            form = CompanyForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.manager = request.user
                company.save()
                messages.success(request, "Company entity created successfully.")
                return redirect(reverse("core:index"))  # Adjust the redirect URL as needed
            
        elif entity_type == "applicant":
            form = ApplicantForm(request.POST)
            if form.is_valid():
                applicant = form.save(commit=False)
                applicant.user = request.user
                applicant.save()
                messages.success(request, "Applicant entity created successfully.")
                return redirect(reverse("core:index"))  # Adjust the redirect URL as needed
            
    else:
        # Handle GET request and render the form
        if entity_type == "company":
            form = CompanyForm()
        elif entity_type == "applicant":
            form = ApplicantForm()
        else:
            messages.error(request, "There was an error with the entity choice.")
            return redirect(reverse("core:chose-entity"))

    return render(request, 'entity_creation_form.html', {'form': form, 'entity_type': entity_type})
