from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from classes.models import Class


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class

        fields = [
            "id",
            "name",
            "life",
            "attack",
            "defense",
            "mana",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Class.objects.all(), message="name alredy exists"
                    )
                ]
            },
        }

        depth = 1

    def create(self, validated_data):

        return Class.objects.create(**validated_data)
