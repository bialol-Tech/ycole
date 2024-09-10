from etablissement.models import Etablissement

def getData():
    etablissement = Etablissement.objects.first()

    data = {}
    data['etablissement'] = etablissement
    
    return data