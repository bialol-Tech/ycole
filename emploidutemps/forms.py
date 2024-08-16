from django import forms
from .models import (
    EmploiDuTemps, Matiere, Enseignant, TrancheHoraire, PresenceEtudiant,
    CahierTexte, Unite, UniteClasse, Semestre, Note
)

class EmploiDuTempsForm(forms.ModelForm):
    class Meta:
        model = EmploiDuTemps
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = '__all__'

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'

class TrancheHoraireForm(forms.ModelForm):
    class Meta:
        model = TrancheHoraire
        fields = '__all__'

class PresenceEtudiantForm(forms.ModelForm):
    class Meta:
        model = PresenceEtudiant
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CahierTexteForm(forms.ModelForm):
    class Meta:
        model = CahierTexte
        fields = '__all__'

class UniteForm(forms.ModelForm):
    class Meta:
        model = Unite
        fields = '__all__'

class UniteClasseForm(forms.ModelForm):
    class Meta:
        model = UniteClasse
        fields = '__all__'

class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
