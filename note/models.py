from django.db import models
from etablissement.models import Etablissement
from inscription.models import Etudiant, Classe


# Create your models here.
class Semestre(models.Model):
    nom = models.CharField(max_length=100)
    debut = models.DateField()
    fin = models.DateField()
    description = models.TextField(blank=True, null=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Unite(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

    classes = models.ManyToManyField(Classe, through='UniteClasse', related_name="unites")

    def __str__(self):
        return self.nom


class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    coefficient = models.FloatField()
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, related_name="matieres")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class UniteClasse(models.Model):
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, related_name="unite_classes")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="unite_classes")
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, related_name="unite_classes")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.unite} - {self.classe} - {self.semestre}"


class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="notes")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="notes")
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
    date_attribuee = models.DateField()
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Note de {self.etudiant} pour {self.matiere}"
