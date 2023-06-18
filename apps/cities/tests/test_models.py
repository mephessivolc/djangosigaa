
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone as tmz
from django.conf import settings

from apps.cities.models import StatesModel, CitiesModel

class StatesManagersTests(TestCase):
    
    def test_create_state(self):
        self.state = StatesModel.objects.create(
            name = "Teste",
            acronym = "TE"
        )

        self.assertEqual(self.state.name, "Teste")
        self.assertEqual(self.state.acronym, "TE")


class CitiesManagersTests(TestCase):

    def test_create_cities(self):
        self.created_state = StatesModel.objects.create(
            name = "Teste",
            acronym = "TE"
        )

        self.cities = CitiesModel.objects.create(
            state = self.created_state,
            name = "Teste Cidade"
        )

        self.assertEqual(self.cities.name, "Teste Cidade")
        self.assertEqual(self.cities.state, self.created_state)

