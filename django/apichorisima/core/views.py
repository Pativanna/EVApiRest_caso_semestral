from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import user

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