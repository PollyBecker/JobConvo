from django.contrib.auth.forms import User, UserCreationForm
from .models import Candidato, Empresa
from django import forms

class CriarUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Candidato
        fields = ( 'username', 'email','password1', 'password2')

class CadEmpresaForm(UserCreationForm):
    cnpj = forms.IntegerField()
    porte = forms.CharField()

    class Meta:
        model = Empresa
        fields = ('username', 'email','cnpj', 'porte', 'password1', 'password2')

