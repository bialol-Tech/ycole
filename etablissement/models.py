from django.db import models

# Create your models here.
class Etablissement(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    pays = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    site_web = models.URLField(blank=True, null=True)
    secteur_activite = models.CharField(max_length=100, blank=True, null=True)
    nb_salaries = models.PositiveIntegerField(blank=True, null=True)
    nb_etudiants = models.PositiveIntegerField(blank=True, null=True)
    nb_employes = models.PositiveIntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to="Etablissement/logo",blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name = "Etablissement"
        verbose_name_plural = "Etablissements"
        ordering = ["nom"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["telephone"]),
        ]

    
    def __str__(self):
        return self.nom
    
    def getEtablissement():
        return Etablissement.objects.all()


class Responsable(models.Model):
    nom = models.CharField(max_length=100)
    signature = models.ImageField(null=True, blank=True)
    profile = models.CharField(max_length=30)
    telephone = models.CharField(null=True, blank=True, max_length=20)
    email = models.EmailField(null=True, blank=True)


    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        ordering = ["profile"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["telephone"]),
        ]


    def __str__(self) -> str:
        return self.nom

    def getResponsables(self):
        return Responsable.objects.all()
    
    
