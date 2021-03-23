from rest_framework import serializers
from .models import EquipoMarca, EquipoModel, Cliente, Stock, Productos, EquipoBackup


class EquipoMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoMarca
        fields = '__all__'


class EquipoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['marca'] = EquipoMarcaSerializer(instance.marca).data
        return response


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categoria'] = StockSerializer(instance.categoria).data
        return response

class EquipoBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoBackup
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cliente'] = StockSerializer(instance.cliente).data
        return response