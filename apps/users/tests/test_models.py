from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone as tmz
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from scripts.create_users import create_cpf
from scripts.create_random import create_random_strings, random_number

from apps.users import models as user_models

class UsersManagersTests(TestCase):

    def setUp(self):

        self.User = get_user_model()
        self.document = create_cpf()
        self.admin_document = create_cpf()
        self.name = create_random_strings(140)

        self.user = self.User.objects.create_user(
            email='normal@user.com', 
            name = self.name,
            password='foo',
            document=self.document,
            )
        self.user.save()
        self.admin_user = self.User.objects.create_superuser(
            email='super@user.com', 
            name = self.name,
            password='foo',
            document=self.admin_document,
            )
            
    def test_create_user(self):
        
        self.assertEqual(self.user.email, 'normal@user.com')
        self.assertEqual(self.user.document, self.document)
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
        self.assertEqual(self.admin_user.document, self.admin_document)
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