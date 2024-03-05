from django.urls import path
from .views import (
    index, 
    signup, 
    set_login, 
    set_logout, 
    chose_entity, 
    create_entity,
    company_page,
    job_posts,
)

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", set_login, name="login"),
    path("logout/", set_logout, name="logout"),
    path("chose-entity/", chose_entity, name="chose-entity"),
    path("create-entity/<str:entity_type>/", create_entity, name="create-entity"),
    path("company-page/<int:id>/", company_page, name="company-page"),
    path("job-posts/", job_posts, name="job-posts"),
    path('job-post/<int:id>/', job_posts, name='job-post'),
]
