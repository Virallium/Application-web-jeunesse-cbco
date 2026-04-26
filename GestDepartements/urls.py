from django.urls import path
from . import views
urlpatterns = [
    path('',views.Accueil, name="accueil"),
    path('Apropos/', views.Apropos, name='apropos'),
    path('Departements/', views.Departements, name='departements'),
    path('Méditation/', views.meditations, name='meditations'),
    path('Activites/', views.activites, name='activites'),
    path('Contact/', views.Contact, name='contact'),
]
