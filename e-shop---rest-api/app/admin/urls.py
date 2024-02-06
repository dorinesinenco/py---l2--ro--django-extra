from django.urls import path

from .views import *

# administrative routes
urlpatterns = [
   path('products/<uuid:pk>', ProductREADView.as_view()),
   path('products/', ProductBView.as_view()),
]
