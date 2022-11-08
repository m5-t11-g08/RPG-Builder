from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework.views import Response, APIView, Request
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from .serializers import AttributeSerializer
from .models import Attribute
from characters.models import Character

class AttributesRetrieveCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request, character_id: int) -> Response:
        character = get_object_or_404(Character, id=character_id)
        class_character = character.classes
        equipaments = character.equipaments

        life, mana, atack, defense = 0

        for att in class_character:
            if att == "life":
                life += att
            if att == "mana":
                mana += att
            if att == "atack":
                atack += att
            if att == "defense":
                defense += att

        for equipament in equipaments:
            for att in equipament:
                if att == "life":
                    life += att
                if att == "mana":
                    mana += att
                if att == "atack":
                    atack += att
                if att == "defense":
                    defense += att

        result = {
            "life": life,
            "atack": atack,
            "defense": defense,
            "mana": mana,
            "character": character
        }

        serializer = AttributeSerializer(data=result)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

class GetAttributes(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer