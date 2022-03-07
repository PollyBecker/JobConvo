from django.shortcuts import render, redirect, reverse
from .models import Job, Aplicados
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sujeito.forms import AplicaForm
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# fbv function based views
# def homepage(request):
#     return render(request, 'base.html')
# cbv class based views

class Homepage(ListView):
    template_name = 'homepage.html'
    model=Job


class DetalheVagaCandidato (LoginRequiredMixin, DetailView,FormView):

    template_name = 'detalhe.html'
    model = Job
    form_class = AplicaForm

    def get(self, request, *args, **kwargs ):
        #contabilizando as views
        job = self.get_object()
        job.visualizados +=1
        job.save()
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        #add o nome da vaga no formulario de aplly
        formulario = form.save(commit=False)
        job = self.get_object()
        formulario.vaga= job
        #contabiliza os candidatos aplicados
        job.total_candidatos += 1
        #salvando o form e o job
        job.save()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job:homepage')


class DetalheVagaEmpresa(DetailView):
    template_name = 'empresadetalhe.html'
    model = Job


