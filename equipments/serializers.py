from rest_framework import serializers
# from characters.models import Character
from equipments.models import Equipment
from characters.models import Character


class EquipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    durability = serializers.IntegerField()
    add_attack = serializers.IntegerField(default=0)
    add_defense = serializers.IntegerField(default=0)
    add_mana = serializers.IntegerField(default=0)
    add_life = serializers.IntegerField(default=0)
    category = serializers.CharField()

    def create(self, validated_data):
        list_characters = []
        if "characters" in validated_data:
            characters = validated_data.pop("characters")

            for character in characters:
                obj, _ = Character.objects.get_or_create(**character)
                list_characters.append(obj)

            characters_obj = Equipment.objects.create(**validated_data)
            characters_obj.characters.set(list_characters)

        else:
            characters_obj = Equipment.objects.create(**validated_data)


        return characters_obj


    def update(self, instance: Equipment, validated_data):
        if "characters" in validated_data:
            characters = validated_data.pop("characters")
            for key, value in validated_data.items():
                setattr(instance, key, value)
            equip = instance.save()
            for character in characters:
                obj, _ = Character.objects.get_or_create(**character)
                obj.equipments.add(equip)
            return instance