from rest_framework import serializers
from .models import Character
from classes.serializer import ClassSerializer
from classes.models import Class


class CharacterSerializer(serializers.ModelSerializer):
    char_class_id = serializers.CharField(write_only=True)
    char_class = ClassSerializer(read_only=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "level",
            "silver",
            "gold",
            "char_class",
            "char_class_id"
        ]
    # char_class = CharClassSerializer
    # equipments = EquipmentsSerializer
    # skills = SkillsSerializer
    # stats = StatsSerializer


    def create(self, validated_data):
        char_class_id = validated_data.pop("char_class_id")

        char_class, _ = Class.objects.get_or_create(id=char_class_id)

        character = Character.objects.create(**validated_data, char_class=char_class)
 
        return character


    def update(self, instance, validated_data):
        for attr in validated_data:
            setattr(instance, attr, validated_data.get(attr, instance.__dict__[attr]))

        instance.save()
        return instance