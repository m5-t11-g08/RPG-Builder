from django.db.utils import IntegrityError
from django.test import TestCase

from characters.models import Character
from users.models import User
from classes.models import Class

class ModelCharacterTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
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

        cls.character_data = {
            "name": "character",
            "level": 1,
            "silver": 100,
            "gold": 100, 
            "char_class_id": cls.classe.id,
            "user_id": cls.user.id
        }
        cls.character = Character.objects.create(**cls.character_data, user=cls.user, char_class=cls.classe)


    def test_name_character_is_unique(self):
        """"Verifica se o nome do personagem é único"""
        expected_msg = 'duplicate key value violates unique constraint "characters_character_name_key"'
        with self.assertRaisesMessage(IntegrityError, expected_msg):
            Character.objects.create(**self.character_data)
    

    def test_pk_is_uuid(self):
        """"Verifica se a chave primaria é um UUID"""
        length_expected = 32
        result = Character._meta.get_field("id").max_length

        self.assertEquals(length_expected, result)