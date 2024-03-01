from django.urls import path
from .views import index, signup, set_login, set_logout, chose_entity, create_entity
app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", set_login, name="login"),
    path("logout/", set_logout, name="logout"),
    path("chose-entity/", chose_entity, name="chose-entity"),
    path("create-entity/<str:entity_type>/", create_entity, name="create-entity"),
]
