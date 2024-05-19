from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

@api_view(['POST'])
def login(request):
    cliente = get_object_or_404(Cliente, correo=request.data['correo'])
    if not cliente.check_password(request.data['contraseña']):
        return Response({"Error": "Contraseña invalida"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ClienteSerializer(instance=cliente)

    return Response({"cliente": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = ClienteSerializer(data=request.data)

    if serializer.is_valid():
        correo_ingresado = serializer.validated_data['correo']
        contraseña = serializer.validated_data['contraseña']

        if Cliente.objects.filter(correo=correo_ingresado).exists():
            return Response({'Error': 'El correo electrónico ya está registrado'}, status=status.HTTP_400_BAD_REQUEST)

        cliente = serializer.save()
        cliente.set_password(contraseña)
        cliente.save()

        return Response({"cliente": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

