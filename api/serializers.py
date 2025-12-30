
from rest_framework import serializers
from .models import product,workers
from django.contrib.auth.models import User
#Add the serializer here for each model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = workers
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

