from rest_framework import generics
from store.models import Product
from .models import Product ,Category
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer