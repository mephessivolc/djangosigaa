from django.test import TestCase

from apps.core.models import EquivalenceCreditsHours
# Create your tests here.

class EquivalenceCreditsHoursManagersTests(TestCase):

    def setUp(self) -> None:
        self.object = EquivalenceCreditsHours.objects.create(
            equivalence = 15,
        )

    def test_create(self):      
        self.assertEqual(self.object.equivalence, 15)

    def test_get_number_of_equivalence(self):
        self.assertEqual(self.object.get_number_of_equivalence(), 15)