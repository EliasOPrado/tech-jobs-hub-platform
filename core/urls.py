from django.urls import path
from .views import index, signup, set_login, set_logout

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", set_login, name="login"),
    path("logout/", set_logout, name="logout"),
]
