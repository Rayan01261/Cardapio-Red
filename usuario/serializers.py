from rest_framework import serializers
from .models import Gerente, Garcom
from django.contrib.auth.hashers import make_password


class GerenteSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Gerente
        fields = '__all__'
        read_only_fields = ['id'] 
        depth = 1


class GarcomSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Garcom
        fields = '__all__'
        read_only_fields = ['id'] 
        depth = 1
