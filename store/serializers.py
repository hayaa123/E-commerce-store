from importlib.metadata import files
from itertools import product
from statistics import mode
from rest_framework import serializers

from .models import Product, ProductImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image','alt_text']


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True , read_only=True)

    class Meta :
        model = Product
        fields = ["id","title","description","regular_price","product_image"]