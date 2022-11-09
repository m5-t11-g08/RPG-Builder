from users.models import User
from characters.models import Character
from classes.models import Class
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "suzuki",
            "password": "1234",
            "email": "suzuki@teste.com",
        }

        cls.class_data = {
            "name": "mago",
            "life": 100,
            "attack": 100,
            "defense": 10,
            "mana": 50
        }

        cls.create_class = Class.objects.create(**cls.class_data)

        cls.character_data = {
            "name": "char2",
            "level": 1,
            "silver": 100,
            "gold": 100,
            "char_class_id": cls.create_class.id
        }   

        cls.user = User.objects.create_user(**cls.user_data)
        cls.character = Character.objects.create(**cls.character_data, user=cls.user)
    
    def test_atributes_max_length(self):
        username = self.user._meta.get_field("username").max_length
        email = self.user._meta.get_field("email").max_length

        self.assertEqual(username, 20)
        self.assertEqual(email, 80)

    
    def test_atributes_unique(self):
        username = self.user._meta.get_field("username").unique
        email = self.user._meta.get_field("email").unique

        self.assertTrue(username)
        self.assertTrue(email)

    
    def test_user_fields(self):
        self.assertEqual(self.user.username, self.user_data["username"])
        self.assertEqual(self.user.email, self.user_data["email"])


    def test_one_to_one_character(self):
        character_count = Character.objects.count()
        expected_count = 1

        self.assertEqual(character_count, expected_count)
