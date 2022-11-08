from users.models import User
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "suzuki",
            "password": "1234",
            "email": "suzuki@teste.com",
        }

        cls.user = User.objects.create_user(**cls.user_data)

    
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