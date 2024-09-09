from django.contrib import admin

from etablissement.models import Responsable

# Register your models here.


@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    pass
