from django.db import models

# Create your models here.

class Produto(models.Model):
    nome =  models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)    
    peso = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField()

    def __str__(self):
        return self.nome
