
from django.contrib import admin
from django.urls import include, path
from ycole import settings
from django.conf.urls.static import static
from .views import  exportReleveNote, getUnites, getMatieres, importerNote

urlpatterns = [
    path('get-unites',getUnites, name='get-unites' ),
    path('get-matieres',getMatieres, name='get-matieres' ),
    path('exporter-releve-note-inscrit/', exportReleveNote, name="exporter-releve-note-inscrit"),
    path('importer-note/', importerNote, name="importer-note"),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
