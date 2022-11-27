from django.test import TestCase
from django.template.defaultfilters import slugify

# Create your tests here.
from apps.core import models

class InstituteManagersTests(TestCase):

    @classmethod
    def setUpTestData(self):
        self.institute = models.Institute.objects.create(
            name = "Nome de Instiução",
            short_name = "NI"
        )

    def test_create_institute(self):
        self.assertEqual(self.institute.name, "Nome de Instiução")
        self.assertEqual(self.institute.short_name, "NI")
        self.assertEqual(self.institute.slug, slugify("Nome de Instiução"))

class DepartmentsManagersTests(TestCase):

    @classmethod
    def setUpTestData(self):
        self.institute = models.Institute.objects.create(
            name = "Nome de Instiução",
            short_name = "NI"
        )

        self.department = models.Departaments.objects.create(
            name = "Nome departamento",
            short_name = "Dep",
            institute = self.institute
        )


    def test_create_department(self):

        self.assertEqual(self.department.name, "Nome departamento")
        self.assertEqual(self.department.short_name, "Dep")
        self.assertEqual(self.department.institute, self.institute)
        self.assertEqual(self.department.slug, slugify("Nome departamento"))

class CoursesManagersTests(TestCase):

    @classmethod
    def setUpTestData(self):
        self.institute = models.Institute.objects.create(
            name = "Nome de Instiução",
            short_name = "NI"
        )

        self.department = models.Departaments.objects.create(
            name = "Nome departamento",
            short_name = "Dep",
            institute = self.institute
        )

        self.course = models.Courses.objects.create(
            name = "Nome do Curso",
            departament = self.department
        )

    def test_create_courses(self):
        self.assertEqual(self.course.name, "Nome do Curso")
        self.assertEqual(self.course.slug, slugify("Nome do Curso"))
        self.assertEqual(self.course.departament, self.department)
