from django.contrib.auth.forms import User, UserCreationForm
from .models import Candidato, Empresa
from job.models import Job, Aplicados
from django import forms

class CriarUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Candidato
        fields = ( 'username', 'email','password1', 'password2')




class CadEmpresaForm(UserCreationForm):

    class Meta:
        model = Empresa
        fields = ('username', 'email','cnpj', 'password1', 'password2')



class CriarJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [ 'tilulo','escolaridade','faixa_salarial' ,'requisitos',]


class AplicaForm(forms.ModelForm):

    class Meta:
        model = Aplicados
        exclude=('vaga',)










