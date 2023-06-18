from django.db import models
from django.template.defaultfilters import slugify
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