from django.shortcuts import render, get_object_or_404
from .models import Activites, Categorie, Departement, Evolution, Intervenant, Intervention, Membres,Participation, meditation
def Accueil(request):
    activites=Activites.objects.all()[:10]
    versets=meditation.objects.all()[:2]
    return render(request, 'pages/index.html', {
        'actus':activites,
        'versets':versets
    })

def Apropos(request):
    return render(request,'pages/apropos.html')

def verset(request):
    versets=meditation.objects.all()
    return render(request,'pages/meditation.html',{'versets_all':versets})

def activites(request):
    activities=Activites.objects.all()
    return render(request, 'pages/activites.html',{
        'activites':activities,

    })

def detail_activites(request,id):
    activities=get_object_or_404(Activites, IdAct=id)
    interventions=Intervention.objects.filter(idAct=activities).select_related('idInter')
    return  render(request,'pages/detail_activites.html',{
        'activite':activities,
        'interventions':interventions
    })
def departements(request):
    departements=Departement.objects.all()
    membres=Membres.objects.all()
    return render(request, 'pages/departement.html',{
        'departements':departements,
        'membres':membres
    })
    

def Members(request):
    return render(request,'pages/Membres.html')

def Interventions(request):
    return render(request,'pages/Interventions.html')
