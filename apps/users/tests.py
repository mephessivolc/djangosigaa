from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone as tmz

from scripts.create_users import create_cpf
from apps.users import models as user_models

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="user",
            email='normal@user.com', 
            password='foo'
            )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        # admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        admin_user = User.objects.create_superuser(
            username="user",
            email='super@user.com', 
            password='foo'
            )
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

    def test_create_userdocuments(self):
        User = get_user_model()
        user = User.objects.create(
            name = "Teste de usuário",
            username = 'Username',
            email = "user@mail.com",
            password = 'foo',
        )

        number = create_cpf()
        document = user_models.UsersDocument.objects.create(
            user = user,
            number = number,
        )

        self.assertEqual(document.user, user)
        self.assertEqual(document.number, number)

    def test_create_alternativeemail(self):
        User = get_user_model()
        user = User.objects.create(
            name = 'Teste de usuário',
            username = 'teste',
            email = 'user@email.com',
            password = 'foo'
        )

        user_email = user_models.UsersEmail.objects.create(
            user = user,
            email = 'email@alternativo.com',
        )

        self.assertEqual(user_email.user, user)
        self.assertEqual(user_email.email, 'email@alternativo.com')

    def test_create_city(self):
        city = user_models.City.objects.create(
            name = "Cidade",
        )

        self.assertEqual(city.name, "Cidade")

    def test_create_address(self):
        User = get_user_model()
        user = User.objects.create(
            name = 'Teste de usuário',
            username = 'teste',
            email = 'user@email.com',
            password = 'foo'
        )

        city = user_models.City.objects.create(
            name = "teste de nome de cidade",
        )

        address = user_models.UserAddress.objects.create(
            user = user,
            city = city,
            public_place = "Teste de Endereço",
            number = "1809",
            district = "bairro",
            complement = "complemento",
            cep = '12345-678',
        )

        self.assertEqual(address.user, user)
        self.assertEqual(address.city, city)
        self.assertEqual(address.public_place,"Teste de Endereço")
        self.assertEqual(address.number,"1809")
        self.assertEqual(address.district, "bairro")
        self.assertEqual(address.complement, "complemento")
        self.assertEqual(address.cep, "12345-678")

    def test_create_birthday(self):
        User = get_user_model()
        user = User.objects.create(
            name = 'Teste de usuário',
            username = 'teste',
            email = 'user@email.com',
            password = 'foo'
        )
        timezone = tmz.now()
        birthdate = user_models.UserBirth.objects.create(
            user = user,
            birth_date = timezone
        )

        self.assertEqual(birthdate.user, user)
        self.assertEqual(birthdate.birth_date, timezone)