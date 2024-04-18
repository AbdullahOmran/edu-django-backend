
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path,include

urlpatterns = [
    path('token/',MyTokenObtainPairView.as_view(), name = 'token' ),
    path('token/refresh/',TokenRefreshView.as_view(), name = 'token-refresh' ),
]
