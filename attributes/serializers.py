from rest_framework import serializers
from .models import Attribute
from characters.serializers import CharacterSerializer

class AttributeSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(read_only=True)

    class Meta:
        model = Attribute
        fields = "__all__"


    def create(self, validated_data):
        attribute, _ = Attribute.objects.get_or_create(**validated_data)
        attribute.save()
        return attribute


class AttributeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = [
            "id",
            "character_id",
            "life",
            "attack",
            "defense",
            "mana",
        ]

        read_only_fields = ["id", "character_id"]