from rest_framework import serializers
from .models import CustomUser  # Ajusta el nombre del modelo

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'