from django.shortcuts import render

from inscription.models import AnneeAcademique, Classe
from note.models import Semestre
from vacation.models import Enseignant, Vacation

# Create your views here.
def gestionVacations(request):
    annees = AnneeAcademique.objects.all()
    classes = Classe.objects.all()
    enseignants = Enseignant.objects.all()

    vacations = []

    context = {
        'annees': annees,
        'classes': classes,
        'enseignants': enseignants,
    }

    if request.method == 'POST': 
        print(request.POST)
        annee_id = request.POST.get('annee_academique')
        classe_id = request.POST.get('classe')
        enseignant_id = request.POST.get('enseignant')
        somme_total_vacation = 0

    
        if annee_id:
            annee = AnneeAcademique.objects.filter(id=annee_id).first()
            if classe_id and enseignant_id:
                classe = Classe.objects.filter(id=classe_id).first()
                enseignant = Enseignant.objects.filter(pk=enseignant_id).first()
                vacations = Vacation.objects.filter(annee=annee, classe=classe, enseignant=enseignant)
                

            elif enseignant_id:
                enseignant = Enseignant.objects.filter(pk=enseignant_id).first()
                vacations = Vacation.objects.filter(annee=annee,  enseignant=enseignant)


            elif classe_id:
                classe = Classe.objects.filter(id=classe_id).first()          
                vacations = Vacation.objects.filter(annee=annee, classe=classe)

    
            else:
                annee = AnneeAcademique.objects.filter(id=annee_id).first()
                vacations = Vacation.objects.filter(annee=annee)


        elif enseignant_id:
            enseignant = Enseignant.objects.filter(pk=enseignant_id).first()
            vacations = Vacation.objects.filter(annee=annee)


        else:
            vacations = []
            somme_total_vacation = 0


            
        nombre_heure_effectuees_total = Vacation.statistiqueUtile(vacations)['nbre_heure_effectuee']
        montant_total_vacation = Vacation.statistiqueUtile(vacations)['montant_total_vacation']
        nbre_cours_effectues = Vacation.statistiqueUtile(vacations)['nbre_cours_effectues']


        context['vacations'] = vacations
        context['somme_total_vacation'] = montant_total_vacation
        context['nombre_heure_effectuees_total'] = nombre_heure_effectuees_total
        context['nbre_cours_effectues'] = nbre_cours_effectues

        return render(request, 'vacation/liste.html', context)
    else:
        return render(request, 'vacation/liste.html', context)