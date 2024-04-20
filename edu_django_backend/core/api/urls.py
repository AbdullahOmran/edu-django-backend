
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import Register
schema_view = get_schema_view(
    openapi.Info(
        title="Edu API Documentation",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('auth/token/',MyTokenObtainPairView.as_view(), name = 'auth-token' ),
    path('auth/refresh/',TokenRefreshView.as_view(), name = 'auth-refresh' ),
    path('auth/register/',Register.as_view(), name = 'auth-register' ),
    # path('auth/logout/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/forgot-password/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/reset-password/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/verify/',TokenRefreshView.as_view(), name = 'token-refresh' ),
    # path('auth/login/',TokenRefreshView.as_view(), name = 'token-refresh' ),
]
