from django.test import TestCase
from django.core.exceptions import ValidationError
from classes.models import Class


class ClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.magus_data = {
            "name": "magus",
            "life": 4,
            "attack": 5,
            "defense": 3,
            "mana": 10,
        }

        cls.magus = Class.objects.create(**cls.magus_data)

    def test_name_max_length(self):
        """
        Verifica a propriedade de tamanho máximo de `name`
        """
        expected_max_length = 30

        result_max_length = Class._meta.get_field("name").max_length

        msg = f"Verifique se a propriedade `max_length` de name foi definida como {expected_max_length}"

        self.assertEqual(expected_max_length, result_max_length, msg)

    def test_negative_number_life(self):
        """
        Verifica se `life` aceita numeros menores que 0
        """
        class_data_life = {
            "name": "dragon",
            "life": -4,
            "attack": 5,
            "defense": 3,
            "mana": 10,
        }

        classes_1 = Class(**class_data_life)

        expected_message = "Ensure this value is greater than or equal to 0."

        with self.assertRaisesMessage(ValidationError, expected_message):
            classes_1.full_clean()

    def test_negative_number_attack(self):
        """
        Verifica se `attack` aceita numeros menores que 0
        """
        class_data_attack = {
            "name": "dragon",
            "life": 4,
            "attack": -5,
            "defense": 3,
            "mana": 10,
        }

        classes_1 = Class(**class_data_attack)

        expected_message = "Ensure this value is greater than or equal to 0."

        with self.assertRaisesMessage(ValidationError, expected_message):
            classes_1.full_clean()

    def test_negative_number_defense(self):
        """
        Verifica se `defense` aceita numeros menores que 0
        """
        class_data_defense = {
            "name": "dragon",
            "life": 4,
            "attack": 5,
            "defense": -3,
            "mana": 10,
        }

        classes_1 = Class(**class_data_defense)

        expected_message = "Ensure this value is greater than or equal to 0."

        with self.assertRaisesMessage(ValidationError, expected_message):
            classes_1.full_clean()

    def test_negative_number_mana(self):
        """
        Verifica se `mana` aceita numeros menores que 0
        """
        class_data_mana = {
            "name": "dragon",
            "life": 4,
            "attack": 5,
            "defense": 3,
            "mana": -10,
        }

        classes_1 = Class(**class_data_mana)

        expected_message = "Ensure this value is greater than or equal to 0."

        with self.assertRaisesMessage(ValidationError, expected_message):
            classes_1.full_clean()
