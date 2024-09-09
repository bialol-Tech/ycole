
from django.contrib import admin
from django.urls import include, path
from ycole import settings
from django.conf.urls.static import static
from .views import  gestionVacations

urlpatterns = [
    path('gerer',gestionVacations, name='gerer-vacations' ),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
