from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone as tmz
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from scripts.create_users import create_cpf
from scripts.create_random import create_random_strings

from apps.users import models as user_models

class UsersManagersTests(TestCase):

    def setUp(self):

        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            password='foo'
            )
        self.admin_user = self.User.objects.create_superuser(
            email='super@user.com', 
            password='foo'
            )
            
    def test_create_user(self):
        
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertFalse(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(self.user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            self.User.objects.create_user()
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
               
        self.assertEqual(self.admin_user.email, 'super@user.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(self.admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
    
    def test_len_is_equal_or_minus(self):

        self.assertTrue(len(self.user.registration) <= 12)
        self.assertTrue(len(self.user.slug) <= 170)
    
    def test_len_slug(self):
        name = slugify(create_random_strings(180))
        user = self.User.objects.create(
            name = name,
            email = "teste@email.com",
            password = "foo"
        )
        user.save()

        user = self.User.objects.first()

        self.assertFalse(len(user.slug) > 170)

        user.delete()

class DocumentsManagersTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            password='foo'
            )

    def test_create_userdocuments(self):
        number = create_cpf()
        document = user_models.Document.objects.create(
            user = self.user,
            number = number,
        )

        self.assertEqual(document.user, self.user)
        self.assertEqual(document.number, number)

class AlternativeEmailManagersTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            password='foo'
            )

    def test_create_alternativeemail(self):
        user_email = user_models.AlternativeEmail.objects.create(
            user = self.user,
            email = 'email@alternativo.com',
        )

        self.assertEqual(user_email.user, self.user)
        self.assertEqual(user_email.email, 'email@alternativo.com')

class CityManagersTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            password='foo'
            )

    def test_create_city(self):
        city = user_models.City.objects.create(
            name = "Cidade",
        )

        self.assertEqual(city.name, "Cidade")

    def test_create_address(self):
        city = user_models.City.objects.create(
            name = "teste de nome de cidade",
        )

        address = user_models.Address.objects.create(
            user = self.user,
            city = city,
            public_place = "Teste de Endereço",
            number = "1809",
            district = "bairro",
            complement = "complemento",
            cep = '12345-678',
        )

        self.assertEqual(address.user, self.user)
        self.assertEqual(address.city, city)
        self.assertEqual(address.public_place,"Teste de Endereço")
        self.assertEqual(address.number,"1809")
        self.assertEqual(address.district, "bairro")
        self.assertEqual(address.complement, "complemento")
        self.assertEqual(address.cep, "12345-678")

class UsersBirthdayManagersTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            password='foo'
            )

    def test_create_birthday(self):
        
        timezone = tmz.now()
        birthdate = user_models.BirthDay.objects.create(
            user = self.user,
            birth_date = timezone
        )

        self.assertEqual(birthdate.user, self.user)
        self.assertEqual(birthdate.birth_date, timezone)