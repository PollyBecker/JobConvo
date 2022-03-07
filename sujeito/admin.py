from django.contrib import admin
from .models import Candidato,Empresa
from django.contrib.auth.admin import UserAdmin




# Register your models here.
admin.site.register(Candidato, UserAdmin)
admin.site.register(Empresa)

# Register your models here.
