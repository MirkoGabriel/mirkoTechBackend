from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def equipoBack_api_view(request):
    if request.method == 'GET':
        equipoBack = models.EquipoBackup.objects.all()
        equipoBack_serializer = serializers.EquipoBackupSerializer(equipoBack, many=True)
        return Response(equipoBack_serializer.data)
    elif request.method == 'POST':
        data = {}
        equipoBack_serializer = serializers.EquipoBackupSerializer(data = request.data)
        if equipoBack_serializer.is_valid():
            equipoBack_serializer.save()
            return Response(equipoBack_serializer.data)
        else:
            data["error"]="Cliente existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        #return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def equipoBack_detail_view(request, pk):
    if request.method == 'GET':
        equipoBack = models.EquipoBackup.objects.filter(id = pk).first()
        equipoBack_serializer = serializers.EquipoBackupSerializer(equipoBack)
        return Response(equipoBack_serializer.data)
    elif request.method == 'PUT':
        equipoBack = models.EquipoBackup.objects.filter(id = pk).first()
        equipoBack_serializer = serializers.EquipoBackupSerializer(equipoBack, data=request.data)
        if equipoBack_serializer.is_valid():
            equipoBack_serializer.save()
            return Response(equipoBack_serializer.data)
        return Response(equipoBack_serializer.errors)
    elif request.method == 'DELETE':
        equipoBack = models.EquipoBackup.objects.filter(id = pk).first()
        equipoBack.delete()
        return Response('Eliminado')
        

