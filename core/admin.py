from django.contrib import admin
from .models import Applicant, Company, JobPost, Technology

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(Technology)
