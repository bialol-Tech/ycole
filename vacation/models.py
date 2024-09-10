from django.db import models

from inscription.models import AnneeAcademique, Classe
from note.models import Matiere, Semestre
from django.core.validators import MinValueValidator


class Grade(models.Model):
    libelle = models.CharField(max_length=50)
    prix_unitaire_horaire = models.IntegerField(validators=[MinValueValidator(1000)])


    def __str__(self) -> str:
        return self.libelle.capitalize()

# Create your models here.
class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    diplome = models.CharField(max_length=100)
    document_administratif = models.FileField(upload_to="Enseignant/Documents/")
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.nom + " " + self.prenom 



class Vacation(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    annee = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    date = models.DateField()
    debut = models.TimeField(null=True, blank=True)
    fin = models.TimeField(null=True, blank=True)
    nbre_heure_effectue = models.IntegerField()

    def calculMontantVacation(self):
        return self.enseignant.grade.prix_unitaire_horaire * self.nbre_heure_effectue
    
    @staticmethod
    def statistiqueUtile(liste_vacations):
        montant_total = 0
        nbre_heure_effectuee = 0
        nbre_cours_effectues = 0
        statistiques = {}

        for vacation in liste_vacations:
            montant_total += vacation.calculMontantVacation()
            nbre_heure_effectuee += vacation.nbre_heure_effectue
            nbre_cours_effectues += 1

        statistiques['nbre_heure_effectuee'] = nbre_heure_effectuee
        statistiques['montant_total_vacation'] = montant_total
        statistiques['nbre_cours_effectues'] = nbre_cours_effectues
        return statistiques
    






