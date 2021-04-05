from rest_framework import serializers
from .models import Remito, Factura
from apps.gerente.serializers import ClienteSerializer
from apps.users.serializers import UserSerializer
from apps.tecnico.serializers import OrdenTrabajoSerializer


class RemitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remito
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['administrador'] = UserSerializer(instance.administrador).data
        response['oti'] = OrdenTrabajoSerializer(instance.oti).data
        return response

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['administrador'] = UserSerializer(instance.administrador).data
        response['oti'] = OrdenTrabajoSerializer(instance.oti).data
        return response