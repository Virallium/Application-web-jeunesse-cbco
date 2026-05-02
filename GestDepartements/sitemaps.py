from django.contrib.sitemaps import Sitemap
from .models import Activites, meditation, Intervenant

class ActiviteSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    def items(self):
        return Activites.objects.all()

class MeditationSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    def items(self):
        return meditation.objects.all()

class IntervenantSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Intervenant.objects.all()