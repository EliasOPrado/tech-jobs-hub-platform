from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExtendedUser(User):
    is_company = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Company(Base):
    company_name = models.CharField(max_length=255)
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="companies_managed"
    )
    email = models.EmailField()
    location = models.CharField(max_length=255, default="São Paulo, Brazil")

    def __str__(self):
        return str(self.company_name)


class Applicant(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.TextField()

    def __str__(self):
        return f"Applicant: {self.user.username}"


class JobPost(Base):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="job_posts"
    )
    applicants = models.ManyToManyField(Applicant, related_name="job_application", null=True, blank=True)
    location = models.CharField(max_length=255, default="São Paulo, Brazil")
    
    def __str__(self):
        return str(self.job_title)
