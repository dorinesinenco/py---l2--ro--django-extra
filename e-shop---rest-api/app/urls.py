from django.urls import path, include

urlpatterns = [
    path('admin/', include('app.admin.urls')),       
    path('', include('app.client.urls')),       
]
