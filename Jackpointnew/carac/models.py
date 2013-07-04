from django.db import models

class Carac (models.Model):  
    Nom = models.CharField(max_length=64, null=True, blank=True)
    Description = models.TextField(max_length=256, null=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Carac_Carac_Admin")
    def __unicode__(self):
        return self.Nom
