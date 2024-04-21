from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Register(APIView):

  
    def post(self, request, format=None):
        """
        Register a new user
        """
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors,status=status.HTTP_201_CREATED)
