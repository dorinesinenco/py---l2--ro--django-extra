from rest_framework import generics
from rest_framework.views import APIView
from ..models.Product import Product
from ..models.Money import Money
from ..models.Order import Order
from ..models.Client import Client
from ..models.OrderItem import OrderItem
from ..serializers import ProductSerializer, OrderSerializer, MoneySerializer

from rest_framework import status
from rest_framework.response import Response

from django.http import HttpResponse
from django.template import loader
from .auth import CustomJWTAuthentication

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken




import stripe

# PUBLIC API VIEWS
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class MoneyView(generics.RetrieveAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer 



class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

    # Override
    def create(self, request, *args, **kwargs):

        # find / create the client account
        # print("ORDER INCOMMING DATA",request.data)
        client = Client.objects.filter(phone=request.data['client_phone']).first()
        # print("FOUND BY EMAIL",client)
        if client == None:
            client = Client.objects.filter(email=request.data['client_email']).first()
            # print("FOUND BY PHONE",client)
        if client == None:
            client = Client.objects.create(
                # User model
                password = '',  # just an idea - could generate this as shor pin
                is_superuser = False,
                username = request.data['client_email'],
                first_name = '',
                last_name = '',
                email = request.data['client_email'],
                is_staff = False,
                # extended Client
                phone = request.data['client_phone'], 

            )       

       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # this creates the Order objet
        self.perform_create(serializer)
        order = Order.objects.get(pk = serializer.data.get('id'))
        order.client = client
        order.save()

        # CUSTOM: OrderItem creation here
        product_id =  kwargs.get('uuid')

        order_item = OrderItem (
            product = Product.objects.get(pk = product_id), 
            order = order
        )
        
        order_item.save()
        # CUSTOM: OrderItem creation here

        headers = self.get_success_headers(serializer.data)

        access_token = AccessToken.for_user(client)
        access_token['order_id'] = str(order.id)

        # print("TOKEN",access_token) 

        response = {'access': str(access_token), 'id': order.id}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
    









# B[R]EAD
class OrderRView(
                  generics.RetrieveAPIView,
                ):
    
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer 






class PaymentView(APIView):
    # HW*: could use token authentication here
    def get(self, request, *args, **kwargs):
        order_id =  kwargs.get('pk')
        stripe.api_key = "sk_test_6FRLqRGKysXgFEslhoragL8o"    

        # HW*: get the price from the db
        price = stripe.Price.create(
            currency="usd",
            unit_amount=1000,
            recurring={"interval": "month"},
            product_data={"name": order_id},
        )    

        payment_link = stripe.PaymentLink.create(
            line_items=[
                {"price": price['id'], "quantity": 1}
            ],
            after_completion= {
                'type' : 'redirect',
                'redirect'  : {
                    'url': f'http://127.0.0.1:8000/payment/confirm/{order_id}'
                }
            }
        )

        return Response(payment_link, status=status.HTTP_201_CREATED) 