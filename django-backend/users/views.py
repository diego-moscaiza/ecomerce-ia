from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


