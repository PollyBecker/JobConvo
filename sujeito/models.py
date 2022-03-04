from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
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


PORTE=[('Ate 9 empregados','Ate 9 empregados'),
       ('Entre 10 e 49 empregados','Entre 10 e 49 empregados'),
       ('Entre 50 e 99 empregados','Entre 50 e 99 empregados'),
       ('Mais de 100', 'Mais de 100')

]
class Usuario(AbstractUser):
    ...


class Empresa(Usuario):
    nome=models.CharField(max_length=100)
    vagas_criadas = models.IntegerField(default=0)
    cnpj =models.IntegerField()
    porte= models.CharField(max_length=100, choices=PORTE)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Candidato(Usuario):
    # vaga = models.ForeignKey("Job", related_name="meus_candidatos", on_delete=models.CASCADE)
    nome_candidato= models.CharField(max_length=100)
    pretensao_salarial = models.CharField(max_length=20, choices=FAIXA_SALARIAL)
    experiencia=models.TextField(max_length=500)
    ultima_escolaridade= models.CharField(max_length=20, choices=ESCOLARIDADE)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_candidato
