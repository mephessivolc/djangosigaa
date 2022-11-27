from django.test import TestCase

# Create your tests here.
from apps.core import models

class CoreManagersTests(TestCase):

    @classmethod
    def setUpTestData(self):
        self.institute = models.Institute.objects.create(
            name = "Nome de Instiução",
            short_name = "NI"
        )

    def test_create_institute(self):
        self.assertEqual(self.institute.name, "Nome de Instiução")
        self.assertEqual(self.institute.short_name, "NI")

    def test_create_department(self):
        department = models.Departaments.objects.create(
            name = "Nome departamento",
            short_name = "Dep",
            institute = self.institute
        )

        self.assertEqual(department.name, "Nome departamento")
        self.assertEqual(department.short_name, "Dep")
        self.assertEqual(department.institute, self.institute)