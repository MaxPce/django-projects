from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from producto.models import Producto
from producto.api.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer 