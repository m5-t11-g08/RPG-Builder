from rest_framework import serializers
from .models import Character
from classes.serializer import ClassSerializer
from classes.models import Class
from users.serializers import UserSerializer
from equipments.serializers import EquipmentSerializer
from skills.serializers import Skill_Serializer
from django.http import Http404
from .errors import Class404

class CharacterSerializer(serializers.ModelSerializer):
    char_class_id = serializers.CharField(write_only=True)
    char_class = ClassSerializer(read_only=True)
    equipments = EquipmentSerializer(many=True, read_only=True)
    skills = Skill_Serializer(many=True, read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "level",
            "silver",
            "gold",
            "char_class",
            "char_class_id",
            "user_id",
            "equipments",
            "skills"
        ]

        read_only_fields = [
            "equipments",
            "skills"
        ]
    # char_class = CharClassSerializer
    # equipments = EquipmentsSerializer
    # skills = SkillsSerializer
    # stats = StatsSerializer


    def create(self, validated_data):
        char_class_id = validated_data.pop("char_class_id")

        try:
            char_class = Class.objects.get(id=char_class_id)
        except Class.DoesNotExist:
            raise Class404()

        character = Character.objects.create(**validated_data, char_class=char_class)
 
        return character


    def update(self, instance, validated_data):
        for attr in validated_data:
            setattr(instance, attr, validated_data.get(attr, instance.__dict__[attr]))

        instance.save()
        return instance