from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from skills.models import Skill
from users.models import User

# python manage.py test skills.tests.tests_views
# .\venv\Scripts\activate 

class SkillViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # routes
        cls.get_routes = "/api/skills/"
        cls.create_route = "/api/skills/create/"

        # skill data;
        cls.skill_data_1 = {"name": "bola_de_fogo", "damage": 50, "mana_cost": 10} 
        cls.skill_data_2 = {"name": "bola_de_gelo", "damage": 22, "mana_cost": 3} 
        cls.skill_data_3 = {"name": "bola_de_agua", "damage": 44, "mana_cost": 8} 

        # criar user adm
        cls.user_adm_data_1 = {"username": "adm","password": "1234","email": "teste@adm.com"}
        cls.user_1 = User.objects.create_superuser(**cls.user_adm_data_1)
        cls.user_1_token = Token.objects.create(user=cls.user_1)

        # criar user comun
        cls.user_comun_data_2 = {"username": "comunUser","password": "1234","email": "teste2@comun.com"}

        cls.user_2 = User.objects.create(**cls.user_comun_data_2)
        cls.user_2_token = Token.objects.create(user=cls.user_2)

    # create route ---------------------------------------

    def test_create_skill_route_with_token_adm_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)

        response = self.client.post(self.create_route,self.skill_data_1,format='json')
        self.assertEqual(response.status_code, 201,"testando criar skill deve ser 201")
        # verificando os atributos da skill criada
        self.assertEqual(response.data['name'], self.skill_data_1['name'],"verificando o name")
        self.assertEqual(response.data['damage'], self.skill_data_1['damage'],"verificando o damage")
        self.assertEqual(response.data['mana_cost'], self.skill_data_1['mana_cost'],"verificando o mana_cost")
        self.assertEqual(len(response.data['id']), 36,"verificando se o id e um uuid, um uuid deve ter 36 digitos")

    def test_create_skill_route_no_token_fail(self):
        response = self.client.post(self.create_route,self.skill_data_2,format='json')
        self.assertEqual(response.status_code, 401,"não deve ser possivel criar sem um token 401")

    def test_create_skill_route_with_token_comunUser_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_2_token.key)

        response = self.client.post(self.create_route,self.skill_data_2,format='json')
        self.assertEqual(response.status_code, 403,"testando criar skill sem autorizacao deve ser 403")

    # update route ---------------------------------------

    def test_update_with_token_skill_route_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        # criando outra skill
        responseCreate = self.client.post(self.create_route,self.skill_data_2,format='json')

        self.id_para_update = responseCreate.data['id']
        # editando a outra skill
        response_success = self.client.patch(f'/api/skills/{self.id_para_update}/',{"damage": 10},format='json')
        self.assertEqual(response_success.status_code, 200,"testando se e possivel para um adm mudar os dados de uma skill ja criada deve ser 200")
        self.assertEqual(response_success.data['damage'], 10,"verificando se o damage mudou deve ser 10")

    def test_update_comun_user_token_skill_route_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_2_token.key)

        response = self.client.patch(f'/api/skills/{10}/',{"damage": 10},format='json')
        self.assertEqual(response.status_code, 403,"um usuario comun não deve poder acessar essa rota deve ser 403 não autorizado")

    def test_update_no_token_skill_route_fail(self):
        response = self.client.patch(f'/api/skills/{10}/',{"damage": 10},format='json')
        self.assertEqual(response.status_code, 401,"não deve ser possivel acessar sem um token")

    def test_update_not_found_route_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        response = self.client.patch(f'/api/skills/{10}/',{"damage": 10},format='json')
        self.assertEqual(response.status_code, 404,"não deve ser possivel editar uma qua não exista 404")

    # delete route ---------------------------------------

    def test_delete_with_token_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)

        responseCreate = self.client.post(self.create_route,self.skill_data_2,format='json')

        id_para_delete = responseCreate.data['id']

        response = self.client.delete(f'/api/skills/{id_para_delete}/')
        self.assertEqual(response.status_code, 204,"deve ser possivel para o adm deletar uma skill 204")

    def test_delete_no_token_fail(self):
        response = self.client.delete(f'/api/skills/{10}/')
        self.assertEqual(response.status_code, 401,"deve ser possivel deletar sem token")

    def test_delete_comun_user_with_token_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_2_token.key)

        response = self.client.delete(f'/api/skills/{10}/')
        self.assertEqual(response.status_code, 403,"dnão deve ser possivel que um usuario comun delete uma skill 403 não autorizado")

    def test_delete_not_found_route_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        response = self.client.delete(f'/api/skills/{10}/')
        self.assertEqual(response.status_code, 404,"naõ deve ser possivel deletar uma que não existe")

    # get of id route ---------------------------------------

    def test_get_id_with_token_skill_route_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        # criando outra skill
        responseCreate = self.client.post(self.create_route,self.skill_data_2,format='json')

        self.id_para_update = responseCreate.data['id']
        # tirando o token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + "")

        response = self.client.get(f'/api/skills/get/{self.id_para_update}/')
        self.assertEqual(response.status_code, 200,"deve ser possivel listar uma skill 200")

    def test_delete_not_found_route_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        response = self.client.get(f'/api/skills/get/{10}/')
        self.assertEqual(response.status_code, 404,"naõ deve ser possivel listar uma skill que não existe")

    # get_routes ---------------------------------------
    
    def test_get_all_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        responseCreate1 = self.client.post(self.create_route,self.skill_data_1,format='json')
        responseCreate2 = self.client.post(self.create_route,self.skill_data_2,format='json')
        responseCreate3 = self.client.post(self.create_route,self.skill_data_3,format='json')

        # tirando o token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + "")

        response = self.client.get(f'/api/skills/')
        self.assertEqual(response.status_code, 200,"deve ser possivel listar todos ")
        self.assertEqual(len(response.data), 3,"deve ter todos os 3 criados")