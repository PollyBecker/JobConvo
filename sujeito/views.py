from django.shortcuts import render,  reverse
from django.views.generic import FormView, DetailView
from .models import Usuario
from .forms import CriarUserForm, CadEmpresaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from job.models import Job

# Create your views here.
class CriarPerfil(FormView):
    template_name = 'usuario.html'
    form_class = CriarUserForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job:homepage')


class CriarEmpresa(FormView):
    template_name = 'cadastrarempresa.html'
    form_class = CadEmpresaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job:homepage')


class DashboardEmpresa(LoginRequiredMixin, DetailView):
    template_name = 'dashboard.html'
    model = Usuario
    #detailview me retorna a variavel object

    def vagas_exibidas(self):
        context=super(DashboardEmpresa, self).get_context_data()
        todas_vagas =Job.objects.filter(contratante=self.get_object().minhas_vagas)
        context['lista_todas_vagas']= todas_vagas

        return context
