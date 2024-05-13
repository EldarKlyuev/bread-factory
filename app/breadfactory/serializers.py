from rest_framework import serializers
from .models import Orders, Orderers, Items, Factors, Production


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrdererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderers
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factors
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'
