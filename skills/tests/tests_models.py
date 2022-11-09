from django.test import TestCase

from django.forms.models import model_to_dict

from skills.models import Skill
# python manage.py test skills.tests.tests_models
# .\venv\Scripts\activate 

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class Skill_Test(TestCase):
    def test_criar_skill_valida(self):
        self.disc_bola_de_fogo = {"name": "bola_de_fogo", "damage": 50, "mana_cost": 10}
        self.bola_de_fogo = Skill.objects.create(**self.disc_bola_de_fogo)

        self.model_to_disc_bola_de_fogo = model_to_dict(self.bola_de_fogo)

        print(self.model_to_disc_bola_de_fogo)
        self.assertEqual(self.model_to_disc_bola_de_fogo['name'], self.disc_bola_de_fogo['name'], "verificar o name da skill")
        self.assertEqual(self.model_to_disc_bola_de_fogo['damage'], self.disc_bola_de_fogo['damage'], "verificar o damage da skill")
        self.assertEqual(self.model_to_disc_bola_de_fogo['mana_cost'], self.disc_bola_de_fogo['mana_cost'], "verificar o mana_cost da skill")