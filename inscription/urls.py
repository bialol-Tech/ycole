
from django.contrib import admin
from django.urls import include, path
from ycole import settings
from django.conf.urls.static import static
from .views import inscrireEtudiant

urlpatterns = [

    path('inscrire-etudiant/', inscrireEtudiant, name="inscrire-etudiant"),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
