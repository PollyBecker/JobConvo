from django.urls import path
from .views import CriarPerfilUsuario,CriarNovaEmpresa,DashboardEmpresa,CriarJob
from django.contrib.auth import views as auth_views


app_name= 'sujeito'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html') ,name='logout'),
    path('usuario/', CriarPerfilUsuario.as_view(), name='usuario'),
    path('cadastrarempresa/', CriarNovaEmpresa.as_view(), name='cadastrarempresa'),
    path('criarjob/<int:pk>', CriarJob.as_view(), name='criarjob'),
    path("dashboard/<int:pk>", DashboardEmpresa.as_view(),name='dashboard'),



]
