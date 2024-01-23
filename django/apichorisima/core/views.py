from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apichorisima.utils import obtener_rol_del_usuario
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET', 'POST'])
def lista_usuarios(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()  # Cambiado de User a CustomUser
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        correo = data.get('correo')
        existing_user = CustomUser.objects.filter(correo=correo).first()  # Cambiado de User a CustomUser
        if existing_user:
            return Response({'error': 'Ya existe un usuario con este correo electrónico.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            # Asegúrate de incluir el campo 'role' en tu data al guardar
            serializer.save(role=data.get('role'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def autenticar_usuario(request):
    data = request.data
    correo = data.get('correo')
    password = data.get('password')
    print(f'Correo: {correo}, Contraseña: {password}')

    # Autenticar al usuario
    authenticated_user = authenticate(request, email=correo, password=password)
    print(f'Usuario autenticado: {authenticated_user}')

    if authenticated_user:
        print(f'Usuario activo: {authenticated_user.is_active}')
    else:
        print('Usuario no autenticado')

    if authenticated_user and authenticated_user.is_active:
        # Crear tokens y obtener el rol
        refresh = RefreshToken.for_user(authenticated_user)
        access_token = str(refresh.access_token)
        role = obtener_rol_del_usuario(authenticated_user)

        return Response({'token': access_token, 'role': role, 'mensaje': 'Autenticación exitosa'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Credenciales inválidas o cuenta inactiva'}, status=status.HTTP_401_UNAUTHORIZED)
