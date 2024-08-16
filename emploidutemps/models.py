from django.db import models
from inscription.models import Etudiant


class Semestre(models.Model):
    libelle = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Les semestres"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle


class UniteClasse(models.Model):
    libelle = models.CharField(max_length=100)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Unité de Classe"
        verbose_name_plural = "Les unités de classe"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle


class Unite(models.Model):
    libelle = models.CharField(max_length=100)
    unite_classe = models.ForeignKey(UniteClasse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Unité"
        verbose_name_plural = "Les unités"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle


class Matiere(models.Model):
    libelle = models.CharField(max_length=100)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    volume_horaire = models.IntegerField()  # Ajout du champ volume_horaire

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Les matières"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle


class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)  # Utilisation directe du modèle Etudiant
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note_obtenue = models.DecimalField(max_digits=5, decimal_places=2)
    date_evaluation = models.DateField()

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Les notes"
        ordering = ["-date_evaluation"]

    def __str__(self):
        return f"Note de {self.etudiant} pour {self.matiere}"


class Grade(models.Model):
    libelle = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Les grades"
        ordering = ["-libelle"]

    def __str__(self):
        return self.libelle


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    email = models.EmailField()
    telephone = models.CharField(max_length=15, null=True, blank=True)  # Ajout du champ telephone
    matricule = models.CharField(max_length=50, unique=True)  # Ajout du champ matricule

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Les enseignants"
        ordering = ["-nom", "-prenom"]

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class TrancheHoraire(models.Model):
    debut = models.TimeField()
    fin = models.TimeField()
    libelle = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tranche Horaire"
        verbose_name_plural = "Les tranches horaires"
        ordering = ["-debut"]

    def __str__(self):
        return f"{self.libelle} ({self.debut} - {self.fin})"


class PresenceEtudiant(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)  # Utilisation directe du modèle Etudiant
    date = models.DateField()
    presence = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Présence Étudiant"
        verbose_name_plural = "Les présences étudiants"
        ordering = ["-date"]

    def __str__(self):
        return f"Présence de {self.etudiant} le {self.date}"


class EmploiDuTemps(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    classe = models.ForeignKey('inscription.Classe', on_delete=models.CASCADE)  # Correctement référencé
    tranche_horaire = models.ForeignKey(TrancheHoraire, on_delete=models.CASCADE)
    presence_etudiant = models.ForeignKey(PresenceEtudiant, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Emploi du Temps"
        verbose_name_plural = "Les emplois du temps"
        ordering = ["-jour", "-tranche_horaire"]

    def __str__(self):
        return f"Emploi du temps de {self.classe} - {self.matiere}"


class CahierTexte(models.Model):
    emploi_du_temps = models.ForeignKey(EmploiDuTemps, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = "Cahier de Texte"
        verbose_name_plural = "Les cahiers de texte"
        ordering = ["-date"]

    def __str__(self):
        return f"Cahier de texte du {self.date} pour {self.emploi_du_temps}"
