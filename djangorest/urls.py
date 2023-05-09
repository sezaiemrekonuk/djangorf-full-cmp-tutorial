from django.urls import include, path
from api import views

urlpatterns = [
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
