from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=50)


    def __str__(self):
        return nome


class Telefone(models.Model):
    residencial = models.CharField(max_length=20)
    comercial = models.CharField(max_length=20)





