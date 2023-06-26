from django.test import TestCase

# Create your tests here.
from apps.core.models import EquivalenceCreditsHours
from apps.institute.models import Courses, Departaments, Institute
from apps.discipline.models import (LoadTeoricCredits, LoadPCCCredits,
                                    LoadInternshipsCredits, Discipline,
                                    PreRequisite)

class LoadTeoricCreditsManagerTest(TestCase):
    def setUp(self) -> None:
        self.equivalence = EquivalenceCreditsHours.objects.create(
                    equivalence = 15,
                )
        self.object = LoadTeoricCredits.objects.create(
                quantity = 4,
                equivalence_hours = self.equivalence
        )

    def test_create(self):
        self.assertEqual(self.object.quantity, 4)
        self.assertEqual(self.object.equivalence_hours, self.equivalence)
    
    def test_return_get_number_in_word(self):
        self.assertEqual(self.object.get_number_in_word(), "4")

    def test_return_get_credits_in_hours(self):
        value = 4*15
        self.assertEqual(self.object.get_credits_in_hours(), value)

class LoadPCCCreditsManagerTest(TestCase):
    def setUp(self) -> None:
        self.equivalence = EquivalenceCreditsHours.objects.create(
                    equivalence = 15,
                )
        self.object = LoadPCCCredits.objects.create(
                quantity = 4,
                equivalence_hours = self.equivalence
        )

    def test_create(self):
        self.assertEqual(self.object.quantity, 4)
        self.assertEqual(self.object.equivalence_hours, self.equivalence)
    
    def test_return_get_number_in_word(self):
        self.assertEqual(self.object.get_number_in_word(), "4")

    def test_return_get_credits_in_hours(self):
        value = 4*15
        self.assertEqual(self.object.get_credits_in_hours(), value)

class LoadInternshipsCreditsManagerTest(TestCase):
    def setUp(self) -> None:
        self.equivalence = EquivalenceCreditsHours.objects.create(
                    equivalence = 15,
                )
        self.object = LoadInternshipsCredits.objects.create(
                quantity = 4,
                equivalence_hours = self.equivalence
        )

    def test_create(self):
        pass 

    def test_object_is_equal(self):
        self.assertEqual(self.object.quantity, 4)
        self.assertEqual(self.object.equivalence_hours, self.equivalence)
    
    def test_return_get_number_in_word(self):
        self.assertEqual(self.object.get_number_in_word(), "4")

    def test_return_get_credits_in_hours(self):
        value = 4*15
        self.assertEqual(self.object.get_credits_in_hours(), value)

class DisciplineManagerTest(TestCase):
    
    def setUp(self) -> None:
        equivalence = EquivalenceCreditsHours.objects.create(
                    equivalence = 15,
                )
        self.teoric = LoadTeoricCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        self.pcc = LoadPCCCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        self.internship = LoadInternshipsCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        institute = Institute.objects.create(
            name = 'Teste',
        )
        dep = Departaments.objects.create(
            short_name = "Teste",
            institute = institute
        )
        self.courses = Courses.objects.create(
            short_name = "Teste",
            departament = dep, 
        )

        self.object = Discipline.objects.create(
            name = "Teste",
            course = self.courses,
            teoric_credits = self.teoric,
            pcc_credits = self.pcc,
            internship_credits = self.internship
        )
    
    def test_create(self):
        self.assertEquals(Discipline.objects.filter(name='Teste').exists(), True)

    def test_object_is_equal(self):
        self.assertEqual(self.object.name, "Teste")
        self.assertEqual(self.object.course, self.courses)
        self.assertEqual(self.object.teoric_credits, self.teoric)
        self.assertEqual(self.object.pcc_credits, self.pcc)
        self.assertEqual(self.object.internship_credits, self.internship)

    def test_get_credits_total(self):
        self.assertEqual(self.object.get_credits_total(), 12)

    def test_get_hours_total(self):
        self.assertEqual(self.object.get_hour_total(), 12*15)

class PreRequisiteManagerTest(TestCase):
    
    def setUp(self) -> None:
        equivalence = EquivalenceCreditsHours.objects.create(
                    equivalence = 15,
                )
        teoric = LoadTeoricCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        pcc = LoadPCCCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        internship = LoadInternshipsCredits.objects.create(
                quantity = 4,
                equivalence_hours = equivalence
        )
        institute = Institute.objects.create(
            name = 'Teste',
        )
        dep = Departaments.objects.create(
            short_name = "Teste",
            institute = institute
        )
        courses = Courses.objects.create(
            short_name = "Teste",
            departament = dep, 
        )

        self.discipline = Discipline.objects.create(
            name = "Teste",
            course = courses,
            teoric_credits = teoric,
            pcc_credits = pcc,
            internship_credits = internship
        )

        self.prerequisite = Discipline.objects.create(
            name = "Prerequisito",
            course = courses,
            teoric_credits = teoric,
            pcc_credits = pcc,
            internship_credits = internship
        )

        self.object = PreRequisite.objects.create(
            discipline = self.discipline,
            prerequisite = self.prerequisite,
        )
    def test_create(self):
        self.assertEquals(PreRequisite.objects.filter(prerequisite=self.prerequisite).exists(), True)

    def test_equals(self):
        self.assertEqual(self.object.discipline, self.discipline)
        self.assertEqual(self.object.prerequisite, self.prerequisite)