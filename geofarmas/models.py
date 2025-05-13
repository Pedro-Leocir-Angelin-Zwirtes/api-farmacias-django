from django.db import models
from uuid import uuid4

class Farmacias(models.Model):

    id_farmacia = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    uf = models.CharField(max_length=5)
    municipio = models.CharField(max_length=255)
    nome_farmacia = models.CharField(max_length=255)
    endereco = models.TextField()
    bairro = models.CharField(max_length=255)