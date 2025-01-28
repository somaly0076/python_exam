from pathlib import __all__
from rest_framework import serializers
from .models import ProductTB, CategoryTB

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTB
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many= True)
    class Meta:
        model = CategoryTB
        fields = '__all__'





