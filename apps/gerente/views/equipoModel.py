from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def equipoModel_api_view(request):
    if request.method == 'GET':
        equipoModel = models.EquipoModel.objects.all()
        equipo_serializer = serializers.EquipoModelSerializer(equipoModel, many=True)
        return Response(equipo_serializer.data)
    elif request.method == 'POST':
        data = {}
        equipo_serializer = serializers.EquipoModelSerializer(data = request.data)
        if equipo_serializer.is_valid():
            equipo_serializer.save()
            return Response(equipo_serializer.data)
        else:
            data["error"]="Usuario existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','DELETE'])
def equipoModel_detail_view(request, pk):
    if request.method == 'GET':
        equipoModel = models.EquipoModel.objects.filter(id = pk).first()
        equipo_serializer = serializers.EquipoModelSerializer(equipoModel)
        return Response(equipo_serializer.data)
    elif request.method == 'DELETE':
        equipoModel = models.EquipoModel.objects.filter(id = pk).first()
        equipoModel.delete()
        return Response('Eliminado')
        