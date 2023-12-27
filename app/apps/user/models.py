from collections.abc import Iterable
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from localflavor.br.models import BRCPFField

from .managers import CustomUserManager


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    username = models.CharField(_("username"), unique=True, max_length=50, default=None)
    name = models.CharField(_("name"), max_length=100,)
    slug = models.SlugField(_("identifier"), max_length=100, editable=False, default="", blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)

    register_number = BRCPFField("CPF", unique=True, default="")

    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    data_modified = models.DateTimeField(auto_now=True, editable=False)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', "register_number"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering =['slug', "date_joined"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("()", kwargs={"pk": self.pk})
    

    def save(self, **kwargs):
        slug_field = slugify(self.name)
        if not self.slug or slug_field is not self.slug:
            self.slug = slugify(self.name)

        super().save(**kwargs)
