from django.db import models
from django.conf import settings

class Mesa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    mestre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_max_jogadores = models.IntegerField()
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
