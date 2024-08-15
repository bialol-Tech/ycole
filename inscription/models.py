from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

SEMESTRES = {
        "s1": "SEMESTRE 1",
        "s2": "SEMESTRE 2",
    }


# Create your models here.
class AnneeAcademique(models.Model):
    libelle = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Année académique"
        verbose_name_plural = "Les années académiques"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle

class Classe(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        verbose_name = "La classe"
        verbose_name_plural = "Les classes"
        ordering = ["-libelle"]
    
    def __str__(self):
        return self.libelle


class Etudiant(AbstractUser):
    date_de_naissance = models.DateField()
    adresse = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    quartier = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='etudiant_set',  # related_name personnalisé
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='etudiant_permissions_set',  # related_name personnalisé
        blank=True
    )

    class Meta:
        verbose_name = "Étudiant(e)"
        verbose_name_plural = "Les étudiants"
        ordering = ["-first_name", "-last_name"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class MontantAttenduSemestre(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=2, choices=SEMESTRES)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    montant = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Montant attendu par semestre"
        verbose_name_plural = "Les montants attendus par semestre"
        ordering = ["-semestre","-annee_academique"]

    def __str__(self):
        return f"{self.montant} attendu pour {self.classe.libelle} de semestre {self.semestre} de l'année académique {self.annee_academique.libelle}"

class MontantAttenduInscription(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    montant = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Montant attendu par inscription"
        verbose_name_plural = "Les montants attendus par inscription"
        ordering = ["-annee_academique", "-classe"]

    def __str__(self):
        return f"{self.montant} attendu par inscription pour {self.classe.libelle} de l'année académique {self.annee_academique.libelle}"

class Inscription(models.Model):
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inscription"
        verbose_name_plural = "Les inscriptions"
        ordering = ["-date_inscription", "-date_inscription", "classe"]
        unique_together = ["annee_academique", "etudiant", "classe"]

    def __str__(self):
        return f"Inscription de {self.etudiant.last_name} {self.etudiant.first_name} pour {self.classe.libelle} de l'année académique {self.annee_academique.libelle}"

class PaiementInscription(models.Model):
    montant_attendu_inscription = models.ForeignKey(MontantAttenduInscription, on_delete=models.CASCADE)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    date_versement = models.DateTimeField(auto_now_add=True)
    montant_versement = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Paiement effectué par inscription"
        verbose_name_plural = "Les paiements effectués par inscription"
        ordering = ["-date_versement", "-inscription"]

    def __str__(self):
        return f"Paiement effectué par {self.inscription.etudiant.first_name} {self.inscription.etudiant.last_name} pour {self.montant_attendu_inscription.classe.libelle} de l'année académique {self.montant_attendu_inscription.annee_academique.libelle}"


class PaiementSemestre(models.Model):
    montant_attendu_semestre = models.ForeignKey(MontantAttenduSemestre, on_delete=models.CASCADE)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    date_versement = models.DateTimeField(auto_now_add=True)
    montant_versement = models.IntegerField(validators=[MinValueValidator(1)])


    class Meta:
        verbose_name = "Paiement effectué par semestre"
        ordering = ["-date_versement", "-inscription"]
        verbose_name_plural = "Les paiements effectués par semestre"

    def __str__(self):
        return f"Paiement effectué par {self.inscription.etudiant.first_name} {self.inscription.etudiant.last_name} pour {self.montant_attendu_semestre.classe.libelle} au semestre {self.montant_attendu_semestre.semestre} de l'année académique {self.montant_attendu_semestre.annee_academique.libelle}"