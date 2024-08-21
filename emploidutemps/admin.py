from django.contrib import admin
from .models import (
    Semestre, UniteClasse, Unite, Matiere, Note, Grade, Enseignant,
    TrancheHoraire, PresenceEtudiant, EmploiDuTemps, CahierTexte
)


# Register your models here.
# Enregistrement des modèles dans l'administration Django
@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'date_debut', 'date_fin')
    ordering = ('-date_debut',)

@admin.register(UniteClasse)
class UniteClasseAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'semestre')
    ordering = ('-libelle',)

@admin.register(Unite)
class UniteAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'unite_classe')
    ordering = ('-libelle',)

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'unite', 'volume_horaire')
    ordering = ('-libelle',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'matiere', 'note_obtenue', 'date_evaluation')
    ordering = ('-date_evaluation',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('libelle',)
    ordering = ('-libelle',)

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'grade', 'email', 'telephone', 'matricule')
    ordering = ('-nom', '-prenom',)

@admin.register(TrancheHoraire)
class TrancheHoraireAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'debut', 'fin')
    ordering = ('-debut',)

@admin.register(PresenceEtudiant)
class PresenceEtudiantAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'date', 'presence')
    ordering = ('-date',)

@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('matiere', 'enseignant', 'classe', 'tranche_horaire', 'presence_etudiant', 'jour')
    ordering = ('-jour',)

@admin.register(CahierTexte)
class CahierTexteAdmin(admin.ModelAdmin):
    list_display = ('emploi_du_temps', 'contenu', 'date')
    ordering = ('-date',)
