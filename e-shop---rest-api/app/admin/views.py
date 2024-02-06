from rest_framework.generics import  RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from ..models.Product import Product
from ..serializers import ProductSerializer


# ADMIN VIEWS    
# B[READ]
class ProductREADView(
                  RetrieveUpdateDestroyAPIView,
                  CreateAPIView                  
                ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

# [B]READ
class ProductBView(
                 ListAPIView            
                ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
