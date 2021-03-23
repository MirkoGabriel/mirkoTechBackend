from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from . import models
from . import serializers

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        data = {}
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        if email!=None and password!=None:
            print(email, password)
            users = models.User.objects.filter(email=email, password=password)
            if users.exists() == False:
                data["error"]="Usuario no existe"
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            users = models.User.objects.all()
        user_serializer = serializers.UserSerializer(users, many=True)
        return Response(user_serializer.data)
    elif request.method == 'POST':
        kind = request.data.get("kind")
        data = {}
        if kind =='A' or kind =='V' or kind=='G' or kind=='T':
            user_serializer = serializers.UserSerializer(data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            else:
                data["error"]="Usuario existente"
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data["error"]="Ingrese kind A:Administrador, V:Vendedor, T:tecnico, G:Gerente"
            return Response(data = data, status=status.HTTP_400_BAD_REQUEST)
        #return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk):
    if request.method == 'GET':
        user = models.User.objects.filter(id = pk).first()
        user_serializer = serializers.UserSerializer(user)
        return Response(user_serializer.data)
    elif request.method == 'PUT':
        user = models.User.objects.filter(id = pk).first()
        user_serializer = serializers.UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    elif request.method == 'DELETE':
        user = models.User.objects.filter(id = pk).first()
        user.delete()
        return Response('Eliminado')
        

