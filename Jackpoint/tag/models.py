from django.db import models

# Create your models here.
class Tag(models.Model):  
    Name = models.CharField(max_length=128,blank=True, null=True)
    Public = models.BooleanField(default=True)
    Administration = models.ManyToManyField("administration.Administration",null=True, blank=True,related_name="Tag_Tag_Admin")
    Date =  models.DateTimeField(auto_now_add=True, blank=True)