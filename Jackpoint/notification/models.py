from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategorieNotification(models.Model):  
    Nom = models.CharField(max_length=128)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Notification_Categorie_Admin")
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.Nom

class Notification(models.Model):  
    user = models.OneToOneField(User)  
    Nom = models.CharField(max_length=128)
    Texte = models.TextField(max_length=256, null=True, blank=True)
    hand = models.ManyToManyField("hand.Question", blank=True, null=True)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Notification_Notification_Admin")
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.Nom

class PlaceNotification(models.Model):  
    user = models.OneToOneField(User)  
    Nom = models.CharField(max_length=128)
    Texte = models.TextField(max_length=256, null=True, blank=True)
    Place = models.ManyToManyField("place.Place", blank=True, null=True)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Notification_Place_Admin")
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.Nom

#Notification News
#Notification Group
#Notification Projet