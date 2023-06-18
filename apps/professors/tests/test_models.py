from django.contrib.auth import get_user_model
from django.test import TestCase

from scripts.create_random import random_number, create_random_strings
from scripts.create_users import create_cpf

from apps.professors.models import ProfessorsModels

class ProfessorManagersTests(TestCase):

    def setUp(self):

        self.User = get_user_model()
        self.document = create_cpf()
        self.admin_document = create_cpf()
        self.name = create_random_strings(140)

        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            name = self.name,
            password='foo',
            document=self.document,
            )
        self.user.save()

    def test_create_professor(self):
        self.professor = ProfessorsModels.objects.create(
            users = self.user,
        )

        self.assertEqual(self.professor.users, self.user)

    def test_create_register(self):
        register = random_number(6)

        self.professor = ProfessorsModels.objects.create(
            users = self.user,
            registration = register,
        )

        self.assertEqual(self.professor.registration, register)

    def test_create_professor_with_not_registration(self):
        self.professor = ProfessorsModels.objects.create(
            users = self.user,
        )

        self.assertEqual(self.professor.registration, None)
    
    def test_create_professor_with_len_registration(self):
        register = random_number(10)

        self.professor = ProfessorsModels.objects.create(
            users = self.user,
            registration = register,
        )

        self.assertEqual(len(self.professor.registration), 10)