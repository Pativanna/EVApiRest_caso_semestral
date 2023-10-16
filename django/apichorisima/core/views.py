from rest_framework import viewsets
from .serializer import UserSerializer
from .models import user

# Create your views here.
 
class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer