from rest_framework import serializers
from .models import Attribute

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


    def create(self, validated_data):
        attribute = Attribute.objects.create(**validated_data)
        # validated_data['character']
        import ipdb
        ipdb.set_trace()
        return attribute