from django.test import TestCase
from django.utils import timezone as tmz

# Create your tests here.
from apps.congress.models import Congress, CongressType, RelationsCongressTypes

class CongressManagersTests(TestCase):

    def test_create_congress(self):
        timezone = tmz.now()
        congress = Congress.objects.create(
            name = "Teste de Nome",
            short_name = "Teste",
            date_joined = timezone,
        )

        self.assertEqual(congress.name, "Teste de Nome")
        self.assertEqual(congress.short_name, "Teste")
        # self.assertEqual(congress.date_joined, timezone)
        self.assertNotEqual(congress.date_joined, tmz.now())

    def test_create_congress_type(self):
        congress_type = CongressType.objects.create(
            name = "Teste"
        )

        self.assertEqual(congress_type.name, 'Teste')

    def test_create_relations_congress_types(self):
        congress = Congress.objects.create(
            name = "Teste de Nome",
            short_name = "Teste",
        )
        congress_type = CongressType.objects.create(
            name = "Teste"
        )
        relations_congress = RelationsCongressTypes.objects.create(
            congress = congress,
            type_of = congress_type
        )

        self.assertEqual(relations_congress.congress, congress)
        self.assertEqual(relations_congress.type_of, congress_type)