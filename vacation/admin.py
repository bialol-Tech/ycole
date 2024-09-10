from django.contrib import admin

from vacation.models import Vacation, Grade,Enseignant

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'prix_unitaire_horaire']


# Register your models here.
@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ('annee', 'classe', 'enseignant', 'semestre', 'matiere', 'debut', 'fin', 'nbre_heure_effectue' )
    search_fields = ('annee', 'enseignant')
    list_filter = ('annee','enseignant')
    ordering = ('annee','enseignant')

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'email', 'diplome', 'document_administratif', 'grade')
    search_fields = ('nom', 'telephone', 'email')
    ordering = ('nom','prenom')