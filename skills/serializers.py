from characters.models import Character
from rest_framework import serializers
from django.http import Http404
from .models import Skill

class Skill_Serializer(serializers.ModelSerializer):
    characters = serializers.ListField(default=None)

    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'damage',
            'mana_cost',
            'characters'
        ]

        # extra_kwargs = {'id': {'read_only': True}}

    # def create(self, validated_data:dict) -> Skill:
    #     new_skill = Skill.objects.create(**validated_data)
    #     return new_skill

    def update(self, instance: Skill, validated_data):
        if "characters" in validated_data:
            characters = validated_data.pop("characters")
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            for character in characters:
                try:
                    obj = Character.objects.get(name=character)
                    obj.skills.add(instance)
                    
                except Character.DoesNotExist:
                    raise Http404
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
        return instance