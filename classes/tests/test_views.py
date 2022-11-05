from rest_framework.test import APITestCase
from classes.models import Class
from rest_framework.authtoken.models import Token
from rest_framework.views import status, Response


class ClassViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user_admin_data = {
            "username": "ana",
            "password": 1234,
            "email": "ana@mail.com",
        }
        cls.user_not_admin_data = {
            "username": "pedro",
            "password": 1234,
            "email": "pedro@mail.com",
        }
        cls.class_data = {
            "name": "magus",
            "life": 30,
            "defense": 9,
            "attack": 20,
            "mana": 1,
        }
        cls.class_data_1 = {}

        cls.user_admin = User.objects.create_superuser(**cls.user_admin_data)
        cls.token_admin = Token.objects.create(user=cls.user_admin)

        cls.user_not_admin = User.objects.create_user(**cls.user_not_admin_data)
        cls.token_not_admin = Token.objects.create(user=cls.user_not_admin)

    def test_can_register_classes(self):
        """
        Verifica a somente superuser pode criar uma class
        """
        register_url = "/api/classes/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        response = self.client.post(register_url, self.class_data)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code
        msg = f"Verifique se o status_code da criação de uma class foi definido como {expected_status_code}"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_keys_register_classes(self):
        """
        Verifica se as keys passadas estão corretas
        """
        register_url = "/api/classes/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin.key)

        response = self.client.post(register_url, self.class_data_1)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = f"Verifique se as keys passadas em create estão corretas"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_can_list_all_classes(self):
        """
        Verifica se é possivel qualquer user pode listar todas as classes
        """
        register_url = "/api/classes/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        response = self.client.get(register_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code
        msg = f"Verifique se qualquer user pode listar todas as classes "

        self.assertEqual(expected_status_code, result_status_code, msg)


class ClassViewDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user_admin_data = {
            "username": "ana",
            "password": 1234,
            "email": "ana@mail.com",
        }
        cls.user_not_admin_data = {
            "username": "pedro",
            "password": 1234,
            "email": "pedro@mail.com",
        }
        cls.class_data = {
            "name": "magus",
            "life": 30,
            "defense": 9,
            "attack": 20,
            "mana": 1,
        }

        cls.user_admin = User.objects.create_superuser(**cls.user_admin_data)
        cls.token_admin = Token.objects.create(user=cls.user_admin)

        cls.user_not_admin = User.objects.create_user(**cls.user_not_admin_data)
        cls.token_not_admin = Token.objects.create(user=cls.user_not_admin)

        cls.classe = Class.objects.create(**cls.class_data)

        cls.character_data = {
            "name": "mago",
            "class": cls.classe.id
        }
        cls.character_data_2 = {
            "name": "dragon",
            "class": cls.classe.id
        }
        cls.character = Character.objects.create(**cls.character_data, user=cls.user_admin)
        cls.character_not_admin = Character.objects.create(**cls.character_data_2, user=cls.user_not_admin)

    def test_can_list_detail_class(self):
        """
        Verifica se é possivel listar class pelo id
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin.key)

        response = self.client.get(register_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code
        msg = f"Verifique se  leitura de class foi definido como {expected_status_code}"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_can_updated_class(self):
        """
        Verifica se é possivel somente superuser atualizar class
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        data_update = {"mana": 5}

        response = self.client.patch(register_url, data_update)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code
        msg = f"Verifique se somente superuser pode atualizar class"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_keys_patch_class(self):
        """
        Verifica se as keys passadas em update estão corretas
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_admin.key)

        data_update = {}

        response = self.client.patch(register_url, data_update)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = f"Verifique se as keys passadas em update estão corretas"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_status_code_update_class(self):
        """
        Verifica se o status code de patch class está correto
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        data_update = {"mana": 5}

        response = self.client.patch(register_url, data_update)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code
        msg = f"Verifique se o status code de patch class está correto {expected_status_code}"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_can_deleted_class(self):
        """
        Verifica se é possivel somente superuser deletar class
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        response = self.client.delete(register_url)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code
        msg = f"Verifique se somente superuser pode deletar class"

        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_status_code_delete_class(self):
        """
        Verifica se o status code de delete class está correto
        """
        register_url = f"/api/classes/{self.user_admin.id}/"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_not_admin.key)

        response = self.client.delete(register_url)

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code
        msg = f"Verifique se o status code de delete class está correto {expected_status_code}"

        self.assertEqual(expected_status_code, result_status_code, msg)
