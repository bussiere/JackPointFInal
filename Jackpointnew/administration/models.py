from django.db import models

# Create your models here.



class Administration(models.Model):
	Commentaire = models.TextField()
	Creator = models.ForeignKey("jack.UserProfile",related_name="Creator")
	Visibility = models.BooleanField(default=True)
	VisibilityStatut = models.ManyToManyField("jack.Statut",null=True, blank=True)
	Locked = models.BooleanField(default=False)
	DateFinLock = models.DateTimeField(null=True, blank=True)
	Date = models.DateTimeField(auto_now_add=True, blank=True)
	Solved = models.BooleanField(default=False)

# partie Administration
class Administrateur(models.Model):
	Nom = models.TextField()
	Commentaire = models.TextField()
	User = models.ForeignKey("jack.UserProfile",related_name="Administration_Administrateur_User")

class GroupeAdministrateur(models.Model):
	Nom = models.TextField()
	Commentaire = models.TextField()
	Admin = models.ManyToManyField("Administrateur",related_name="Administration_GroupeAdministrateur_Admin")

