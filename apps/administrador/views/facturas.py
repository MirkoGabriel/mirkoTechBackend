from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from apps.administrador import models
from apps.administrador import serializers
from datetime import datetime, timedelta


@api_view(['GET', 'POST'])
def factura_api_view(request):
    if request.method == 'GET':
        data = {}
        fecha1 = request.query_params.get('fecha1')
        fecha2 = request.query_params.get('fecha2')
        if fecha1 != None and fecha2 != None:
            startdate = datetime.strptime(fecha1, '%d/%m/%Y')
            enddate = datetime.strptime(fecha2, '%d/%m/%Y')
            print(startdate)
            print(enddate)
            factura = models.Factura.objects.filter(fechaIngreso__date__range=(startdate,enddate))
        else:
            factura = models.Factura.objects.all()[:10]
        factura_serializer = serializers.FacturaSerializer(factura, many=True)
        return Response(factura_serializer.data)
    elif request.method == 'POST':
        data = {}
        factura_serializer = serializers.FacturaSerializer(data = request.data)
        if factura_serializer.is_valid():
            factura_serializer.save()
            return Response(factura_serializer.data)
        else:
            data["error"]="Usuario existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def factura_detail_view(request, pk):
    if request.method == 'GET':
        data = {}
        factura = models.Factura.objects.filter(id = pk).first()
        if factura == None:
            data["error"]="tarea no existe"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            factura_serializer = serializers.FacturaSerializer(factura)
            return Response(factura_serializer.data)
    elif request.method == 'PUT':
        factura = models.Factura.objects.filter(id = pk).first()
        factura_serializer = serializers.FacturaSerializer(factura, data=request.data)
        if factura_serializer.is_valid():
            factura_serializer.save()
            return Response(factura_serializer.data)
        return Response(factura_serializer.errors)
    elif request.method == 'DELETE':
        factura = models.Factura.objects.filter(id = pk).first()
        factura.delete()
        return Response('Eliminado')
        
