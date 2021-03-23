from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def equipoMarca_api_view(request):
    if request.method == 'GET':
        equipoMarca = models.EquipoMarca.objects.all()
        equipo_serializer = serializers.EquipoMarcaSerializer(equipoMarca, many=True)
        return Response(equipo_serializer.data)
    elif request.method == 'POST':
        data = {}
        equipo_serializer = serializers.EquipoMarcaSerializer(data = request.data)
        if equipo_serializer.is_valid():
            equipo_serializer.save()
            return Response(equipo_serializer.data)
        else:
            data["error"]="Usuario existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','DELETE'])
def equipoMarca_detail_view(request, pk):
    if request.method == 'GET':
        equipoMarca = models.EquipoMarca.objects.filter(id = pk).first()
        equipo_serializer = serializers.EquipoMarcaSerializer(equipoMarca)
        return Response(equipo_serializer.data)
    elif request.method == 'DELETE':
        equipoMarca = models.EquipoMarca.objects.filter(id = pk).first()
        equipoMarca.delete()
        return Response('Eliminado')
        