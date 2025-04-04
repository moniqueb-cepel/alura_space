from django.db import models
from datetime import datetime

# Criar classes/ representa uma tabela no bd
# herdando a biblioteca models 
class Fotografia(models.Model):

    # categoria é uma lista
    # o CharField é uma tupla
    # precisa de virgula no final 
    opcoes_categoria = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PALNETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default='')
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False, verbose_name="Data da Fotografia")
    descricao = models.TextField(null=False, blank=False)
    # foto = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        # return f"Fotografia [nome={self.nome}]"
        return self.nome
