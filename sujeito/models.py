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
    is_empresa = models.BooleanField('empresa status', default=False)
    is_candidato = models.BooleanField('candidato status', default=False)


class Empresa(Usuario):
    nome_empresa=models.CharField(max_length=100)
    vagas_criadas = models.IntegerField(default=0)
    cnpj =models.IntegerField()
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_empresa


class Candidato(Usuario):
    nome_candidato= models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome_candidato


