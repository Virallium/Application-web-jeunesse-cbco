from django.shortcuts import render, get_object_or_404
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from .models import Activites, Categorie, Departement, Evolution,  Intervention, Membres,Participation, meditation
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


def culte_jeune(request):
    CHANNEL_ID="UCfCe4LT_UWFf8HeLPOZtxcA"
    UPLOAD_PLAYLIST_ID = "UU" + CHANNEL_ID[2:]
    API_KEY=os.getenv('YOUTUBE_API_KEY')
    videos=[]
    error_message=None
    
    try:
        youtube=build('youtube','v3',developerKey=API_KEY)
        request_api=youtube.playlistItems().list(
            playlistId=UPLOAD_PLAYLIST_ID,
            part='snippet',
            maxResults=30
        )
        response=request_api.execute()
        for item in response.get('items',[]):
            snippet = item.get('snippet', {})
            video_id = snippet.get('resourceId', {}).get('videoId')
            
            videos.append({
                'id': video_id,
                'title': snippet.get('title'),
                'thumbnail': snippet.get('thumbnails', {}).get('high', {}).get('url'),
                'published_at': snippet.get('publishedAt'),
            })  
    except HttpError as e:
        error_message="Impossible de charger les vidéos youtubes pour le moment."
    context={
        'videos':videos,
        'error_message':error_message
    }
        
    return render(request, 'pages/culte_jeune.html', context)