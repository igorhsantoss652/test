from django.db import models

# Create your models here.
class Clients(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    rua = models.CharField(max_length=40)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.nome

