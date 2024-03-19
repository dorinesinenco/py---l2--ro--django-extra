from rest_framework import serializers

from .models.Product import Product
from .models.Image import Image
from .models.Money import Money
from .models.Order import Order

class ProductSerializer(serializers.ModelSerializer):
    
    # configuration
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 
            'price_standard', 'price_discount'
        ]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id', 'file', 'product',             
        ]

class OrderSerializer(serializers.ModelSerializer):
    
    # configuration
    class Meta:
        model = Order
        fields = ['id', 'client_id']

class MoneySerializer(serializers.ModelSerializer):

    # configuration
    class Meta:
        model = Money
        fields = ['id','amount','currency']