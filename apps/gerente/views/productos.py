from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def producto_api_view(request):
    if request.method == 'GET':
        data = {}
        categoria = request.query_params.get('categoria')
        if categoria!=None:
            print(categoria)
            producto = models.Productos.objects.filter(categoria__nombreCategoria=categoria)
            if producto.exists() == False:
                data["error"]="Producto no existe"
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            producto = models.Productos.objects.all()
        producto_serializer = serializers.ProductosSerializer(producto, many=True)
        return Response(producto_serializer.data)
    elif request.method == 'POST':
        data = {}
        producto_serializer = serializers.ProductosSerializer(data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        else:
            data["error"]="Producto existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        #return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def producto_detail_view(request, pk):
    if request.method == 'GET':
        producto = models.Productos.objects.filter(id = pk).first()
        producto_serializer = serializers.ProductosSerializer(producto)
        return Response(producto_serializer.data)
    elif request.method == 'PUT':
        producto = models.Productos.objects.filter(id = pk).first()
        producto_serializer = serializers.ProductosSerializer(producto, data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)
    elif request.method == 'DELETE':
        producto = models.Productos.objects.filter(id = pk).first()
        producto.delete()
        return Response('Eliminado')
        

