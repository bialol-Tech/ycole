from django.shortcuts import redirect, render

# from inscription.forms import FormulaireInscriptionEtudiantForm
from etablissement.models import Etablissement, Responsable
from inscription.models import AnneeAcademique, Classe, Etudiant, Inscription

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from datetime import date

def certificatScolarite(request, etudiant_id, annee_id):
    # Créez une réponse HTTP pour le fichier PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificat_scolarite_{etudiant_id}.pdf"'

    # Créez le canevas pour le PDF
    p = canvas.Canvas(response, pagesize=A4)
    p.setTitle("Certificat de Scolarité")

    # Chemin du logo
    # logo_path = os.path.join(settings.STATIC_ROOT, 'images', 'logo.png')

    logo_url = Etablissement.objects.first().logo.path
    # Données de l'étudiant (à partir de la base de données)
    # Vous pouvez récupérer les informations de l'étudiant par son ID
    etudiant = Etudiant.objects.get(pk=etudiant_id)
    etablissement = etudiant.etablissement.nom
    nom_complet = f"{etudiant.nom} {etudiant.prenom}"
    annee_scolaire = annee_id  # Exemple, cela peut être dynamique
    libelle_annee = AnneeAcademique.objects.filter(pk=annee_id).first().libelle 
    signature_DE = Responsable.objects.filter(profile="DE").first().signature.path

    classe = Classe.objects.filter(inscription__annee_academique_id=annee_scolaire, inscription__etudiant_id=etudiant).first().libelle

    p.drawString( 3* cm, 27 * cm, "                             ")


    # Ajoutez le logo (x, y, largeur, hauteur)
    p.drawImage(logo_url, 8 * cm, 26 * cm, width=3 * cm, height=2.5 * cm, mask='auto')
    p.setFont("Helvetica", 10)

    p.drawString( 7 * cm, 25 * cm, "Ministère de l'Enseignement supérieur")
    p.drawString( 7 * cm, 24 * cm, f"{etablissement}")
    p.drawString( 7 * cm, 23 * cm, "Service scolarité")
    p.drawString( 7 * cm, 22 * cm, "                             ")



    # Ajouter des éléments sur le PDF
    p.setFont("Helvetica-Bold", 22)
    p.drawCentredString(10.5 * cm, 21 * cm, "CERTIFICAT DE SCOLARITE")

    p.drawString( 10.5 * cm, 21 * cm, "                             ")
    p.drawString( 10.5 * cm, 20 * cm, "                             ")
 

    p.setFont("Helvetica", 12)
    p.drawString(3 * cm, 20* cm, f"Je sousigné, Responsable des affaires académique  de {etablissement}, ")
    p.drawString(3 * cm, 19 * cm, f"certifie que par le présent que M/Mme {nom_complet} Né(e) le {etudiant.date_de_naissance} à ")
    p.drawString(3 * cm, 18 * cm, f"{etudiant.lieu_de_naissance}({etudiant.pays_de_naissance}) est régulièrement inscrit en {classe} pour l'année académique {libelle_annee}")
    p.drawString(3 * cm, 17 * cm, f"En foi de quoi, le présent certificat lui est délivré pour lui servir et valoir ce que de droit.")


    # Ajouter du contenu supplémentaire (signature, date, etc.)
    p.drawString(11 * cm, 15 * cm, "Fais à Libreville le : ____f{datetime.date}______")
    p.drawString(11 * cm, 13 * cm, "Le responsable des affaires académique ")

    p.drawImage(signature_DE, 11 * cm, 9 * cm, width=4 * cm, height=4 * cm, mask='auto')


    # Terminez la création du PDF
    p.showPage()
    p.save()

    return response


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
        # annee = AnneeAcademique.objects.filter(pk=annee_academique_id).first()
        context['etudiants'] = etudiants
        context['annee'] = annee_academique_id
  
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




