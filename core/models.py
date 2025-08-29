from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MainUser(AbstractUser):
    departamento = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self): 
        return self.get_full_name() or self.username