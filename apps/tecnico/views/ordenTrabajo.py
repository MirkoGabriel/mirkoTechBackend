from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers
from datetime import datetime, timedelta


@api_view(['GET', 'POST'])
def ot_api_view(request):
    if request.method == 'GET':
        data = {}
        estado = request.query_params.get('estado')
        nroSerie = request.query_params.get('nroSerie')
        fecha1 = request.query_params.get('fecha1')
        fecha2 = request.query_params.get('fecha2')
        his = request.query_params.get('his')
        if estado != None:
            ordenTrabajo = models.OrdenTrabajo.objects.exclude(
                estadoEquipo=estado)
            if ordenTrabajo.exists() == False:
                data["error"] = "tarea no existe"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        elif fecha1 != None and fecha2 != None:
            startdate = datetime.strptime(fecha1, '%d/%m/%Y')
            enddate = datetime.strptime(fecha2, '%d/%m/%Y')
            ordenTrabajo = models.OrdenTrabajo.objects.exclude(
                estadoEquipo='Entregado').filter(fechaIngreso__date__range=(startdate, enddate))
        elif nroSerie != None:
            ordenTrabajo = models.OrdenTrabajo.objects.filter(
                nroSerie=nroSerie)
            if ordenTrabajo.exists() == False:
                data["error"] = "tarea no existe"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        elif his!=None:
            ordenTrabajo = models.OrdenTrabajo.objects.filter(id = his)
            if ordenTrabajo.exists() == False:
                data["error"]="tarea no existe"
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            ordenTrabajo = models.OrdenTrabajo.objects.all()[:10]
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
        data = {}
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo_serializer = serializers.OrdenTrabajoSerializer(ordenTrabajo)
        return Response(ordenTrabajo_serializer.data)
    elif request.method == 'PUT':
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo_serializer = serializers.OrdenTrabajoSerializer(ordenTrabajo, data=request.data)
        if ordenTrabajo_serializer.is_valid():
            ordenTrabajo_serializer.save()
            return Response(ordenTrabajo_serializer.data)
        return Response(ordenTrabajo_serializer.errors)
    elif request.method == 'DELETE':
        ordenTrabajo = models.OrdenTrabajo.objects.filter(id = pk).first()
        ordenTrabajo.delete()
        return Response('Eliminado')
        

