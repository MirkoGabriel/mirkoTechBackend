from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def ot_api_view(request):
    if request.method == 'GET':
        ordenTrabajo = models.OrdenTrabajo.objects.all()
        ordenTrabajo_serializer = serializers.OrdenTrabajoSerializer(ordenTrabajo, many=True)
        return Response(ordenTrabajo_serializer.data)
    elif request.method == 'POST':
        data = {}
        ordenTrabajo_serializer = serializers.OrdenTrabajoSerializer(data = request.data)
        if ordenTrabajo_serializer.is_valid():
            ordenTrabajo_serializer.save()
            return Response(ordenTrabajo_serializer.data)
        else:
            data["error"]="Error"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ot_detail_view(request, pk):
    if request.method == 'GET':
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo_serializer = serializers.OrdenTrabajoSerializer(ordenTrabajo)
        return Response(ordenTrabajo_serializer.data)
    elif request.method == 'PUT':
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo_serializer = serializers.OrdenTrabajo(ordenTrabajo, data=request.data)
        if ordenTrabajo_serializer.is_valid():
            ordenTrabajo_serializer.save()
            return Response(ordenTrabajo_serializer.data)
        return Response(ordenTrabajo_serializer.errors)
    elif request.method == 'DELETE':
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo.delete()
        return Response('Eliminado')
        

