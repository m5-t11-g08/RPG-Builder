from rest_framework import serializers
from classes.serializer import ClassSerializer
from rest_framework.authtoken.models import Token
from equipments.serializers import EquipmentSerializer
from django.core.exceptions import PermissionDenied
from skills.serializers import Skill_Serializer
from equipments.models import Equipment
from classes.models import Class
from skills.models import Skill
from django.http import Http404
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    name = serializers.CharField(max_length=20)
    level = serializers.IntegerField(default=1, allow_null=True)
    silver = serializers.IntegerField(default=100, allow_null=True)
    gold = serializers.IntegerField(default=20, allow_null=True)
    
    char_class = ClassSerializer()
    equipments = EquipmentSerializer()
    skills = Skill_Serializer()
    # stats = StatsSerializer

    class Meta:
        model = Character
        fields = [
            'id',
            'name',
            'level',
            'silver',
            'gold',
            'char_class',
            'equipments',
            'skills'
        ]

    def create(self, validated_data):
        character_owner = Token.objects.get(key=validated_data['auth_token']).user
        equipments = validated_data["equipments"]
        skills = validated_data["skills"]

        validated_data.pop('equipments')
        validated_data.pop('auth_token')

        characters = Character.objects.get(name=validated_data['name'])
        if characters:
            raise PermissionDenied()
        
        character_class = Class.objects.get(name=validated_data['class'])
        if not character_class:
            raise Http404("Class not found.")

        created_character = Character.objects.create(**validated_data, char_class=character_class)

        for equipment in equipments:
            equipment_obj, _ = Equipment.objects.get(
                name=equipment["name"]
            )

            equip_name = equipment["name"]
            if not equipment_obj:
                raise Http404(f"Equipment '{equip_name}' not found.")
            
            created_character.equipments.add(equipment_obj)

        for skill in skills:
            skill_obj, _ = Skill.objects.get(
                name=equipment["name"]
            )

            skill_name = skill["name"]
            if not skill_obj:
                raise Http404(f"Skill '{skill_name}' not found.")
            
            created_character.skills.add(skill_obj)

        return created_character


    def update(self, instance, validated_data):
        for attr in validated_data:
            setattr(instance, attr, validated_data.get(attr, instance.__dict__[attr]))

        instance.save()
        return instance