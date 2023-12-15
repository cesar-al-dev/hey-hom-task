from rest_framework import serializers
from .models import Property
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        return data