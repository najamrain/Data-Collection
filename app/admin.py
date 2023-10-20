from django.contrib import admin

from app.models import Company, Photo, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(Photo)