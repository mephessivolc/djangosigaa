import uuid as uid

from django.test import TestCase
from django.utils import timezone as tmz
from django.contrib.auth import get_user_model

# Create your tests here.
from apps.congress.models import (
    Congress, DateCongress, CongressType, 
    RelationsCongressTypes, Subscription
)

class CongressManagersTests(TestCase):

    def test_create_congress(self):
        timezone = tmz.now()
        uuid = uid.uuid4()
        congress = Congress.objects.create(
            id = uuid,
            name = "Teste de Nome",
            short_name = "Teste",
            date_joined = timezone,
        )
        
        self.assertEqual(congress.id, uuid)
        self.assertEqual(congress.name, "Teste de Nome")
        self.assertEqual(congress.short_name, "Teste")
        self.assertNotEqual(congress.date_joined, tmz.now())

    def test_create_congress_type(self):
        uuid = uid.uuid4()
        congress_type = CongressType.objects.create(
            id = uuid,
            name = "Teste"
        )

        self.assertEqual(congress_type.id, uuid)
        self.assertEqual(congress_type.name, 'Teste')

    def test_create_relations_congress_types(self):
        uuid = uid.uuid4()
        congress = Congress.objects.create(
            id = uuid,
            name = "Teste de Nome",
            short_name = "Teste",
        )
        congress_type = CongressType.objects.create(
            id = uuid,
            name = "Teste"
        )
        relations_congress = RelationsCongressTypes.objects.create(
            id = uuid,
            congress = congress,
            type_of = congress_type
        )

        self.assertEqual(relations_congress.id, uuid)
        self.assertEqual(relations_congress.congress, congress)
        self.assertEqual(relations_congress.type_of, congress_type)

    def test_create_subscription(self):
        uuid = uid.uuid4()
        User = get_user_model()
        user = User.objects.create_user(
            id = uuid,
            name = 'Teste',
            email = "teste@gmail.com",
            password = 'foo',
        )
        congress = Congress.objects.create(
            id = uuid,
            name="Teste de Congresso",
            short_name="Teste",
        )

        subscription = Subscription.objects.create(
            id = uuid,
            user = user,
            congress = congress
        )
        
        self.assertEqual(subscription.id, uuid)
        self.assertEqual(subscription.user, user)
        self.assertEqual(subscription.congress, congress)

    def test_create_datecongress(self):
        uuid = uid.uuid4()
        congress = Congress.objects.create(
            id = uuid,
            name = "Teste de Evento",
            short_name = "Teste",
        )
        start_date = tmz.now() + tmz.timedelta(days=5)
        end_date = tmz.now() + tmz.timedelta(days=10)
        enrollment_start_date = tmz.now()
        enrollment_end_date = tmz.now() + tmz.timedelta(days=4)
        date_for_issuing_certificate = tmz.now() + tmz.timedelta(days=15)

        date_congress = DateCongress.objects.create(
            id = uuid,
            congress = congress,
            start_date = start_date,
            end_date = end_date,
            enrollment_start_date = enrollment_start_date,
            enrollment_end_date = enrollment_end_date,
            date_for_issuing_certificate = date_for_issuing_certificate
        )

        self.assertEqual(date_congress.id, uuid)
        self.assertEqual(date_congress.congress, congress)
        self.assertEqual(date_congress.start_date, start_date)
        self.assertEqual(date_congress.end_date, end_date)
        self.assertEqual(date_congress.enrollment_start_date, enrollment_start_date)
        self.assertEqual(date_congress.enrollment_end_date, enrollment_end_date)
        self.assertEqual(date_congress.date_for_issuing_certificate, date_for_issuing_certificate)