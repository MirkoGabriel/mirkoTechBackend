from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def tareasOT_api_view(request):
    if request.method == 'GET':
        data = {}
        ot = request.query_params.get('ot')
        if ot!=None:
            tareasOT = models.TareasOT.objects.filter(ot=ot)
            if tareasOT.exists() == False:
                data["error"]="tarea no existe"
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            tareasOT = models.TareasOT.objects.all()
        tareasOT_serializer = serializers.TareasOTSerializer(tareasOT, many=True)
        return Response(tareasOT_serializer.data)
    elif request.method == 'POST':
        data = {}
        tareasOT_serializer = serializers.TareasOTSerializer(data = request.data)
        if tareasOT_serializer.is_valid():
            tareasOT_serializer.save()
            return Response(tareasOT_serializer.data)
        else:
            data["error"]="Error"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def tareasOT_detail_view(request, pk):
    if request.method == 'GET':
        tareasOT = models.TareasOT.objects.filter(id = pk).first()
        tareasOT_serializer = serializers.TareasOTSerializer(tareasOT)
        return Response(tareasOT_serializer.data)
    elif request.method == 'PUT':
        tareasOT = models.TareasOT.objects.filter(id = pk).first()
        tareasOT_serializer = serializers.TareasOTSerializer(tareasOT, data=request.data)
        if tareasOT_serializer.is_valid():
            tareasOT_serializer.save()
            return Response(tareasOT_serializer.data)
        return Response(tareasOT_serializer.errors)
    elif request.method == 'DELETE':
        tareasOT = models.TareasOT.objects.filter(id = pk).first()
        tareasOT.delete()
        return Response('Eliminado')
        

