from django.urls import path
from .views import (emploiDuTempsIndex, emploiDuTempsDetail, emploiDuTempsCreer, emploiDuTempsModifier, emploiDuTempsSupprimer,
                    matiereIndex, matiereDetail, matiereCreer, matiereModifier, matiereSupprimer,
                    enseignantIndex, enseignantDetail, enseignantCreer, enseignantModifier, enseignantSupprimer,
                    trancheHoraireIndex, trancheHoraireDetail, trancheHoraireCreer, trancheHoraireModifier, trancheHoraireSupprimer,
                    presenceEtudiantIndex, presenceEtudiantDetail, presenceEtudiantCreer, presenceEtudiantModifier, presenceEtudiantSupprimer,
                    cahierTexteIndex, cahierTexteDetail, cahierTexteCreer, cahierTexteModifier, cahierTexteSupprimer,
                    uniteIndex, uniteDetail, uniteCreer, uniteModifier, uniteSupprimer,
                    uniteClasseIndex, uniteClasseDetail, uniteClasseCreer, uniteClasseModifier, uniteClasseSupprimer,
                    semestreIndex, semestreDetail, semestreCreer, semestreModifier, semestreSupprimer,
                    noteIndex, noteDetail, noteCreer, noteModifier, noteSupprimer)

urlpatterns = [
    path('', emploiDuTempsIndex, name="emploiDuTempsIndex"),
    path('emploi-du-temps/<int:id>/', emploiDuTempsDetail, name="emploiDuTempsDetail"),
    path('emploi-du-temps/creer/', emploiDuTempsCreer, name="emploiDuTempsCreer"),
    path('emploi-du-temps/<int:id>/modifier/', emploiDuTempsModifier, name="emploiDuTempsModifier"),
    path('emploi-du-temps/<int:id>/supprimer/', emploiDuTempsSupprimer, name="emploiDuTempsSupprimer"),

    path('matiere/', matiereIndex, name="matiereIndex"),
    path('matiere/<int:id>/', matiereDetail, name="matiereDetail"),
    path('matiere/creer/', matiereCreer, name="matiereCreer"),
    path('matiere/<int:id>/modifier/', matiereModifier, name="matiereModifier"),
    path('matiere/<int:id>/supprimer/', matiereSupprimer, name="matiereSupprimer"),

    path('enseignant/', enseignantIndex, name="enseignantIndex"),
    path('enseignant/<int:id>/', enseignantDetail, name="enseignantDetail"),
    path('enseignant/creer/', enseignantCreer, name="enseignantCreer"),
    path('enseignant/<int:id>/modifier/', enseignantModifier, name="enseignantModifier"),
    path('enseignant/<int:id>/supprimer/', enseignantSupprimer, name="enseignantSupprimer"),

    path('tranche-horaire/', trancheHoraireIndex, name="trancheHoraireIndex"),
    path('tranche-horaire/<int:id>/', trancheHoraireDetail, name="trancheHoraireDetail"),
    path('tranche-horaire/creer/', trancheHoraireCreer, name="trancheHoraireCreer"),
    path('tranche-horaire/<int:id>/modifier/', trancheHoraireModifier, name="trancheHoraireModifier"),
    path('tranche-horaire/<int:id>/supprimer/', trancheHoraireSupprimer, name="trancheHoraireSupprimer"),

    path('presence-etudiant/', presenceEtudiantIndex, name="presenceEtudiantIndex"),
    path('presence-etudiant/<int:id>/', presenceEtudiantDetail, name="presenceEtudiantDetail"),
    path('presence-etudiant/creer/', presenceEtudiantCreer, name="presenceEtudiantCreer"),
    path('presence-etudiant/<int:id>/modifier/', presenceEtudiantModifier, name="presenceEtudiantModifier"),
    path('presence-etudiant/<int:id>/supprimer/', presenceEtudiantSupprimer, name="presenceEtudiantSupprimer"),

    path('cahier-texte/', cahierTexteIndex, name="cahierTexteIndex"),
    path('cahier-texte/<int:id>/', cahierTexteDetail, name="cahierTexteDetail"),
    path('cahier-texte/creer/', cahierTexteCreer, name="cahierTexteCreer"),
    path('cahier-texte/<int:id>/modifier/', cahierTexteModifier, name="cahierTexteModifier"),
    path('cahier-texte/<int:id>/supprimer/', cahierTexteSupprimer, name="cahierTexteSupprimer"),

    path('unite/', uniteIndex, name="uniteIndex"),
    path('unite/<int:id>/', uniteDetail, name="uniteDetail"),
    path('unite/creer/', uniteCreer, name="uniteCreer"),
    path('unite/<int:id>/modifier/', uniteModifier, name="uniteModifier"),
    path('unite/<int:id>/supprimer/', uniteSupprimer, name="uniteSupprimer"),

    path('unite-classe/', uniteClasseIndex, name="uniteClasseIndex"),
    path('unite-classe/<int:id>/', uniteClasseDetail, name="uniteClasseDetail"),
    path('unite-classe/creer/', uniteClasseCreer, name="uniteClasseCreer"),
    path('unite-classe/<int:id>/modifier/', uniteClasseModifier, name="uniteClasseModifier"),
    path('unite-classe/<int:id>/supprimer/', uniteClasseSupprimer, name="uniteClasseSupprimer"),

    path('semestre/', semestreIndex, name="semestreIndex"),
    path('semestre/<int:id>/', semestreDetail, name="semestreDetail"),
    path('semestre/creer/', semestreCreer, name="semestreCreer"),
    path('semestre/<int:id>/modifier/', semestreModifier, name="semestreModifier"),
    path('semestre/<int:id>/supprimer/', semestreSupprimer, name="semestreSupprimer"),

    path('note/', noteIndex, name="noteIndex"),
    path('note/<int:id>/', noteDetail, name="noteDetail"),
    path('note/creer/', noteCreer, name="noteCreer"),
    path('note/<int:id>/modifier/', noteModifier, name="noteModifier"),
    path('note/<int:id>/supprimer/', noteSupprimer, name="noteSupprimer"),
]
