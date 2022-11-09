from rest_framework import serializers
from .models import Attribute
from characters.serializers import CharacterSerializer

class AttributeSerializer(serializers.ModelSerializer):
    character = CharacterSerializer()

    class Meta:
        model = Attribute
        fields = "__all__"


    def create(self, validated_data):
        attribute = Attribute.objects.create(**validated_data)
        attribute.save()

        return attribute