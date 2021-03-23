from rest_framework import serializers
from .models import OrdenTrabajo
from apps.gerente.serializers import ClienteSerializer
from apps.users.serializers import UserSerializer

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cliente'] = ClienteSerializer(instance.cliente).data
        response['tecnico'] = UserSerializer(instance.tecnico).data
        return response