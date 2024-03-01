from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Company, Applicant


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="",
        help_text=None,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter an unique username"}
        ),
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}
        ),
    )
    password1 = forms.CharField(
        label="",
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        ),
    )
    password2 = forms.CharField(
        label="",
        max_length=16,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm your password"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
        labels = {
            "username": "",
            "email": "",
            "first_name": "",
            "last_name": "",
            "password1": "",
            "password2": "",
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),
        }


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username or email",
            }
        ),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        ),
    )


class CompanyForm(forms.ModelForm):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the company's email address",
            }
        ),
    )
    company_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter the company name"}
        ),
    )

    class Meta:
        model = Company
        fields = ["company_name", "email"]


class ApplicantForm(forms.ModelForm):
    headline = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex: Your job title..."}
        ),
    )
    technologies = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Chose the technologies you work.",
            }
        ),
    )

    description = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Describe about yourself."}
        ),
    )

    class Meta:
        model = Applicant
        fields = ["headline", "description", "technologies"]
