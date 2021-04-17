from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers


@api_view(['GET', 'POST'])
def cliente_api_view(request):
    if request.method == 'GET':
        data = {}
        nombre = request.query_params.get('nombre')
        if nombre != None:
            cliente = models.Cliente.objects.filter(nombre__icontains=nombre)
            if cliente.exists() == False:
                data["error"] = "cliente no existe"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        else:
            cliente = models.Cliente.objects.all()[:10]
        cliente_serializer = serializers.ClienteSerializer(cliente, many=True)
        return Response(cliente_serializer.data)
    elif request.method == 'POST':
        data = {}
        cliente_serializer = serializers.ClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        else:
            data["error"] = "Cliente existente"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        # return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail_view(request, pk):
    if request.method == 'GET':
        cliente = models.Cliente.objects.filter(id=pk).first()
        cliente_serializer = serializers.ClienteSerializer(cliente)
        return Response(cliente_serializer.data)
    elif request.method == 'PUT':
        cliente = models.Cliente.objects.filter(id=pk).first()
        cliente_serializer = serializers.ClienteSerializer(
            cliente, data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)
    elif request.method == 'DELETE':
        cliente = models.Cliente.objects.filter(id=pk).first()
        cliente.delete()
        return Response('Eliminado')
