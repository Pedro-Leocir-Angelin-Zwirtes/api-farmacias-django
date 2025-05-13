from rest_framework import viewsets, filters
from geofarmas.api import serializers
from geofarmas import models

class FarmaciasViewSet(viewsets.ReadOnlyModelViewSet): # Alterando para apenas dar get e não post
    serializer_class = serializers.FarmaciasSerializer
    queryset = models.Farmacias.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['uf']