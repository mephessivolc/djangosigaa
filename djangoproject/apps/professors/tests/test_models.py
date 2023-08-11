from django.contrib.auth import get_user_model
from django.test import TestCase

from scripts.create_random import random_number, create_random_strings
from scripts.create_users import create_cpf

from apps.professors.models import ProfessorsModels

class ProfessorManagersTests(TestCase):

    def setUp(self):
        self.document = create_cpf()
        self.name = create_random_strings(140)

        self.object = ProfessorsModels.objects.create(
            email='normal@user.com', 
            name = self.name,
            password='foo',
            document=self.document,
        )

    def test_create_professor(self):
        self.assertEqual(ProfessorsModels.objects.filter(name=self.name).exists(), True)

    def test_equals(self):
        self.assertEqual(self.object.name, self.name)
        self.assertEqual(self.object.email, 'normal@user.com')
        self.assertEqual(self.object.password, 'foo')
        self.assertEqual(self.object.document, self.document)

    def test_create_register(self):
        register = random_number(6)

        self.object = ProfessorsModels.objects.create(
            registration = register,
        )

        self.assertEqual(self.object.registration, register)

    def test_create_professor_with_not_registration(self):    
        self.assertEqual(self.object.registration, None)
    