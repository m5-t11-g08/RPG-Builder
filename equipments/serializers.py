from rest_framework import serializers
from characters.models import Character
from equipments.models import Equipment
from rest_framework.views import Response, status
from django.http import Http404

class EquipmentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=30)
    durability = serializers.IntegerField()
    add_attack = serializers.IntegerField(default=0)
    add_defense = serializers.IntegerField(default=0)
    add_mana = serializers.IntegerField(default=0)
    add_life = serializers.IntegerField(default=0)
    category = serializers.CharField()
    characters = serializers.ListField(default=None, write_only=True)

    def create(self, validated_data):
        if "characters" in validated_data:
            validated_data.pop("characters")
        equipment = Equipment.objects.create(**validated_data)
        return equipment


    def update(self, instance: Equipment, validated_data):
        if "characters" in validated_data:
            characters = validated_data.pop("characters")
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            for character in characters:
                # import ipdb
                # ipdb.set_trace()
                try:
                    obj = Character.objects.get(name=character)
                    obj.equipments.add(instance)
                    
                except Character.DoesNotExist:
                    raise Http404
        else:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
        return instance