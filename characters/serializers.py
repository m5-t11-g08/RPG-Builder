from rest_framework import serializers

class CharacterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    name = serializers.CharField(max_length=20)
    level = serializers.IntegerField()
    silver = serializers.IntegerField()
    gold = serializers.IntegerField()
    
    # char_class = CharClassSerializer
    # equipments = EquipmentsSerializer
    # skills = SkillsSerializer
    # stats = StatsSerializer


    def update(self, instance, validated_data):
        for attr in validated_data:
            setattr(instance, attr, validated_data.get(attr, instance.__dict__[attr]))

        instance.save()
        return instance