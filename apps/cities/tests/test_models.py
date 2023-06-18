from django.contrib.auth import get_user_model
from django.test import TestCase

from scripts.create_users import create_cpf

from apps.cities.models import StatesModel, CitiesModel, Address

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

class AddressManagersTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            name = "User",
            email = "Email@users.com",
            password = 'foo',
            document = create_cpf(),
        )

        state = StatesModel.objects.create(
            name = "Teste",
            acronym = "TE"
        )

        self.cities = CitiesModel.objects.create(
            state = state,
            name = "Teste Cidade"
        )

    def test_create_addres(self):
        self.create = Address.objects.create(
            user = self.user,
            public_place = "Endereço do usuário",
            number = "123",
            district = "Bairro do usuário",
            complement = "Complemento do Usuário",
            cep = "Cep",
            city = self.cities,
        )

        self.assertEqual( self.create.user, self.user)
        self.assertEqual( self.create.public_place, "Endereço do usuário")
        self.assertEqual( self.create.number, "123")
        self.assertEqual( self.create.district, "Bairro do usuário")
        self.assertEqual( self.create.complement, "Complemento do Usuário")
        self.assertEqual( self.create.cep, "Cep")
        self.assertEqual( self.create.city, self.cities,)
