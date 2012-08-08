from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from carac.forms import CaracFormChoice
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from hand.forms import AskForm
from hand.models import Question,Answer
from jack.models import CaracUser,SkillUser,ItemUser
from tag.models import Tag
from engine.models import ThreadEngine
from engine.script import sendnotificationPlace
from place.models import Place,CategoriePlace

def enregistrementPlace(request,caracs,skills,items,tags,place):
    Place = Place.objects.create() 
    Place.save()
    Place.Createur =  User.objects.get(id=request.user.id)
    Place.Nom = place['Nom']
    Place.save()
    for categorie in place['Categorie'] :
        try :
            result = CategoriePlace.objects.get(Nom=categorie)
        except :
            result = CategoriePlace.objects.create(Nom=categorie)
            result.save()
        Place.Categorie.add(result)
    Place.save()
    place['GPS']
    place['Geohash'] 
    place['Adresse1']
    place['Adresse2'] 
    place['Adresse3'] 
    place['Adresse4'] 
    place['CP']
    place['Ville'] 
    place['Region'] 
    place['Pays'] 
    place['Telephone'] 
    place['Email'] 
    place['LundiM1'] 
    place['LundiM2'] 
    place['LundiAM1'] 
    place['MardiM1'] 
    place['MardiM2'] 
    place['MardiAM1'] 
    place['MardiAM2']
    place['MercrediM1']
    place['MercrediM2'] 
    place['MercrediAM1']
    place['MercrediAM2'] 
    place['JeudiM1']
    place['JeudiM2'] 
    place['JeudiAM1'] 
    place['JeudiAM2'] 
    place['VendrediM1']
    place['VendrediM2']
    place['VendrediAM1'] 
    place['VendrediAM2'] 
    place['SamediM1'] 
    place['SamediM2'] 
    place['SamediAM1'] 
    place['SamediAM2'] 
    place['DimancheM1'] 
    place['DimancheM2'] 
    place['DimancheAM1'] 
    place['DimancheAM2'] 
    place['URL1'] 
    place['URL2'] 
    place['URL3'] 
    place['URL4'] 
    place['URL5'] 
    place['Transport1'] 
    place['Transport2']
    place['Transport3'] 
    place['Transport4'] 
    place['Transport5'] 
    place['Transport6']
    place['Commentaire'] 
    Place.save()
    #TODO
    #Factoriser et expliquer les tags
    tags = tags.split('#')
    # TODO
    # A factoriser
    for tag in tags :
        tag = tag.strip()
        try :
            result = Tag.objects.get(Name=tag)
        except :
            result = Tag.objects.create(Name=tag)
            result.save()
        Place.Tags.add(result)
    Place.save()
    for carac in caracs.keys():
        caracdb  = Carac.objects.get(Nom=carac)
        try :
            result = CaracUser.objects.get(carac=caracdb,Level=int(caracs[carac][0]))
        except :
            result = CaracUser.objects.create(Level=0)
            result.Carac.add(caracdb)
            result.Level = int(caracs[carac][0])
            result.save()
        Place.Caracs.add(result)
    for skill in skills.keys():
        skilldb  = Skill.objects.get(Nom=skill)
        print "nomSki"
        print skilldb.Nom
        private = False
        try :
            result = SkillUser.objects.get(Skills=skilldb,Level=int(skills[skill][0]))
        except :
            result = SkillUser.objects.create(Level=0)
            result.Skill.add(skilldb)
            result.Private = private
            result.Level = int(skills[skill][0])
            result.save()
        Place.Skills.add(result)
    for item in items.keys():
        itemdb  = Item.objects.get(Nom=item)
        try :
            result = ItemUser.objects.get(Item=itemdb)
        except :
            result = ItemUser.objects.create()
            result.Item.add(itemdb)
            result.Private = private
            result.save()
        Place.Items.add(result)
    Place.save()
    sendnotificationPlace()