from .models import Job, Aplicados


def lista_jobs(request):
    #organiza os jobs apartir do mais recente
    lista_jobs =Job.objects.all().order_by('-lancamento')
    return {'lista_jobs_recentes':lista_jobs }


def bonus_vagas_mais_vistas(request):
    #organiza os jobs apartir do mais acessado e estabelece o mais acessado
    lista_jobs_populares =Job.objects.all().order_by('-visualizados')
    if lista_jobs_populares:
        job_popular = lista_jobs_populares[0]
    else:
        job_popular=None
    return {'lista_jobs_mais_vistos': lista_jobs_populares,'job_mais_visto': job_popular}


def bonus_vagas_mais_aplicadas(request):
    #organiza os jobs apartir do que tiver maior numero de candidatos
    #estabelece o job com maior numero de candidatos
    lista_jobs_populares = Job.objects.all().order_by('-total_candidatos')
    if lista_jobs_populares:
        job_popular = lista_jobs_populares[0]
    else:
        job_popular = None
    return {'lista_jobs_mais_aplicados': lista_jobs_populares,'job_mais_candidatos': job_popular}










