from django.contrib import admin
from .models import Candidato
from django.contrib.auth.admin import UserAdmin




# Register your models here.
admin.site.register(Candidato, UserAdmin)

# Register your models here.
