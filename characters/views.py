from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response
from .serializers import CharacterSerializer
from .permissions import IsAdminOrReadOnly, IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from .models import Character

class CharactersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request: Request) -> Response:
        request.data["auth_token"] = str(request.auth)
        serializer = CharacterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)

    
    def get(self, request: Request) -> Response:
        serializer = CharacterSerializer(Character.objects.all(), many=True)
        return Response(serializer.data)

class SpecificCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly | IsOwner]

    def get(self, request: Request, character_id) -> Response:
        character = try_get(character_id)
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