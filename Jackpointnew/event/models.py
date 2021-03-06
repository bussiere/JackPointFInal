from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# TODO rajouter commentaires USER sur les events.

class CategorieEvent(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Event_Categorie_Admin")
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class Url(models.Model):
    Link = models.TextField(max_length=1024, null=True, blank=True)
    Description = models.TextField(max_length=1024, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Event_Url_Admin")
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.Link)


class Event(models.Model):  
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Categorie = models.ManyToManyField('CategorieEvent', null=True, blank=True)
    Texte = models.TextField(max_length=1024, null=True, blank=True)
    Url = models.ManyToManyField('Url', null=True, blank=True)
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("jack.ItemUser", null=True, blank=True)
    Caracs = models.ManyToManyField("jack.CaracUser", null=True, blank=True)
    Invited = models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventInvited")
    Maybe = models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventMaybe")
    Going =  models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventGoing")
    Horaire = models.ManyToManyField('date.DateJourHoraire',null=True, blank=True)
    Place = models.ManyToManyField('place.Place',null=True, blank=True)
    Createur = models.ForeignKey('jack.Createur',null=True, blank=True)
    Editeur = models.ForeignKey('jack.Editeur',null=True, blank=True)    
    Date = models.DateTimeField(auto_now_add=True, blank=True) 
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Event_Event_Admin")
    #TODO
    # Why not faire le save et ecrire le texte en fonciton de la langue ?
    def __unicode__(self):
        return str(self.User.id)


class OldEvent(models.Model):  
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Categorie = models.ManyToManyField('CategorieEvent', null=True, blank=True)
    Texte = models.TextField(max_length=1024, null=True, blank=True)
    Url = models.ManyToManyField('Url', null=True, blank=True)
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("jack.ItemUser", null=True, blank=True)
    Caracs = models.ManyToManyField("jack.CaracUser", null=True, blank=True)
    Invited = models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventOldInvited")
    Maybe = models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventOldMaybe")
    Going =  models.ManyToManyField(User, unique=False, null=True, blank=True,related_name="EventOldGoing")
    Horaire = models.ManyToManyField('date.DateJourHoraire',null=True, blank=True)
    Place = models.ManyToManyField('place.Place',null=True, blank=True)
    Createur = models.ForeignKey('jack.Createur',null=True, blank=True)
    Editeur = models.ForeignKey('jack.Editeur',null=True, blank=True)    
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Event_EventOld_Admin")
    #TODO
    # Why not faire le save et ecrire le texte en fonciton de la langue ?
    def __unicode__(self):
        return str(self.User.id)
