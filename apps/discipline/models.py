from django.db import models

from apps.core.models import Common, DateTime, EquivalenceCreditsHours
from apps.institute.models import Courses

# Create your models here.

def get_object():
    try: 
        return EquivalenceCreditsHours.objects.all().last()

    except:
        return None
    
class AbstractClass(Common):
    quantity = models.IntegerField("Carga Horária")
    equivalence_hours = models.ForeignKey(
            EquivalenceCreditsHours, 
            on_delete=models.PROTECT,
            blank=True,
            null=True,
            default=get_object(),
        )

    class Meta:
        ordering = ['quantity']
        abstract = True

    def __str__(self) -> str:
        return f"{self.quantity}"

    def get_number_in_word(self):
        return f"{self.quantity}"
    
    def get_credits_in_hours(self) -> int:
        return self.quantity * self.equivalence_hours.get_number_of_equivalence()
   
class LoadTeoricCredits(AbstractClass):
    pass

class LoadPCCCredits(AbstractClass):
    pass

class LoadInternshipsCredits(AbstractClass):
    """
        Estágios Curriculares

        Model para regisro de créditos de estágios curriculares
    """
    pass 
    
class Discipline(Common, DateTime):
    
    name = models.CharField("Nome", max_length=200)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT, verbose_name="Curso")
    teoric_credits = models.ForeignKey(LoadTeoricCredits, on_delete=models.PROTECT, verbose_name="Créditos Teóricos")
    pcc_credits = models.ForeignKey(LoadPCCCredits, on_delete=models.PROTECT, verbose_name="Créditos PCC")
    internship_credits = models.ForeignKey(LoadInternshipsCredits, on_delete=models.PROTECT, verbose_name="Créditos Estagio")

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplina"
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_credits_total(self) -> int:
        value = self.teoric_credits.quantity + self.pcc_credits.quantity + self.internship_credits.quantity

        return value
    
    def get_hour_total(self) -> int:
        
        return self.teoric_credits.get_credits_in_hours() + \
            self.pcc_credits.get_credits_in_hours() + \
            self.internship_credits.get_credits_in_hours()
    
class PreRequisite(Common, DateTime):
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="discipline")
    prerequisite = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="prerequisiti")


    class Meta:
        verbose_name = 'Pré-Requisito'
        verbose_name_plural = 'Pré-Requisitos'
        ordering = ['discipline', 'prerequisite']

    def __str__(self) -> str:
        return f"{self.prerequisite} ({self.discipline})"