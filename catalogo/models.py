from django.db import models

class Obra(models.Model):
    TIPO_CHOICES = [
        ("Filme", "Filme"),
        ("Série", "Série"),
    ]

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ano = models.IntegerField()
    genero =  models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
