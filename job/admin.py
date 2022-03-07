from django.contrib import admin
from .models import Job, Aplicados
from django.contrib.auth.admin import UserAdmin




# Register your models here.
admin.site.register(Job)
admin.site.register(Aplicados)
