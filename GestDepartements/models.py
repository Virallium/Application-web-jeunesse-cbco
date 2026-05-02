from django.db import models
from django.utils.text import slugify 
from django.urls import reverse

class Membres(models.Model):
    idMembre=models.AutoField(primary_key=True)
    nom=models.CharField( max_length=25, verbose_name="Nom Membre", null=True)
    prenom=models.CharField( max_length=25, verbose_name="Prenom Membre", null=True)
    postnom=models.CharField( max_length=25, verbose_name="PostNom Membre", null=True)
    photo=models.ImageField( upload_to="photos/Membres/", height_field=None, width_field=None, max_length=None, null=True)
    tel=models.CharField( max_length=13, verbose_name="téléphone", null=True)
    def __str__(self):
        return f"{self.nom}--{self.postnom}--{self.tel}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Très important pour le sitemap Google
        return reverse('Membres_detail', kwargs={'slug': self.slug})

class Departement(models.Model):
    idDepart=models.AutoField(primary_key=True)
    denomination=models.CharField(max_length=20, verbose_name="Denomination Departement")
    description=models.CharField(max_length=25, verbose_name="Description Departement" )
    NbrMembre=models.IntegerField(verbose_name="Nombre de Membre")
    def __str__(self):
        return self.denomination
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.denomination)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Très important pour le sitemap Google
        return reverse('Departement_detail', kwargs={'slug': self.slug})



class Activites(models.Model):
    IdAct=models.AutoField(primary_key=True)
    denomination=models.CharField(verbose_name="Dénomination Activité", max_length=50)
    photo=models.ImageField(upload_to="photos/Activites", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.denomination
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.denomination)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Très important pour le sitemap Google
        return reverse('Activités_detail', kwargs={'slug': self.slug})

class Categorie(models.Model):
    idCatg=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=25, null=True)
    idAct=models.ForeignKey(Activites, verbose_name="Id Activités", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class Participation(models.Model):
    date=models.DateField(auto_now=True)
    idMembre=models.ForeignKey(Membres, verbose_name="Id Membres", on_delete=models.CASCADE)
    idAct=models.ForeignKey(Activites, verbose_name="Id Activités", on_delete=models.CASCADE)
    def __str__(self):
        return self.idMembre
    
    
class Evolution(models.Model):
    Periode_evolution=models.DurationField(verbose_name="Periode d'evolution")
    idMembre=models.ForeignKey(Membres, verbose_name="Id Membre", on_delete=models.CASCADE)
    idDepart=models.ForeignKey(Departement, verbose_name="Id departement", on_delete=models.CASCADE)
    def __str__(self):
        return self.Periode_evolution

    
class Intervenant(models.Model):
    idInter=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=25, verbose_name="Nom de l'intervenant", null=True)
    prenom=models.CharField(max_length=25, verbose_name="Prenom de l'intervenant", null=True)
    postnom=models.CharField(max_length=25, verbose_name="Postnom de l'intervenant", null=True)
    photo=models.ImageField(upload_to="photos/Intervenants", height_field=None, width_field=None, max_length=None, null=True)
    tel=models.CharField(max_length=25, verbose_name="Telephone")
    def __str__(self):
        return f"{self.nom}--{self.postnom}"
    
class Intervention(models.Model):
    date_Intervention=models.DateField(auto_now=True)
    idAct=models.ForeignKey(Activites, verbose_name="Id Intervenant", on_delete=models.CASCADE)
    idInter=models.ForeignKey(Intervenant, verbose_name="Id intervenant", on_delete=models.CASCADE)
    def __str__(self):
        return self.date_Intervention
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.date_Intervention)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Très important pour le sitemap Google
        return reverse('Interventions_detail', kwargs={'slug': self.slug})

class meditation(models.Model):
    theme=models.CharField(max_length=25, verbose_name="Theme méditation")
    verset=models.CharField(max_length=25, verbose_name="verset")
    message=models.TextField(verbose_name="message")
    def __str__(self):
        return self.theme
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.theme)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Très important pour le sitemap Google
        return reverse('meditation_detail', kwargs={'slug': self.slug})



    
    
