from django.contrib import admin
from .models import Semestre, Unite, Matiere, UniteClasse, Note


@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('nom', )
    search_fields = ('nom',)


@admin.register(Unite)
class UniteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'credits')
    search_fields = ('nom', 'code')
    list_filter = ('credits',)
    ordering = ('nom',)


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'coefficient', 'unite')
    search_fields = ('nom', 'code')
    list_filter = ('unite',)
    ordering = ('nom',)


@admin.register(UniteClasse)
class UniteClasseAdmin(admin.ModelAdmin):
    list_display = ('unite', 'classe', 'semestre', 'annee')
    search_fields = ('unite__nom', 'classe__nom', 'semestre__nom')
    list_filter = ('unite', 'classe', 'semestre')
    ordering = ('unite', 'classe', 'semestre')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'matiere', 'valeur', 'date_attribuee')
    search_fields = ('etudiant__nom', 'matiere__nom')
    list_filter = ('matiere', 'date_attribuee')
    ordering = ('etudiant', 'matiere')
