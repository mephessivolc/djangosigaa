from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import re
import uuid

from localflavor.br.models import BRCPFField, BRCNPJField

from .manager import CustomUserManager
# Create your models here.


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
    name = models.CharField('Nome', max_length=150, default='')
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.name    