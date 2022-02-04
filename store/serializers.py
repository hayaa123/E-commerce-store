from importlib.metadata import files
from statistics import mode
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ["id","title","description"]