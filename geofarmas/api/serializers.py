from rest_framework import serializers
from geofarmas import models

class FarmaciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farmacias
        fields = '__all__'