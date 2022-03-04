from django.shortcuts import render, redirect, reverse
from .models import Job
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class Detalhe ( LoginRequiredMixin, DetailView):

    template_name = 'detalhe.html'
    model = Job
    #detailview me retorna a variavel object

    def get(self, request, *args, **kwargs ):
        #contabilizando as views
        job = self.get_object()
        job.visualizados +=1
        job.save()

        return super().get(request, *args, **kwargs)


from django.shortcuts import render

# Create your views here.
