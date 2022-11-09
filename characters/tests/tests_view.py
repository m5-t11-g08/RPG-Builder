from rest_framework.test import APITestCase
from rest_framework.views import status
from django.test import Client
from users.models import User
from classes.models import Class
from rest_framework.test import APIClient
from characters.models import Character

class CharacterRegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()

        cls.register_url = "/api/character/"
        cls.login_url = "/api/user/login/"

        cls.user_data = {
            "username": "user",
            "email": "user@mail.com",
            "password": "1234",
        }
        cls.user = User.objects.create_superuser(**cls.user_data)

        cls.class_data = {
            "name": "mago",
            "life": 100,
            "attack": 100,
            "defense": 10,
            "mana": 50
        }

        cls.classe = Class.objects.create(**cls.class_data)

        cls.user_login = {
        "username": "user",
        "password": "1234"
        }

        cls.token = cls.client.post(cls.login_url, cls.user_login)
    
        cls.token = cls.token.data["token"]

        cls.client2 = APIClient()
        cls.client2.credentials(HTTP_AUTHORIZATION=f"Token {cls.token}")

        cls.character_data = {
            "name": "character",
            "level": 1,
            "silver": 10,
            "gold": 1000,
            "char_class_id": cls.classe.id
        }
        
        cls.response_create_character = cls.client2.post(cls.register_url, cls.character_data)

    def test_can_register_character(self):
        """"Verifica criação de um personagem"""

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = self.response_create_character.status_code

        self.assertEqual(expected_status_code, result_status_code)

        character_count = Character.objects.count()
        expected_count = 1

        self.assertEqual(expected_count, character_count)

    def test_initial_gold_character(self):
        """"Verifica se a quantidade inicial de ouro está correta"""

        print("="*100)
        print(self.response_create_character)
        print("="*100)
        expected_gold = 1000
        gold_character = self.response_create_character.data["gold"]

        self.assertEqual(expected_gold, gold_character)

    def test_initial_silver_character(self):
        """"Verifica se a quantidade inicial de rubís está correta"""

        expected_silver = 10
        silver_character = self.response_create_character.data["silver"]

        self.assertEqual(expected_silver, silver_character)

    def test_initial_level_character(self):
        """"Verifica level inicial do personagem"""

        expected_level = 1
        level_character = self.response_create_character.data["level"]

        self.assertEqual(expected_level, level_character)

    def test_initial_equipaments_character(self):
        """"Verifica se o personagem começa sem nenhum equipamento"""

        expected_equipaments = []
        equipaments_character = self.response_create_character.data["equipments"]

        self.assertEqual(expected_equipaments, equipaments_character)

    def test_patch_character(self):
        """"Verifica se é possível att um personagem"""
        character = Character.objects.first()
        response_patch = self.client2.patch(f"/api/character/{character.id}/", {"name": "character patched"})

        expected_status_code = status.HTTP_200_OK
        result_status_code = response_patch.status_code

        self.assertEqual(expected_status_code, result_status_code)

        expected_name = "character patched"
        atual_name = response_patch.data["name"]

        self.assertEqual(expected_name, atual_name)

    def test_get_characters(self):
        """"Verifica se o get de todos personagens está correto"""
        response_get = self.client2.get(self.register_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response_get.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_retrieve_get_character(self):
        """"Verifica se o get de um único personagem está correto"""
        character = Character.objects.first()
        response_get = self.client2.get(f'/api/character/{character.id}/')

        expected_status_code = status.HTTP_200_OK
        result_status_code = response_get.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_retrieve_delete_character(self):
        """"Verifica se o delete de um personagem está correto"""
        character = Character.objects.first()
        response_delete = self.client2.delete(f'/api/character/{character.id}/')

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response_delete.status_code

        self.assertEqual(expected_status_code, result_status_code)


class CharacterRegisterIncorrectKeysViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.register_url = "/api/character/"
        cls.login_url = "/api/user/login/"

        cls.user_data = {
            "username": "user",
            "email": "user@mail.com",
            "password": "1234",
        }
        cls.user = User.objects.create_superuser(**cls.user_data)

        cls.class_data = {
            "name": "mago",
            "life": 100,
            "attack": 100,
            "defense": 10,
            "mana": 50
        }

        cls.classe = Class.objects.create(**cls.class_data)

        cls.user_login = {
        "username": "user",
        "password": "1234"
        }

        cls.token = cls.client.post(cls.login_url, cls.user_login)
        cls.token = cls.token.data["token"]

        cls.client2 = APIClient()
        cls.client2.credentials(HTTP_AUTHORIZATION=f"Token {cls.token}")

        cls.character_data = {}
        
    def test_incorrect_keys_register_character(self):
        """"Verifica se é possível cadastrar um personagem sem as informações necessárias"""
        response_create_character = self.client2.post(self.register_url, self.character_data)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response_create_character.status_code

        self.assertEqual(expected_status_code, result_status_code)

        character_count = Character.objects.count()
        expected_count = 0

        self.assertEqual(expected_count, character_count)

        expected_keys = {"name", "char_class_id", "level", "silver", "gold"}
        result_keys = set(response_create_character.data.keys())

        self.assertEqual(expected_keys, result_keys)