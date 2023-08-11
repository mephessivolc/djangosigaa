from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

Users = get_user_model()
class ProfessorsModels(Users):

    registration = models.CharField("Numero de Registro", max_length=10, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    