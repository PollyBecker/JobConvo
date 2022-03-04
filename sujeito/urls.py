from django.urls import path
from .views import CriarPerfil,CriarEmpresa,DashboardEmpresa
from django.contrib.auth import views as auth_views


app_name= 'sujeito'

urlpatterns = [
    path('usuario', CriarPerfil.as_view(), name='usuario'),
    path('cadastrarempresa', CriarEmpresa.as_view(), name='cadastrarempresa'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html') ,name='logout'),
    path("dashboard/<int:pk>", DashboardEmpresa.as_view(),name='dashboard')
]
