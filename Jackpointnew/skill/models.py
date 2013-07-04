from django.db import models

 


class Skill(models.Model):  
    Parent = models.ManyToManyField("self",blank=True, null=True)
    Child = models.ManyToManyField("self",blank=True, null=True)
    Level = models.IntegerField()
    Nom = models.CharField(max_length=128)
    Description = models.TextField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Skill_Skill_Admin")
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.Nom

    
    
# Create your models here.
