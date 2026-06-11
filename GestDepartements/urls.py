from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('Authentification.urls')),
    path('Accueil/',views.Accueil, name="accueil"),
    path('Apropos/', views.Apropos, name='apropos'),
    path('Departements/<slug:slug>/', views.departements, name='liste_departements'),
    path('Departements/', views.departements, name='departements'),
    path('Méditation/<slug:slug>/', views.verset, name='liste_meditations'),
    path('Méditation/', views.verset, name='meditations'),
    path('Activites/', views.activites, name='activites'),
    path('Activites/<int:id>/',views.detail_activites, name='detail_activites'),
    path('Activites/<slug:slug>/', views.activites, name='liste_activites'),
    path('Membres/<slug:slug>/', views.Members, name='liste_Membres'),
    path('Membres/', views.Members, name='Membres'),
    path('culte/',views.culte_jeune, name='culte_jeune')
]
