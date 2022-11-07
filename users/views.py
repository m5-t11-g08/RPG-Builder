from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import Request, Response, status, APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import OwnAccountOrReadOnlyPermission, OwnAccountPermission
from .serializers import UserSerializer, LoginSerializer, UserDetailSerializer, UserUpdatePasswordSerializer
from .models import User


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnAccountOrReadOnlyPermission]

    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserUpdatePasswordView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnAccountPermission]

    serializer_class = UserUpdatePasswordSerializer
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