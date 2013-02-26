from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from skill.models import Skill

   
class ItemUser(models.Model):
    Item = models.ManyToManyField("item.Item")
    Private = models.BooleanField(default=False)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True)

LevelSkill = (
    (0, 'None Mais interesse'),
    (1, 'Debutant'),
    (2, 'Moyen'),
    (3, 'Doue'),
    (4, 'Bon'),
    (5, 'Expert'),
)

class SkillUser(models.Model):
    Skill = models.ManyToManyField("skill.Skill")
    Level = models.IntegerField(choices=LevelSkill)
    Private = models.BooleanField(default=False)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True)
    def __unicode__(self):
        Nom = ""
        for sk in self.Skill.all() :
            Nom = sk.id
        return "%s %d %r"%(Nom,self.Level,self.Private)

LevelCarac = (
    (1, 'Bof'),
    (2, 'Moyen'),
    (3, 'Pas mal'),
    (4, 'Bon'),
    (5, 'Tres Bon'),
)

class CaracUser(models.Model):
    Carac = models.ManyToManyField("carac.Carac")
    Level = models.IntegerField(choices=LevelCarac)
    Private = models.BooleanField(default=False)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_CaracUser_Admin")
    def __unicode__(self):
        #TODO
        #crade a revoir
        for c in self.carac.all() :
            t = c 
        return "%s %d %r"%(c.Nom,self.Level,self.Private)

class Statut(models.Model):
    Nom = models.CharField(max_length=256)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_Statut_Admin")
    #Group
    #Projet
    #Forum
    #SuperAdmin
    #Admin

class Communaute(models.Model):
    Nom = models.CharField(max_length=256)

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    Skills = models.ManyToManyField("SkillUser", blank=True, null=True,related_name="SkillUser")
    Tags = models.ManyToManyField("tag.Tag", blank=True, null=True,related_name="Tag")
    Items = models.ManyToManyField("ItemUser", blank=True, null=True,related_name="ItemUser")
    Caracs = models.ManyToManyField("CaracUser", blank=True, null=True,related_name="CaracUser")
    Pseudo = models.CharField(max_length=256)
    Bio = models.TextField()
    Email = models.EmailField()
    Avatar = models.ImageField(upload_to='Avatar')
    Finished = models.BooleanField(default=False)
    Statut = models.ManyToManyField("Statut", blank=True, null=True,related_name="StatutUser")
    Communaute = models.ManyToManyField("Communaute", blank=True, null=True,related_name="CommunauteUser")
    InvitationAccepted = models.OneToOneField("invitation.Invitation",related_name="InvitationAccepted", blank=True, null=True)
    InvitationGiven = models.ManyToManyField("invitation.Invitation",related_name="InvitationGiven", blank=True, null=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_UserProfile_Admin")
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):  
          return "%s's profile" % self.user  


class UserProfileTemp(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    Skills = models.ManyToManyField("SkillUser", blank=True, null=True,related_name="SkillUserTemp")
    Tags = models.ManyToManyField("tag.Tag", blank=True, null=True,related_name="TagTemp")
    Items = models.ManyToManyField("ItemUser", blank=True, null=True,related_name="ItemUserTemp")
    Caracs = models.ManyToManyField("CaracUser", blank=True, null=True,related_name="CaracUserTemp")
    Pseudo = models.CharField(max_length=256)
    Bio = models.TextField()
    Email = models.EmailField()
    Avatar = models.ImageField(upload_to='Avatar')
    Finished = models.BooleanField(default=False)
    Communaute = models.ManyToManyField("Communaute", blank=True, null=True,related_name="CommunauteUserTemp")
    Statut = models.ManyToManyField("Statut", blank=True, null=True,related_name="StatutUserTemp")
    InvitationAccepted = models.OneToOneField("invitation.Invitation",related_name="InvitationAcceptedTemp", blank=True, null=True)
    InvitationGiven = models.ManyToManyField("invitation.Invitation",related_name="InvitationGivenTemp", blank=True, null=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_UserProfileTemp_Admin")
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):  
          return "%s's profile" % self.user


class Createur(models.Model):  
    User =  models.ForeignKey(UserProfile, unique=False, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_Createur_Admin")

class Editeur(models.Model):  
    User =  models.ForeignKey(UserProfile, unique=False, null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Jack_Editeur_Admin")


class Amis(models.Model): 
    Amis =  models.ManyToManyField(UserProfile, unique=False, null=True, blank=True,related_name="Amis")

class Block(models.Model): 
    Block =  models.ManyToManyField(UserProfile, unique=False, null=True, blank=True,related_name="Block")



def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  



post_save.connect(create_user_profile, sender=User) 

