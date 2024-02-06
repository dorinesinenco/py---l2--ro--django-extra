from rest_framework import serializers

from .models.Product import Product
from .models.Money import Money
from .models.Order import Order

class ProductSerializer(serializers.ModelSerializer):
    
    # configuration
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'description', 
            'price_standard', 'price_discount'
        ]


class OrderSerializer(serializers.ModelSerializer):
    
    # configuration
    class Meta:
        model = Order
        fields = ['id']

class MoneySerializer(serializers.ModelSerializer):

    # configuration
    class Meta:
        model = Money
        fields = ['id','amount','currency']