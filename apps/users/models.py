from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

import uuid

from localflavor.br import models as localflavor_models

from .manager import CustomUserManager
# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    name = slugify(uuid.uuid5(uuid.NAMESPACE_URL, filebase))
    return f"images/{name}.{extension}"

class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
    username = models.CharField('Login', max_length=30, default="", unique=True)
    name = models.CharField('Nome', max_length=150, default='')
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name    

class UsersDocument(models.Model):

    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    number = localflavor_models.BRCPFField("CPF")

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.number}"

class UsersEmail(models.Model):

    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    email = models.EmailField('E-mail alternativo')

    class Meta:
        verbose_name = 'E-mail alternativo'
        verbose_name_plural = 'E-mails alternativos'
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.email}"

class City(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField("Cidade", max_length=200)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"


class UserAddress(models.Model):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    public_place = models.CharField("Endereço", max_length=200, default="")
    number = models.CharField('Numero', max_length=50)
    district = models.CharField("Bairro", max_length=50)
    complement = models.CharField("Complemento", max_length=150)
    cep = models.CharField("CEP", max_length=10)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.user}"

class UserBirth(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    birth_date = models.DateTimeField("Data de Nascimento")

    class Meta:
        verbose_name = "Data de Nascimento"
        verbose_name_plural = "Datas de Nascimentos"
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.user}"


class UserImage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location)

    class Meta:
        verbose_name = "Imagem"
        verbose_name = "Imagens"
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.user}"