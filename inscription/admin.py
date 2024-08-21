from django.contrib import admin

from inscription.models import Inscription, Etudiant, AnneeAcademique, PaiementInscription, PaiementSemestre, \
Classe, MontantAttenduInscription, MontantAttenduSemestre, PieceAFournirPourInscription, PieceFourniesPourInscription

# Register your models here.
@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    pass

@admin.register(AnneeAcademique)
class AnneeAcademiqueAdmin(admin.ModelAdmin):
    pass

@admin.register(PaiementInscription)
class PaiementInscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(PaiementSemestre)
class PaiementSemestreAdmin(admin.ModelAdmin):
    pass

# class LibelleInline(admin.TabularInline):
#     model = Libelle
#     extra = 1  # Number of empty forms to display in the admin interface

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    # inlines = [LibelleInline]
    list_display = ['libelle', 'etablissement']
    # list_display = ['__str__', 'etablissement']


# @admin.register(Libelle)
# class LibelleClasseAdmin(admin.ModelAdmin):
#     pass




@admin.register(MontantAttenduInscription)
class MontantAttenduInscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(MontantAttenduSemestre)
class MontantAttenduSemestreAdmin(admin.ModelAdmin):
    pass

@admin.register(PieceAFournirPourInscription)
class PieceAFournirPourInscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(PieceFourniesPourInscription)
class PieceFourniesPourInscriptionAdmin(admin.ModelAdmin):
    pass