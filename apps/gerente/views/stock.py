from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .. import models
from .. import serializers

@api_view(['GET', 'POST'])
def stock_api_view(request):
    if request.method == 'GET':
        categoria = models.Stock.objects.all()[:10]
        categoria_serializer = serializers.StockSerializer(categoria, many=True)
        return Response(categoria_serializer.data)
    elif request.method == 'POST':
        data = {}
        categoria_serializer = serializers.StockSerializer(data = request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data)
        else:
            data["error"]="categoria existente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        #return Response(user_serializer.errors)

@api_view(['GET','DELETE'])
def stock_detail_view(request, pk):
    if request.method == 'GET':
        categoria = models.Stock.objects.filter(id = pk).first()
        categoria_serializer = serializers.StockSerializer(categoria)
        return Response(categoria_serializer.data)
    elif request.method == 'DELETE':
        categoria = models.Stock.objects.filter(id = pk).first()
        categoria.delete()
        return Response('Eliminado')
        

