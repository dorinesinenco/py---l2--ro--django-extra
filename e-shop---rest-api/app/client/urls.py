from django.urls import path, include

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from .views_api import *
from .views_pages import *

urlpatterns = [
    # PUBLIC ROUTES
    path('', indexPage),

    path('products', ProductView.as_view()),
    path('money/<uuid:pk>', MoneyView.as_view()),




    path('orders/<uuid:uuid>', CreateOrderView.as_view()),

    # TOKEN CLIENT ROUTES
    # path('client/token', TokenObtainPairView.as_view()),

    
    path('client/pay/<uuid:pk>', PaymentView.as_view()),
    # AUTHENTICATED CLIENT ROUTES
    path('client/orders/<uuid:pk>', OrderRView.as_view()),
]
