from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import FormView, DetailView,CreateView, ListView
from .models import Usuario,Empresa
from .forms import CriarUserForm, CadEmpresaForm, CriarJobForm
from django.contrib.auth.mixins import LoginRequiredMixin
from job.models import Job

# Create your views here.
class CriarPerfilUsuario(FormView):
    template_name = 'usuario.html'
    form_class = CriarUserForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sujeito:login')


class CriarNovaEmpresa(FormView):
    template_name = 'cadastrarempresa.html'
    form_class = CadEmpresaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sujeito:login')


class CriarJob(CreateView):
    template_name = 'criarjob.html'

    form_class = CriarJobForm

    def form_valid(self, form):
        formulario=form.save(commit=False)
        formulario.contratante=self.request.user
        form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('job:homepage')


class DashboardEmpresa(LoginRequiredMixin, DetailView):
    template_name = 'dashboard.html'
    model = Usuario


    def get_context_data(self,**kwargs):
        context=super(DashboardEmpresa, self).get_context_data(**kwargs)
        nome=self.get_object().id
        todas_vagas =Job.objects.filter(contratante=nome)
        context['lista_todas_vagas']= todas_vagas

        return context








