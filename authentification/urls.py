from django.urls import path

from authentification.views import authentification
from ycole import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', authentification, name="authentification")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)