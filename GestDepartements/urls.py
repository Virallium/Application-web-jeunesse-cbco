from django.urls import path
from . import views
urlpatterns = [
    path('',views.Accueil, name="accueil"),
    path('Apropos/', views.Apropos, name='apropos'),
    path('Departements/<slug:slug>/', views.departements, name='departements'),
    path('Méditation/<slug:slug>/', views.meditations, name='meditations'),
    path('Activites/<slug:slug>/', views.activites, name='activites'),
    path('Interventions/<slug:slug>/', views.Interventions, name='Interventions'),
    path('Membres/<slug:slug>/', views.Members, name='Membres'),
    path('Contact/', views.Contact, name='contact'),
    
]
