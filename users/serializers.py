from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser"
        ]

    
    def create(self, validated_data:dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_superuser"
        ]

        read_only_fields = ["id"]

    
class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser"
        ]

        read_only_fields = ["id", "username", "email", "is_superuser"]


    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance