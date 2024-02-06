# from django.contrib import admin
from django.urls import path

from .views import ProductView, CreateOrderView, ProductAdminView, MoneyView, indexPage

urlpatterns = [
    # path('admin/', admin.site.urls),


    # PUBLIC ROUTES
    path('', indexPage),

    path('products', ProductView.as_view()),
    path('orders/<uuid:uuid>', CreateOrderView.as_view()),
    path('money/<uuid:pk>', MoneyView.as_view()),


    # ADMIN ROUTES
    path('admin/products', ProductAdminView.as_view()),
]
