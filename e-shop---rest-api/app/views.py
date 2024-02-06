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



# PUBLIC VIEWS
def indexPage(request):
    template = loader.get_template('public/index.html')
    return HttpResponse(template.render({}, request))


# PUBLIC API VIEWS
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 



class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

    # Override
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # CUSTOM: OrderItem creation here
        product_id =  kwargs.get('uuid')

        order_item = OrderItem (
            product = Product.objects.get(pk = product_id), 
            order = Order.objects.get(pk = serializer.data.get('id'))
        )
        
        order_item.save()
        # CUSTOM: OrderItem creation here

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)










class MoneyView(generics.RetrieveAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer 












# ADMIN VIEWS    
class ProductAdminView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # TODO: access policy

