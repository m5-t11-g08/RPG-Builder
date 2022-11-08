from django.shortcuts import render
import ipdb
from rest_framework.permissions import IsAdminUser
from rest_framework.views import Response, status, APIView, Request
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from .serializers import AttributeSerializer
from .models import Attribute
from characters.models import Character
from classes.serializer import ClassSerializer
from equipments.serializers import EquipmentSerializer

class AttributesRetrieveCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    def get(self, request: Request, character_id: str) -> Response:
        character = get_object_or_404(Character, id=character_id)
        class_character = ClassSerializer(character.char_class)
        equipaments = EquipmentSerializer(character.equipments, many=True)


        life = 0
        mana = 0
        attack = 0
        defense = 0

        for key, value in class_character.data.items():
            if key == "life":
                life += value
            if key == "mana":
                mana += value
            if key == "attack":
                attack += value
            if key == "defense":
                defense += value

        for equipament in equipaments.data:
            for key, value in equipament.items():
                if key == "add_life":
                    life += value
                if key == "add_mana":
                    mana += value
                if key == "add_attack":
                    attack += value
                if key == "add_defense":
                    defense += value

        result = {
            "life": life,
            "attack": attack,
            "defense": defense,
            "mana": mana,
            "character": character
        }

        serializer = AttributeSerializer(data=result)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        # attributes = Attribute.objects.create(**result, character=character)

        # character.attributes.add(attributes)

        return Response(serializer.data)

class GetAttributes(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer