from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response
from rest_framework.pagination import PageNumberPagination
from .serializers import CharacterSerializer
from django.http import Http404
from .models import Character
from django.shortcuts import get_object_or_404
from .errors import Class404
from equipments.permissions import IsSuperUserOrReadOnly

class CharactersView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = CharacterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user=self.request.user)
        except Class404:
            return Response({"detail": "Class not found."}, 404)

        return Response(serializer.data, 201)

    def get(self, request: Request) -> Response:
        characters = Character.objects.all()
        result_page = self.paginate_queryset(characters, request, view=self)
        serializer = CharacterSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)


class SpecificCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request: Request, character_id) -> Response:
        character = get_object_or_404(Character, id=character_id)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def delete(self, request: Request, character_id) -> Response:
        character = try_get(character_id)
        character.delete()
        return Response({}, 204)

    def patch(self, request: Request, character_id) -> Response:
        character = try_get(character_id)
        serializer = CharacterSerializer(character, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


def try_get(id):
    try:
        return Character.objects.get(id=id)
    except Character.DoesNotExist:
        raise Http404