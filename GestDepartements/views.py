from django.shortcuts import render
from .models import Activites, Categorie, Departement, Evolution, Intervenant, Intervention, Membres,Participation, meditation
def Accueil(request):
    activites=Activites.objects.all()
    versets=meditation.objects.all()[:2]
    return render(request, 'pages/index.html', {
        'actus':activites,
        'versets':versets
    })

def Apropos(request):
    return render(request,'pages/apropos.html')

def meditations(request):
    return render(request,'pages/meditation.html')

def activites(request):
    activities=Activites.objects.all()
    intervenant=Intervenant.objects.all()
    return render(request, 'pages/activites.html',{
        'activites':activities,
        'intervenants':intervenant
    })

def departements(request):
    departements=Departement.objects.all()
    membres=Membres.objects.all()
    return render(request, 'pages/departement.html',{
        'departements':departements,
        'membres':membres
    })
    
def Contact(request):
    return render(request, 'pages/contact.html')

def Members(request):
    return render(request,'pages/Membres.html')

def Interventions(request):
    return render(request,'pages/Interventions.html')

