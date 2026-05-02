from django.urls import path
from . import views
urlpatterns = [
    path('',views.Accueil, name="accueil"),
    path('Apropos/', views.Apropos, name='apropos'),
    path('Departements/<slug:slug>/', views.departements, name='liste_departements'),
    path('Departements/', views.departements, name='departements'),
    path('Méditation/<slug:slug>/', views.meditations, name='liste_meditations'),
    path('Méditation/', views.meditations, name='meditations'),
    path('Activites/', views.activites, name='activites'),
    path('Activites/<slug:slug>/', views.activites, name='liste_activites'),
    path('Interventions/<slug:slug>/', views.Interventions, name='liste_Interventions'),
    path('Interventions/', views.Interventions, name='Interventions'),
    path('Membres/<slug:slug>/', views.Members, name='liste_Membres'),
    path('Membres/', views.Members, name='Membres'),
    path('Contact/', views.Contact, name='contact'),
    
]
