

# from importlib.metadata import requires

# from django import forms

# from etablissement.models import Etablissement

# etablissements = Etablissement.objects.all()


# class FormulaireEtudiantForm(forms.ModelForm):
#     nom = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     prenom = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     date_de_naissance = forms.DateField(widget={'class':'form-control'})
#     nationalite = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     adresse = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     telephone = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     quartier = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     nom_prenom_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     telephone_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     profession_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     nationalite_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     quartier_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     ville_residence_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     email_tuteur = forms.CharField(max_length=100, widget={'class':'form-control'} )
#     etablissement = forms.Select(attrs=etablissements, widget={'class':'form-control'})

from django import forms
from inscription.models import Etudiant, Inscription

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_de_naissance', 'nationalite', 'adresse', 'telephone','email', 'quartier',
                  'nom_prenom_tuteur', 'telephone_tuteur', 'profession_tuteur', 'nationalite_tuteur', 
                  'quartier_tuteur', 'ville_residence_tuteur', 'email_tuteur']
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'nom... EX: BIH' }),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'nom... EX: BIH'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder':'nom... EX: Cré'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nationalité...'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control','placeholder':'Adresse...'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Téléphone...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email...'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control','placeholder':'Quartier...'}),
            'nom_prenom_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nom du tuteur...'}),
            'telephone_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Téléphone du tuteur...'}),
            'profession_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Profession du tuteur...'}),
            'nationalite_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nationalité du tuteur...'}),
            'quartier_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Quartier du tuteur...'}),
            'ville_residence_tuteur': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ville residence du tuteur...'}),
            'email_tuteur': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email du tuteur...'}),
        }

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['classe', 'annee_academique' ]

        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'annee_academique': forms.Select(attrs={'class': 'form-control'}),
        }


