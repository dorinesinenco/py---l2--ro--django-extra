from django.urls import path, include

urlpatterns = [
    path('admin/', include('app.admin.urls')),       
]































# urlpatterns = [
#     # path('admin/', admin.site.urls),


#     # PUBLIC ROUTES
#     path('', indexPage),

#     path('products', ProductView.as_view()),
#     path('orders/<uuid:uuid>', CreateOrderView.as_view()),
#     path('money/<uuid:pk>', MoneyView.as_view()),

# ]
