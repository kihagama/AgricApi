
from rest_framework import serializers
from .models import product
#Add the serializer here for each model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'