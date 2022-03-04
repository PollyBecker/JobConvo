from django.db import models
from django.utils import timezone
from sujeito.models import Usuario, Empresa

# Create your models here.

FAIXA_SALARIAL=(
    ('Até 1.000','Até 1.000'),
    ('De 1.000 a 2.000','De 1.000 a 2.000'),
    ('De 2.000 a 3.000','De 2.000 a 3.000'),
    ('Acima de 3.000','Acima de 3.000'),
)

ESCOLARIDADE=(
    ('Ensino fundamental','FUNDAMENTAL'),
    ('Ensino médio','MEDIO'),
    ('Tecnólogo','TECNOLOGO'),
    ('Ensino Superior','SUPERIOR'),
    ('Pós / MBA / Mestrado','POS'),
    ('Doutorado','DOUTORADO'),
)


class Job(models.Model):
    contratante = models.ForeignKey(Usuario, related_name="minhas_vagas", on_delete=models.CASCADE)
    tilulo=models.CharField(max_length=100)
    visualizados =models.IntegerField(default=0)
    lancamento=models.DateTimeField(default=timezone.now)
    escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADE)
    faixa_salarial=models.CharField(max_length=20,choices=FAIXA_SALARIAL)
    requisitos=models.TextField(max_length=1000)
    slug=models.SlugField()

    def __str__(self):
        return self.tilulo



#
