from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from users.models import User


class UserViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.register_url = "/api/user/"
        cls.login_url = "/api/user/login/"
        cls.listall_listone_update_delete = "/api/user/"
        cls.update_password_url = "/api/user/password/"

        cls.user_data = {
            "username": "suzuki",
            "password": "1234",
            "email": "teste@suzuki.com"
        }

        cls.second_user = {
            "username": "suzuki2",
            "password": "1234",
            "email": "suzuki@suzuki.com"
        }

        cls.user_wrong_email = {
            "username": "suzuki2",
            "password": "1234",
            "email": "teste"
        }

        cls.login_data = {
            "username": "suzuki",
            "password": "1234"
        }

        cls.login_wrong_data = {
            "username": "errado",
            "password": "errado"
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)

        expected_status_code = status.HTTP_201_CREATED
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)


    def test_register_without_keys(self):
        response = self.client.post(self.register_url, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data["username"][0], "This field is required.")
        self.assertEqual(response.data["password"][0], "This field is required.")
        self.assertEqual(response.data["email"][0], "This field is required.")


    def test_register_username_exists(self):
        response = self.client.post(self.register_url, self.user_data)
        response_exists = self.client.post(self.register_url, self.user_data)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        response_status_code = response_exists.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response_exists.data["username"][0], "user with this username already exists.")
        self.assertEqual(response_exists.data["email"][0], "user with this email already exists.")


    def test_register_wrong_email(self):
        response = self.client.post(self.register_url, self.user_wrong_email)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data["email"][0], "Enter a valid email address.")


    def test_login_user(self):
        response = self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, self.login_data)

        expected_status_code = status.HTTP_200_OK
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertIn("token", response.data)


    def test_login_wrong_data(self):
        response = self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, self.login_wrong_data)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data["detail"], "wrong username or password")


    def test_login_without_keys(self):
        response = self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data["username"][0], "This field is required.")
        self.assertEqual(response.data["password"][0], "This field is required.")


    def test_list_all(self):
        response = self.client.get(self.listall_listone_update_delete)

        expected_status_code = status.HTTP_200_OK
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)


    def test_list_one(self):
        user = User.objects.create_user(**self.user_data)

        response = self.client.get(f'{self.listall_listone_update_delete}{user.id}/')

        expected_status_code = status.HTTP_200_OK
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)


    def test_list_one_nonexistent_id(self):
        response = self.client.get(f'{self.listall_listone_update_delete}418374faskjf12oa87/')

        expected_status_code = status.HTTP_404_NOT_FOUND
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], 'Not found.')


    def test_patch_not_owner(self):
        owner = User.objects.create_user(**self.user_data)

        not_owner = User.objects.create_user(**self.second_user)
        not_owner_token = Token.objects.create(user=not_owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + not_owner_token.key)

        response = self.client.patch(f'{self.listall_listone_update_delete}{owner.id}/', data={"username": "not owner"})

        expected_status_code = status.HTTP_403_FORBIDDEN
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], 'You do not have permission to perform this action.')
    
    def test_patch_wrong_id(self):
        owner = User.objects.create_user(**self.user_data)
        owner_token = Token.objects.create(user=owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + owner_token.key)

        response = self.client.patch(f'{self.listall_listone_update_delete}4128faskjbfk1h231/', data={"username": "wrong id"})

        expected_status_code = status.HTTP_404_NOT_FOUND
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], "Not found.")


    def test_patch_wrong_token(self):
        owner = User.objects.create_user(**self.user_data)

        self.client.credentials(HTTP_AUTHORIZATION="Token 187rkhqgkhg12")

        response = self.client.patch(f'{self.listall_listone_update_delete}{owner.id}/', data={"username": "wrong token"}) 

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], "Invalid token.")


    def test_patch(self):
        owner = User.objects.create_user(**self.user_data)
        owner_token = Token.objects.create(user=owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + owner_token.key)

        response = self.client.patch(f'{self.listall_listone_update_delete}{owner.id}/', data={"username": "username patch"})

        expected_status_code = status.HTTP_200_OK
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['username'], 'username patch')


    def test_patch_password(self):
        owner = User.objects.create_user(**self.user_data)
        owner_token = Token.objects.create(user=owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + owner_token.key)

        response = self.client.patch(f'{self.update_password_url}{owner.id}/', data={"password": "new password"})

        expected_status_code = status.HTTP_200_OK
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)


    def test_delete_not_owner(self):
        owner = User.objects.create_user(**self.user_data)

        not_owner = User.objects.create_user(**self.second_user)
        not_owner_token = Token.objects.create(user=not_owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + not_owner_token.key)

        response = self.client.delete(f'{self.listall_listone_update_delete}{owner.id}/')

        expected_status_code = status.HTTP_403_FORBIDDEN
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], 'You do not have permission to perform this action.')

    
    def test_delete_wrong_id(self):
        owner = User.objects.create_user(**self.user_data)
        owner_token = Token.objects.create(user=owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + owner_token.key)

        response = self.client.delete(f'{self.listall_listone_update_delete}414k271dhi2/')

        expected_status_code = status.HTTP_404_NOT_FOUND
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], 'Not found.')

    
    def test_delete_wrong_token(self):
        owner = User.objects.create_user(**self.user_data)

        self.client.credentials(HTTP_AUTHORIZATION="Token 798fas2h412")

        response = self.client.delete(f'{self.listall_listone_update_delete}{owner.id}/')

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)
        self.assertEqual(response.data['detail'], 'Invalid token.')


    def test_delete(self):
        owner = User.objects.create_user(**self.user_data)
        owner_token = Token.objects.create(user=owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + owner_token.key)

        response = self.client.delete(f'{self.listall_listone_update_delete}{owner.id}/')

        expected_status_code = status.HTTP_204_NO_CONTENT
        response_status_code = response.status_code

        self.assertEqual(expected_status_code, response_status_code)