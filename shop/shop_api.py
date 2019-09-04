from rest_framework import serializers,viewsets
from .models import Product,Category


class Shopserializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'products')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')