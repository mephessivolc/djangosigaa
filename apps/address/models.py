from django.db import models
from django.contrib.auth import get_user_model

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
    name = models.CharField("Nome", max_length=150)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    
class Address(CoreCommon):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    public_place = models.CharField("Endereço", max_length=200, default="")
    number = models.CharField('Numero', max_length=10)
    district = models.CharField("Bairro", max_length=100)
    complement = models.CharField("Complemento", max_length=150, blank=True, null=True)
    cep = models.CharField("CEP", max_length=10)
    city = models.ForeignKey(CitiesModel, 
                             on_delete=models.CASCADE, 
                             verbose_name="Cidade"
                             )

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ['user']

    def __str__(self) -> str:
        return f"{self.user}"
    
    def get_full_address(self):
        response = f"End: {self.public_place}, {self.number}"
        if self.complement:
            response = response + f", {self.complement}"
        response = response + f". Bairro: {self.district}, CEP: {self.cep}."
        response = response + f"{self.city.name} - {self.city.state.acronym}"

        return response