
from etablissement.models import Etablissement
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentification.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Optionnel : Vous pouvez personnaliser l'admin pour `CustomUser` ici
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('etablissement',)}),
    )


@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    pass