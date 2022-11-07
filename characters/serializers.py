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
from ipdb import set_trace

class CharacterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    name = serializers.CharField(max_length=20)
    level = serializers.IntegerField(default=1, allow_null=True)
    silver = serializers.IntegerField(default=100, allow_null=True)
    gold = serializers.IntegerField(default=20, allow_null=True)
    
    _class = serializers.CharField(max_length=50, write_only=True)
    _equipments = serializers.ListField(write_only=True)
    _skills = serializers.ListField(write_only=True)

    char_class = ClassSerializer(read_only=True)
    equipments = EquipmentSerializer(read_only=True)
    skills = Skill_Serializer(read_only=True)

    auth_token = serializers.CharField(write_only=True)
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
            'skills',
            '_class',
            '_equipments',
            '_skills',
            'auth_token'
        ]

    def create(self, validated_data):
        character_owner = Token.objects.get(key=validated_data['auth_token']).user
        
        equipments_list = validated_data.pop('_equipments')
        skills_list = validated_data.pop('_skills')
        token = validated_data.pop('auth_token')
        _class = validated_data.pop('_class')

        try:
            character_exist = Character.objects.get(name=validated_data['name'])
        except Character.DoesNotExist:
            character_exist = None

        if character_exist:
            raise PermissionDenied()
        
        character_class = Class.objects.get(name=_class)
        if not character_class:
             raise Http404("Class not found.")

        created_character = Character.objects.create(
            **validated_data,
            char_class_id=character_class.id,
            owner_id=character_owner.id
        )

        for equipment in equipments_list:
            equipment_obj, _ = Equipment.objects.get(
                name=equipment["name"]
            )

            equip_name = equipment["name"]
            if not equipment_obj:
                raise Http404(f"Equipment '{equip_name}' not found.")
            
            created_character.equipments.add(equipment_obj)

        for skill in skills_list:
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