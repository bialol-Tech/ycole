from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from etablissement.models import Etablissement

class CustomUser(AbstractUser):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    # Autres champs spécifiques à l'utilisateur

    def __str__(self):
        return self.username