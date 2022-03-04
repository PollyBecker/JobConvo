from .models import Job


def lista_jobs(request):
    lista_jobs =Job.objects.all().order_by('-lancamento')

    return {'lista_jobs_recentes':lista_jobs}