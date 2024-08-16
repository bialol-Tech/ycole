from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import (EmploiDuTemps, Matiere, Enseignant, TrancheHoraire, PresenceEtudiant, CahierTexte, Unite, UniteClasse, Semestre, Note)
from .forms import (EmploiDuTempsForm, MatiereForm, EnseignantForm, TrancheHoraireForm, PresenceEtudiantForm, CahierTexteForm, UniteForm, UniteClasseForm, SemestreForm, NoteForm)

# Vues pour EmploiDuTemps
def emploiDuTempsIndex(request):
    emplois = EmploiDuTemps.objects.all()
    return render(request, "emploidutemps/emploi_du_temps_index.html", {"emplois": emplois})

def emploiDuTempsDetail(request, id):
    emploi = get_object_or_404(EmploiDuTemps, id=id)
    return render(request, "emploidutemps/emploi_du_temps_detail.html", {"emploi": emploi})

def emploiDuTempsCreer(request):
    if request.method == "POST":
        form = EmploiDuTempsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emploiDuTempsIndex')
    else:
        form = EmploiDuTempsForm()
    return render(request, "emploidutemps/emploi_du_temps_form.html", {"form": form})

def emploiDuTempsModifier(request, id):
    emploi = get_object_or_404(EmploiDuTemps, id=id)
    if request.method == "POST":
        form = EmploiDuTempsForm(request.POST, instance=emploi)
        if form.is_valid():
            form.save()
            return redirect('emploiDuTempsDetail', id=emploi.id)
    else:
        form = EmploiDuTempsForm(instance=emploi)
    return render(request, "emploidutemps/emploi_du_temps_form.html", {"form": form})

def emploiDuTempsSupprimer(request, id):
    emploi = get_object_or_404(EmploiDuTemps, id=id)
    if request.method == "POST":
        emploi.delete()
        return redirect('emploiDuTempsIndex')
    return render(request, "emploidutemps/emploi_du_temps_confirm_delete.html", {"emploi": emploi})

# Vues pour Matiere
def matiereIndex(request):
    matieres = Matiere.objects.all()
    return render(request, "matiere/matiere_index.html", {"matieres": matieres})

