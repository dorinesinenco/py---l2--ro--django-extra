from rest_framework import generics

from .models.Product import Product
from .models.Money import Money
from .models.Order import Order
from .models.OrderItem import OrderItem
from .serializers import ProductSerializer, OrderSerializer, MoneySerializer

from rest_framework import status
from rest_framework.response import Response

from django.http import HttpResponse
from django.template import loader


























