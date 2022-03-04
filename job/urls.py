from django.urls import path
from .views import Homepage, Detalhe


app_name= 'job'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path("jobs/<int:pk>", Detalhe.as_view(),name='detalhe'),

]