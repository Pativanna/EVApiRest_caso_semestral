from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .serializer import UserSerializer
from .models import user


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_usuarios(request):
    User = user.objects.all()
    serializer = UserSerializer(User, many=True)
    return Response(serializer.data)