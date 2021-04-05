from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers
from datetime import datetime, timedelta


@api_view(['GET', 'POST'])
def remito_api_view(request):
    if request.method == 'GET':
        data = {}
        fecha1 = request.query_params.get('fecha1')
        fecha2 = request.query_params.get('fecha2')
        if fecha1 != None and fecha2 != None:
            startdate = datetime.strptime(fecha1, '%d/%m/%Y')
            enddate = datetime.strptime(fecha2, '%d/%m/%Y')
            print(startdate)
            print(enddate)
            remito = models.Remito.objects.filter(fechaIngreso__date__range=(startdate,enddate))
        else:
            remito = models.Remito.objects.all()[:10]
        remito_serializer = serializers.RemitoSerializer(remito, many=True)
        return Response(remito_serializer.data)
    elif request.method == 'POST':
        data = {}
        remito_serializer = serializers.RemitoSerializer(data = request.data)
        if remito_serializer.is_valid():
            remito_serializer.save()
            return Response(remito_serializer.data)
        else:
            data["error"]="Usuario existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def remito_detail_view(request, pk):
    if request.method == 'GET':
        remito = models.Remito.objects.filter(id = pk).first()
        remito_serializer = serializers.RemitoSerializer(remito)
        return Response(remito_serializer.data)
    elif request.method == 'PUT':
        remito = models.Remito.objects.filter(id = pk).first()
        remito_serializer = serializers.RemitoSerializer(remito, data=request.data)
        if remito_serializer.is_valid():
            remito_serializer.save()
            return Response(remito_serializer.data)
        return Response(remito_serializer.errors)
    elif request.method == 'DELETE':
        remito = models.Remito.objects.filter(id = pk).first()
        remito.delete()
        return Response('Eliminado')
        
