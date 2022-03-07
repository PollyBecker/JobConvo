from django.urls import path
from .views import Homepage, DetalheVagaCandidato,DetalheVagaEmpresa


app_name= 'job'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path("jobs/<int:pk>", DetalheVagaCandidato.as_view(),name='detalhe'),
    path("meuscandidatos/<int:pk>", DetalheVagaEmpresa.as_view(),name='meuscandidatos')



]