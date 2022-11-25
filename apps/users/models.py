from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import re
import uuid

from localflavor.br import models as localflavor_models

from .manager import CustomUserManager
# Create your models here.


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
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    email = models.EmailField('E-mail alternativo')

    class Meta:
        verbose_name = 'E-mail alternativo'
        verbose_name_plural = 'E-mails alternativos'
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.email}"