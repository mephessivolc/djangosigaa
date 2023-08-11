import uuid as uid

from django.test import TestCase
from django.utils import timezone as tmz
from django.contrib.auth import get_user_model

# Create your tests here.
from apps.congress import models 

class CongressManagersTests(TestCase):

    def setUp(self) -> None:
        
        self.timezone = tmz.now()
        self.uuid = uid.uuid4()
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name = "Teste de Nome",
            short_name = "Teste",
            date_joined = self.timezone,
        )

    def test_create_congress(self):
        
        self.assertEqual(self.congress.id, self.uuid)
        self.assertEqual(self.congress.name, "Teste de Nome")
        self.assertEqual(self.congress.short_name, "Teste")
        self.assertNotEqual(self.congress.date_joined, tmz.now())


class CongressTypeManagersTests(TestCase):
    def setUp(self) -> None:
        
        self.timezone = tmz.now()
        self.uuid = uid.uuid4()
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name = "Teste de Nome",
            short_name = "Teste",
            date_joined = self.timezone,
        )

        self.congress_type = models.CongressType.objects.create(
            id = self.uuid,
            name = "Teste"
        )

    def test_create_congress_type(self):
        self.assertEqual(self.congress_type.id, self.uuid)
        self.assertEqual(self.congress_type.name, 'Teste')

class RelationsCongressTypeManagersTests(TestCase):
    
    def setUp(self) -> None:
        self.timezone = tmz.now()
        self.uuid = uid.uuid4()
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name = "Teste de Nome",
            short_name = "Teste",
            date_joined = self.timezone,
        )

        self.congress_type = models.CongressType.objects.create(
            id = self.uuid,
            name = "Teste"
        )
        self.relations_congress = models.RelationsCongressTypes.objects.create(
            id = self.uuid,
            congress = self.congress,
            type_of = self.congress_type
        )


    def test_create_relations_congress_types(self):

        self.assertEqual(self.relations_congress.id, self.uuid)
        self.assertEqual(self.relations_congress.congress, self.congress)
        self.assertEqual(self.relations_congress.type_of, self.congress_type)

class SubscriptionManagers(TestCase):
    
    def setUp(self) -> None:
        self.uuid = uid.uuid4()
        User = get_user_model()
        self.user = User.objects.create_user(
            id = self.uuid,
            name = 'Teste',
            email = "teste@gmail.com",
            password = 'foo',
        )
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name="Teste de Congresso",
            short_name="Teste",
        )

        self.subscription = models.Subscription.objects.create(
            id = self.uuid,
            user = self.user,
            congress = self.congress
        )

    def test_create_subscription(self):
        
        self.assertEqual(self.subscription.id, self.uuid)
        self.assertEqual(self.subscription.user, self.user)
        self.assertEqual(self.subscription.congress, self.congress)

class DateCongressManagersTests(TestCase):

    def setUp(self) -> None:
        self.uuid = uid.uuid4()
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name = "Teste de Evento",
            short_name = "Teste",
        )
        
        self.start_date = models.day_hence(5)
        self.end_date = models.day_hence(10)
        self.enrollment_start_date = tmz.now()
        self.enrollment_end_date = models.day_hence(4)
        self.date_for_issuing_certificate = models.day_hence(5)

        self.date_congress = models.DateCongress.objects.create(
            id = self.uuid,
            congress = self.congress,
            start_date = self.start_date,
            end_date = self.end_date,
            enrollment_start_date = self.enrollment_start_date,
            enrollment_end_date = self.enrollment_end_date,
            date_for_issuing_certificate = self.date_for_issuing_certificate
        )


    def test_create_datecongress(self):
        
        self.assertEqual(self.date_congress.id, self.uuid)
        self.assertEqual(self.date_congress.congress, self.congress)
        self.assertEqual(self.date_congress.start_date, self.start_date)
        self.assertEqual(self.date_congress.end_date, self.end_date)
        self.assertEqual(self.date_congress.enrollment_start_date, self.enrollment_start_date)
        self.assertEqual(self.date_congress.enrollment_end_date, self.enrollment_end_date)
        self.assertEqual(self.date_congress.date_for_issuing_certificate, self.date_for_issuing_certificate)

class StaffsManagersTests(TestCase):

    def setUp(self) -> None:
        self.uuid = uid.uuid4()
        User = get_user_model()
        self.user = User.objects.create_user(
            id = self.uuid,
            name = 'Teste',
            email = "teste@gmail.com",
            password = 'foo',
        )
        self.congress = models.Congress.objects.create(
            id = self.uuid,
            name = "Teste de Evento",
            short_name = "Teste",
        )
        
        self.staffs = models.Staffs.objects.create(
            id = self.uuid,
            user = self.user,
            congress = self.congress,
        )

    def test_create_staff(self):
        self.assertEqual(self.staffs.id, self.uuid)
        self.assertEqual(self.staffs.user, self.user)
        self.assertEqual(self.staffs.congress, self.congress)