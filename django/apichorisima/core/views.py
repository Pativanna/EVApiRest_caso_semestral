from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.shortcuts import render
from rest_framework import status#, generics
from django.contrib.auth import authenticate
from .models import user
from .serializer import UserSerializer

@api_view(['GET', 'POST'])
def lista_usuarios(request):
    if request.method == 'GET':
        users = user.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        correo = data.get('correo')
        # Verificar si ya existe un usuario con el mismo correo electrónico
        existing_user = user.objects.filter(correo=correo).first()
        if existing_user:
            return Response({'error': 'Ya existe un usuario con este correo electrónico.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def autenticar_usuario(request):
    if request.method == 'POST':
        correo = request.data.get('correo', '')
        password = request.data.get('password', '')

        # Autenticar al usuario
        usuario = authenticate(request, username=correo, password=password)

        if usuario is not None:
            return Response({'success': True, 'message': 'Autenticación exitosa'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)