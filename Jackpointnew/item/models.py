from django.db import models

# Create your models here.
class Item(models.Model):  
    Nom = models.CharField(max_length=128)
    Skills = models.ManyToManyField("skill.Skill")
    Description = models.TextField(max_length=256, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Item_Item_Administration")
    def __unicode__(self):
        return self.Nom
