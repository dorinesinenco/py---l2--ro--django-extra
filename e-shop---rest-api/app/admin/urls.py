from django.urls import path

from .views import *



urlpatterns = [
   # administrative API routes 
   path("products/image", ProductImageAView.as_view()),

   path('products/<uuid:pk>', ProductREDView.as_view()),
   path('products/', ProductBAView.as_view()),


   path('money/<uuid:pk>', MoneyREDView.as_view()),

   # ideally - regular expression of a list of uuids separated by comma
   path('money/multi/<str:pks>', MoneyBCustomView.as_view()),  # GET /money/1,2,3,4...
   path('images/multi/<str:pks>', ImagesBCustomView.as_view()),  # GET /money/1,2,3,4...

   path('money/', MoneyBAView.as_view()),

   # administrative TEMPLATE routes / pages
   path('products-page', productPage),
   path('orders-page', orderPage)
]
