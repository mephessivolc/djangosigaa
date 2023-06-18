from django.db import models


from apps.core.models import Common as CoreCommon
# Create your models here.

class StatesModel(CoreCommon):
    
    name = models.CharField("Nome", max_length=30)
    acronym = models.CharField("Sigla", max_length=2)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    
class CitiesModel(CoreCommon):

    state = models.ForeignKey(StatesModel, 
                              on_delete=models.CASCADE,
                              verbose_name='Estado'
                              )
    name = models.CharField("Nome", max_length=80)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    