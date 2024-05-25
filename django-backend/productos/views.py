from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializer import ProductoSerializer

# Create your views here.

@api_view(['POST'])
def crear_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        nombre = serializer.validated_data['nombre']
        
        if Producto.objects.filter(nombre=nombre).exists():
            return Response({'Error': 'El producto ya está registrado'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'mensaje': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

