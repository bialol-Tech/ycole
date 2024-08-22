
from django.contrib import admin
from django.urls import include, path
from ycole import settings
from django.conf.urls.static import static
from .views import inscrireEtudiant, listeEtudiantsInscripts, exportReleveNote

urlpatterns = [

    path('inscrire-etudiant/', inscrireEtudiant, name="inscrire-etudiant"),
    path('liste-etudiant-inscrits/', listeEtudiantsInscripts, name="liste-etudiant-inscrits"),
    path('exporter-releve-note-inscrit/', exportReleveNote, name="exporter-releve-note-inscrit"),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