def matiereDetail(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    return render(request, "matiere/matiere_detail.html", {"matiere": matiere})

def matiereCreer(request):
    if request.method == "POST":
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiereIndex')
    else:
        form = MatiereForm()
    return render(request, "matiere/matiere_form.html", {"form": form})

def matiereModifier(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if request.method == "POST":
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('matiereDetail', id=matiere.id)
    else:
        form = MatiereForm(instance=matiere)
    return render(request, "matiere/matiere_form.html", {"form": form})

def matiereSupprimer(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if request.method == "POST":
        matiere.delete()
        return redirect('matiereIndex')
    return render(request, "matiere/matiere_confirm_delete.html", {"matiere": matiere})

# Répétez de manière similaire pour les autres modèles (Enseignant, TrancheHoraire, PresenceEtudiant, CahierTexte, Unite, UniteClasse, Semestre, Note)


# Vues pour Enseignant
def enseignantIndex(request):
    enseignants = Enseignant.objects.all()
    return render(request, "enseignant/enseignant_index.html", {"enseignants": enseignants})

def enseignantDetail(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    return render(request, "enseignant/enseignant_detail.html", {"enseignant": enseignant})

def enseignantCreer(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enseignantIndex')
    else:
        form = EnseignantForm()
    return render(request, "enseignant/enseignant_form.html", {"form": form})

def enseignantModifier(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('enseignantDetail', id=enseignant.id)
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, "enseignant/enseignant_form.html", {"form": form})

def enseignantSupprimer(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    if request.method == "POST":
        enseignant.delete()
        return redirect('enseignantIndex')
    return render(request, "enseignant/enseignant_confirm_delete.html", {"enseignant": enseignant})

# Vues pour TrancheHoraire
def trancheHoraireIndex(request):
    tranches = TrancheHoraire.objects.all()
    return render(request, "tranchehoraire/tranche_horaire_index.html", {"tranches": tranches})

def trancheHoraireDetail(request, id):
    tranche = get_object_or_404(TrancheHoraire, id=id)
    return render(request, "tranchehoraire/tranche_horaire_detail.html", {"tranche": tranche})

def trancheHoraireCreer(request):
    if request.method == "POST":
        form = TrancheHoraireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trancheHoraireIndex')
    else:
        form = TrancheHoraireForm()
    return render(request, "tranchehoraire/tranche_horaire_form.html", {"form": form})

def trancheHoraireModifier(request, id):
    tranche = get_object_or_404(TrancheHoraire, id=id)
    if request.method == "POST":
        form = TrancheHoraireForm(request.POST, instance=tranche)
        if form.is_valid():
            form.save()
            return redirect('trancheHoraireDetail', id=tranche.id)
    else:
        form = TrancheHoraireForm(instance=tranche)
    return render(request, "tranchehoraire/tranche_horaire_form.html", {"form": form})

def trancheHoraireSupprimer(request, id):
    tranche = get_object_or_404(TrancheHoraire, id=id)
    if request.method == "POST":
        tranche.delete()
        return redirect('trancheHoraireIndex')
    return render(request, "tranchehoraire/tranche_horaire_confirm_delete.html", {"tranche": tranche})

# Vues pour PresenceEtudiant
def presenceEtudiantIndex(request):
    presences = PresenceEtudiant.objects.all()
    return render(request, "presenceetudiant/presence_etudiant_index.html", {"presences": presences})

def presenceEtudiantDetail(request, id):
    presence = get_object_or_404(PresenceEtudiant, id=id)
    return render(request, "presenceetudiant/presence_etudiant_detail.html", {"presence": presence})

def presenceEtudiantCreer(request):
    if request.method == "POST":
        form = PresenceEtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presenceEtudiantIndex')
    else:
        form = PresenceEtudiantForm()
    return render(request, "presenceetudiant/presence_etudiant_form.html", {"form": form})

def presenceEtudiantModifier(request, id):
    presence = get_object_or_404(PresenceEtudiant, id=id)
    if request.method == "POST":
        form = PresenceEtudiantForm(request.POST, instance=presence)
        if form.is_valid():
            form.save()
            return redirect('presenceEtudiantDetail', id=presence.id)
    else:
        form = PresenceEtudiantForm(instance=presence)
    return render(request, "presenceetudiant/presence_etudiant_form.html", {"form": form})

def presenceEtudiantSupprimer(request, id):
    presence = get_object_or_404(PresenceEtudiant, id=id)
    if request.method == "POST":
        presence.delete()
        return redirect('presenceEtudiantIndex')
    return render(request, "presenceetudiant/presence_etudiant_confirm_delete.html", {"presence": presence})

# Vues pour CahierTexte
def cahierTexteIndex(request):
    cahiers = CahierTexte.objects.all()
    return render(request, "cahiertexte/cahier_texte_index.html", {"cahiers": cahiers})

def cahierTexteDetail(request, id):
    cahier = get_object_or_404(CahierTexte, id=id)
    return render(request, "cahiertexte/cahier_texte_detail.html", {"cahier": cahier})

def cahierTexteCreer(request):
    if request.method == "POST":
        form = CahierTexteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cahierTexteIndex')
    else:
        form = CahierTexteForm()
    return render(request, "cahiertexte/cahier_texte_form.html", {"form": form})

def cahierTexteModifier(request, id):
    cahier = get_object_or_404(CahierTexte, id=id)
    if request.method == "POST":
        form = CahierTexteForm(request.POST, instance=cahier)
        if form.is_valid():
            form.save()
            return redirect('cahierTexteDetail', id=cahier.id)
    else:
        form = CahierTexteForm(instance=cahier)
    return render(request, "cahiertexte/cahier_texte_form.html", {"form": form})

def cahierTexteSupprimer(request, id):
    cahier = get_object_or_404(CahierTexte, id=id)
    if request.method == "POST":
        cahier.delete()
        return redirect('cahierTexteIndex')
    return render(request, "cahiertexte/cahier_texte_confirm_delete.html", {"cahier": cahier})

# Vues pour Unite
def uniteIndex(request):
    unites = Unite.objects.all()
    return render(request, "unite/unite_index.html", {"unites": unites})

def uniteDetail(request, id):
    unite = get_object_or_404(Unite, id=id)
    return render(request, "unite/unite_detail.html", {"unite": unite})

def uniteCreer(request):
    if request.method == "POST":
        form = UniteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uniteIndex')
    else:
        form = UniteForm()
    return render(request, "unite/unite_form.html", {"form": form})

def uniteModifier(request, id):
    unite = get_object_or_404(Unite, id=id)
    if request.method == "POST":
        form = UniteForm(request.POST, instance=unite)
        if form.is_valid():
            form.save()
            return redirect('uniteDetail', id=unite.id)
    else:
        form = UniteForm(instance=unite)
    return render(request, "unite/unite_form.html", {"form": form})

def uniteSupprimer(request, id):
    unite = get_object_or_404(Unite, id=id)
    if request.method == "POST":
        unite.delete()
        return redirect('uniteIndex')
    return render(request, "unite/unite_confirm_delete.html", {"unite": unite})

# Vues pour UniteClasse
def uniteClasseIndex(request):
    uniteClasses = UniteClasse.objects.all()
    return render(request, "uniteclasse/unite_classe_index.html", {"uniteClasses": uniteClasses})

def uniteClasseDetail(request, id):
    uniteClasse = get_object_or_404(UniteClasse, id=id)
    return render(request, "uniteclasse/unite_classe_detail.html", {"uniteClasse": uniteClasse})

def uniteClasseCreer(request):
    if request.method == "POST":
        form = UniteClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uniteClasseIndex')
    else:
        form = UniteClasseForm()
    return render(request, "uniteclasse/unite_classe_form.html", {"form": form})

def uniteClasseModifier(request, id):
    uniteClasse = get_object_or_404(UniteClasse, id=id)
    if request.method == "POST":
        form = UniteClasseForm(request.POST, instance=uniteClasse)
        if form.is_valid():
            form.save()
            return redirect('uniteClasseDetail', id=uniteClasse.id)
    else:
        form = UniteClasseForm(instance=uniteClasse)
    return render(request, "uniteclasse/unite_classe_form.html", {"form": form})

def uniteClasseSupprimer(request, id):
    uniteClasse = get_object_or_404(UniteClasse, id=id)
    if request.method == "POST":
        uniteClasse.delete()
        return redirect('uniteClasseIndex')
    return render(request, "uniteclasse/unite_classe_confirm_delete.html", {"uniteClasse": uniteClasse})

# Vues pour Semestre
def semestreIndex(request):
    semestres = Semestre.objects.all()
    return render(request, "semestre/semestre_index.html", {"semestres": semestres})

def semestreDetail(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    return render(request, "semestre/semestre_detail.html", {"semestre": semestre})

def semestreCreer(request):
    if request.method == "POST":
        form = SemestreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semestreIndex')
    else:
        form = SemestreForm()
    return render(request, "semestre/semestre_form.html", {"form": form})

def semestreModifier(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    if request.method == "POST":
        form = SemestreForm(request.POST, instance=semestre)
        if form.is_valid():
            form.save()
            return redirect('semestreDetail', id=semestre.id)
    else:
        form = SemestreForm(instance=semestre)
    return render(request, "semestre/semestre_form.html", {"form": form})

def semestreSupprimer(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    if request.method == "POST":
        semestre.delete()
        return redirect('semestreIndex')
    return render(request, "semestre/semestre_confirm_delete.html", {"semestre": semestre})

# Vues pour Note
def noteIndex(request):
    notes = Note.objects.all()
    return render(request, "note/note_index.html", {"notes": notes})

def noteDetail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "note/note_detail.html", {"note": note})

def noteCreer(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noteIndex')
    else:
        form = NoteForm()
    return render(request, "note/note_form.html", {"form": form})

def noteModifier(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('noteDetail', id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "note/note_form.html", {"form": form})

def noteSupprimer(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.delete()
        return redirect('noteIndex')
    return render(request, "note/note_confirm_delete.html", {"note": note})
