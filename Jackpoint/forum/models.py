from django.db import models

# Create your models here.


class Forum(models.Model):
    Description = models.TextField(null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True,related_name="Forum_Forum_Creator")
    Categorie = models.ManyToManyField("Categorie",blank=True, null=True)
    Tag = models.ManyToManyField("tag.Tag",null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_Forum_Admin")


class Categorie(models.Model):
    Description = models.TextField(null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True,related_name="Forum_Categorie_Creator")
    Thread = models.ManyToManyField("Thread",blank=True, null=True)
    Tag = models.ManyToManyField("tag.Tag",null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_Categorie_Admin")
    #Group
    #Projet
    #Private



class Thread(models.Model):
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Origin = models.ForeignKey("Post",null=True, blank=True,related_name="Origin")
    Post = models.ManyToManyField("Post",null=True, blank=True,related_name="PostThread")
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_Thread_Admin")
    Locked = models.BooleanField(default=False)
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True,related_name="Forum_Thread_Creator")
    Tag = models.ManyToManyField("tag.Tag",null=True, blank=True)

class Edition(models.Model):
    Text = models.TextField(null=True, blank=True)
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_Edition_Admin")


class Post(models.Model):
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True,related_name="Forum_Post_Creator")
    Text = models.TextField(null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Tag = models.ManyToManyField("tag.Tag",null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Parent = models.ManyToManyField("self",blank=True, null=True)
    Child = models.ManyToManyField("self",blank=True, null=True)
    Level = models.IntegerField()
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_Post_Admin")
    Locked = models.BooleanField(default=False)

class PostOld(models.Model):
    Creator = models.ManyToManyField("jack.UserProfile",null=True, blank=True,related_name="Forum_PostOld_Creator")
    Text = models.TextField(null=True, blank=True)
    Tag = models.ManyToManyField("tag.Tag",null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Parent = models.ManyToManyField("self",blank=True, null=True)
    Child = models.ManyToManyField("self",blank=True, null=True)
    Level = models.IntegerField()
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Forum_PostOld_Admin")
    Locked = models.BooleanField(default=False)




