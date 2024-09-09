from django.shortcuts import render

from inscription.models import AnneeAcademique, Classe
from note.models import Semestre
from vacation.models import Enseignant, Vacation

# Create your views here.
def gestionVacations(request):
    annees = AnneeAcademique.objects.all()
    classes = Classe.objects.all()
    enseignants = Enseignant.objects.all()


    context = {
        'annees': annees,
        'classes': classes,
        'enseignants': enseignants,
    }

    if request.method == 'POST': 
        annee_id = request.POST.get('annee_academique')
        classe_id = request.POST.get('classe')
        enseignant_id = request.POST.get('enseignant')
   
        annee = AnneeAcademique.objects.filter(id=annee_id).first()
        classe = Enseignant.objects.filter(id=classe_id).first()



        if enseignant_id:
            enseignant = Enseignant.objects.filter(pk=enseignant_id).first()
            vacations = Vacation.objects.filter(annee=annee, classe=classe, enseignant=enseignant)
        else:
            vacations = Vacation.objects.filter(annee=annee, classe=classe)

        print("Les vacations:")
        print(vacations)

        context['vacations'] = vacations

        return render(request, 'vacation/liste.html', context)
    else:
        return render(request, 'vacation/liste.html', context)