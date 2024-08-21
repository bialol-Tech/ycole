from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

from etablissement.models import Etablissement

SEMESTRES = {
        "s1": "SEMESTRE 1",
        "s2": "SEMESTRE 2",
    }

ETATS_PIECES_FOURNIES={
    "en cours": "en cours",
    "acceptée":"Pièce acceptée",
    "rejetée":"Pièce rejetée"
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
    
    def getAll():
        return AnneeAcademique.objects.all()


class Classe(models.Model):
    libelle = models.CharField(max_length=100)  # Nom de la classe
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name='classes')

    class Meta:
        verbose_name = "La classe"
        verbose_name_plural = "Les classes"
        # ordering = ["libelle"]  # Pour trier les classes par leur nom
    
    def __str__(self):
        return self.libelle
    

    
# class Libelle(models.Model):
#     libelle = models.CharField(max_length=30)
#     classe = models.ForeignKey(Classe, related_name="libelles", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.libelle


class Etudiant(models.Model):

    date_de_naissance = models.DateField()
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    nationalite = models.CharField(max_length=70, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    quartier = models.CharField(max_length=30)
    nom_prenom_tuteur = models.CharField(max_length=50, verbose_name="Nom et prenom du tuteur", blank=True, null=True)
    telephone_tuteur = models.CharField(max_length=20, verbose_name="Telephone du tuteur (Whatsapp)", blank=True, null=True)
    profession_tuteur = models.CharField(max_length=100, blank=True, null=True)
    nationalite_tuteur = models.CharField(max_length=70, null=True, blank=True)
    quartier_tuteur = models.CharField(max_length=100, blank=True, null=True)
    ville_residence_tuteur = models.CharField(max_length=100, blank=True, null=True)
    email_tuteur = models.EmailField(max_length=50, null=True, blank=True)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)



    class Meta:
        verbose_name = "Étudiant(e)"
        verbose_name_plural = "Les étudiants"
        ordering = ["-nom", "-prenom"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom}"



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
        return f"Inscription de {self.etudiant.nom} {self.etudiant.prenom} pour {self.classe.libelle} de l'année académique {self.annee_academique.libelle}"

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
    

class PieceAFournirPourInscription(models.Model):
    libelle = models.CharField(max_length=255)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    verbose_name = "Pièce à fournir pour l'inscription"
    verbose_name_plural = "Les pièces à fournir pour les inscriptions"
    ordering = ["-annee", "-classe"]

class PieceFourniesPourInscription(models.Model):
    piece_a_fournir_pour_inscription = models.ForeignKey(PieceAFournirPourInscription, on_delete=models.CASCADE)
    incription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    etat =  models.CharField(max_length=15, choices=ETATS_PIECES_FOURNIES, blank=True)
    fichier = models.FileField(upload_to="Fichiers/PieceInscription")

    verbose_name = "Pièce à fournie pour l'inscription"
    verbose_name_plural = "Les pièces à fournies pour les inscriptions"
    def __str__(self):
        return f"{self.piece_a_fournir_pour_inscription.libelle} par {self.inscription.etudiant.last_name} {self.inscription.etudiant.first_name} de {self.inscription.classe.libelle} de l'année académique {self.inscription.annee_academique.libelle}"

