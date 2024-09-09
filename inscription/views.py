from django.shortcuts import redirect, render

# from inscription.forms import FormulaireInscriptionEtudiantForm
from etablissement.models import Etablissement
from inscription.models import AnneeAcademique, Classe, Etudiant, Inscription


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

Title = "Hello world"
pageinfo = "platypus example"
def certificatScolarite(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.restoreState()

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="inscription.pdf")



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



def listeEtudiantsInscripts(request):
    annees = AnneeAcademique.objects.all()
    classes = Classe.objects.all()
    context = {}
    context['annees'] = annees
    context['classes'] = classes

    if request.method == 'POST':
        annee_academique_id = request.POST.get('annee_academique')
        classe_id = request.POST.get('classe')

        etudiants = Inscription.get_etudiants_inscrits(annee_academique_id, classe_id)
        context['etudiants'] = etudiants
  
        return  render(request,'inscription/etudiants_inscrits.html', context)
    else:
        return render(request,'inscription/etudiants_inscrits.html', context)



def imprimerCertificatScolarite(request):
    annee_id = request.POST.get('annee_id')
    classe_id = request.POST.get('classe_id')
    etudiant_id = request.POST.get('etudiant_id')

    annee =  AnneeAcademique.objects.filter(id=annee_id).first
    classe =  Classe.objects.filter(id=classe_id).first
    etudiant =  Etudiant.objects.filter(id=etudiant_id).first




