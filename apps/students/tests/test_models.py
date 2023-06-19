from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone as tmz

from scripts.create_users import create_cpf
from scripts.create_random import create_random_strings, random_number

from apps.students.models import StudentsModel
from apps.institute.models import Courses, Departaments, Institute

class UsersManagersTests(TestCase):

    def setUp(self):

        self.document = create_cpf()
        self.admin_document = create_cpf()
        self.name = create_random_strings(140)
        self.number = random_number(5)

        institute = Institute.objects.create(
            short_name = "TE"
        )
        departament = Departaments.objects.create(
            short_name = "Teste",
            institute = institute
        )

        self.course = Courses.objects.create(
            short_name = "Curso",
            departament = departament,
            number = "123"
        )

        self.registration = random_number(5)

        self.user = StudentsModel.objects.create_user(
            email='normal@user.com', 
            name = self.name,
            password='foo',
            document=self.document,
            course = self.course,
            registration = self.registration,
            )

    def test_create(self):      
        self.assertEqual(self.user.course, self.course)
    
    def test_registration(self):
        number = f"{tmz.now().year}{self.course.number}{self.registration}"

        self.assertEqual(self.user.registration, number)