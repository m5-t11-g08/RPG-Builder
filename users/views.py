from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import Request, Response, status, APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LoginSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response({"detail": "wrong username or password"}, status.HTTP_400_BAD_REQUEST)