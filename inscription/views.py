from django.shortcuts import redirect, render

# from inscription.forms import FormulaireInscriptionEtudiantForm
from etablissement.models import Etablissement
from inscription.models import AnneeAcademique, Classe, Etudiant, Inscription




def getClasseByEtablissement(request, etablissement):
    return  Classe.objects.filter(etablissement=etablissement).all()
     

# Create your views here.from django.shortcuts import redirect, render
from inscription.models import Etudiant, Inscription
from .forms import EtudiantForm, InscriptionForm

def inscrireEtudiant(request):
    etablissement = request.user.etablissement
    
    classes = Classe.objects.filter(etablissement_id=etablissement)
    annees = AnneeAcademique.getAll()

    if request.method == 'POST':
        etudiant_form = EtudiantForm(request.POST)
        inscription_form = InscriptionForm(request.POST)

        if etudiant_form.is_valid() and inscription_form.is_valid():

            etudiant = etudiant_form.save(commit=False)
            etudiant.etablissement = etablissement
            etudiant.save()

            classe_id = request.POST.get('classe')
            annee_academique_id = request.POST.get('annee_academique')

            try:
                classe = Classe.objects.get(id=classe_id)
                annee_academique = AnneeAcademique.objects.get(id=annee_academique_id)
            except Classe.DoesNotExist:
                print(f"Classe avec ID {classe_id} n'existe pas.")
                return render(request, 'inscription/add.html', {
                    'etudiant_form': etudiant_form,
                    'inscription_form': inscription_form,
                    'classes': classes,
                    'annees': annees,
                    'error_message': 'Classe invalide.',
                })


            inscription = inscription_form.save(commit=False)
            inscription.etudiant = etudiant
            inscription.classe = classe
            inscription.annee_academique = annee_academique
            inscription.save()

            return redirect('inscrire-etudiant')
        else:
            print("formulaire invalid")
    else:
        etudiant_form = EtudiantForm()
        inscription_form = InscriptionForm()

       

    return render(request, 'inscription/add.html', {
        'etudiant_form': etudiant_form,
        'inscription_form': inscription_form,
        'classes': classes,
        'annees': annees,
    })

