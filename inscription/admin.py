from django.contrib import admin

from inscription.models import Inscription, Etudiant, AnneeAcademique, PaiementInscription, PaiementSemestre, Classe, MontantAttenduInscription, MontantAttenduSemestre

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

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    pass


@admin.register(MontantAttenduInscription)
class MontantAttenduInscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(MontantAttenduSemestre)
class MontantAttenduSemestreAdmin(admin.ModelAdmin):
    pass