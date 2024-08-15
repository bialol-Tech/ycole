
from django.contrib import admin
from django.urls import include, path
from ycole import settings
from django.conf.urls.static import static
from .views import Accueil

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accueil/', Accueil, name="accueil"),
    path('', include('authentification.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
