from django.db import models
import uuid

# Create your models here.
class Common(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )

    class Meta:
        abstract = True

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    modified_at = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        abstract = True 

class EquivalenceCreditsHours(Common):

    equivalence = models.IntegerField("Equivalência", default=15)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Equivalência de Creditos/Horas"
        verbose_name_plural = "Equivalências de Creditos/Horas"
        ordering = ['equivalence']

    def get_number_of_equivalence(self):
        return int(self.equivalence)
    