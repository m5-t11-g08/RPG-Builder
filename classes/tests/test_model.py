from django.test import TestCase
from classes.models import Class


class ClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.class_data = {
            "name": "magus",
            "life": 4,
            "attack": 5,
            "defense": 3,
            "mana": 10,
        }

        cls.classes = Class.objects.create(**cls.class_data)

        cls.classes.save()

    def test_name_max_length(self):
        """
        Verifica a propriedade de tamanho máximo de `name`
        """

        expected_max_length = 30

        result_max_length = Class._meta.get_field("name").max_length

        msg = f"Verifique se a propriedade `max_length` de name foi definida como {expected_max_length}"

        self.assertEqual(expected_max_length, result_max_length, msg)
