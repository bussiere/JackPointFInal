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
from lieu.models import Lieu,Adresse
from lieu.models import GPS,Geohash,CP,Ville,Region,Pays
from date.models import Plage


def enregistrementPlace(request,caracs,skills,items,tags,place):
    #Todo
    #Faire les verifs avant si existe pas Lieu et tout
    Place = Place.objects.create() 
    Lieu = Lieu.objects.create() 
    Lieu.save()
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
    try :
            result = GPS.objects.get(Coord=place['GPS'])
    except :
            result = GPS.objects.create(Coord=place['GPS'])
            result.save()
    Lieu.GPS = result
    Lieu.save()
    try :
            result = Geohash.objects.get(Hash=place['Geohash'])
    except :
            result = Geohash.objects.create(Hash=place['Geohash'])
            result.save()
    Lieu.Geohash = result
    Lieu.save()
    i = 0
    for adresse in place['Adresse'] :
        numero = place['NumAdresse'][i]
        try :
            result = Adresse.objects.get(Rue=adresse,Numero=numero)
        except :
            result = Adresse.objects.create(Rue=adresse,Numero=numero)
            result.save()
        i += 1
        Lieu.Adresse.add(result)
        Lieu.save()
    
    try :
            result = CP.objects.get(Nom=place['CP'])
    except :
            result = CP.objects.create(Nom=place['CP'])
            result.save()
    Lieu.CP = result
    Lieu.save()
    
    try :
            result = Ville.objects.get(Nom=place['Ville'] )
    except :
            result = Ville.objects.create(Nom=place['Ville'] )
            result.save()
    Lieu.Ville = result
    Lieu.save()
    
    try :
            result = Region.objects.get(Nom=place['Region'])
    except :
            result = Region.objects.create(Nom=place['Region'])
            result.save()
    Lieu.Region = result
    Lieu.save()
    
    try :
            result = Pays.objects.get(Nom=place['Pays'])
    except :
            result = Pays.objects.create(Nom=place['Pays'])
            result.save()
    Lieu.Pays = result
    Lieu.save()
    Place.Lieu = Lieu
    Place.Telephone = place['Telephone'] 
    Place.Email =  place['Email'] 
    Place.Commentaire =  place['Commentaire'] 
    Place.save()
   
   #En cours
   #TODO
   # A refaire en propre.
    plage = []
    try :
            result = Plage.objects.get(DebutH=place['LundiM1'],DebutM= place['LundiM11'],FinH=place['LundiM2'], FinM=place['LundiM22'])
    except :
            result = Plage.objects.create(DebutH=place['LundiM1'],DebutM= place['LundiM11'],FinH=place['LundiM2'], FinM=place['LundiM22'])
            result.save()
    plage.append(result)
    



    place['LundiAM1'] = request.POST['LundiAM1']
    place['LundiAM11'] = request.POST['LundiAM11']
    place['LundiAM2'] = request.POST['LundiAM2']
    place['LundiAM22'] = request.POST['LundiAM22']
    place['MardiM1'] = request.POST['MardiM1']
    place['MardiM11'] = request.POST['MardiM11']
    place['MardiM2'] = request.POST['MardiM2']
    place['MardiM22'] = request.POST['MardiM22']
    place['MardiAM1'] = request.POST['MardiAM1']
    place['MardiAM11'] = request.POST['MardiAM11']
    place['MardiAM2'] = request.POST['MardiAM2']
    place['MardiAM22'] = request.POST['MardiAM22']
    place['MercrediM1'] = request.POST['MercrediM1']
    place['MercrediM11'] = request.POST['MercrediM11']
    place['MercrediM2'] = request.POST['MercrediM2']
    place['MercrediM22'] = request.POST['MercrediM22']
    place['MercrediAM1'] = request.POST['MercrediAM1']
    place['MercrediAM11'] = request.POST['MercrediAM11']
    place['MercrediAM2'] = request.POST['MercrediAM2']
    place['MercrediAM22'] = request.POST['MercrediAM22']
    place['JeudiM1'] = request.POST['JeudiM1']
    place['JeudiM11'] = request.POST['JeudiM11']
    place['JeudiM2'] = request.POST['JeudiM2']
    place['JeudiM22'] = request.POST['JeudiM22']
    place['JeudiAM1'] = request.POST['JeudiAM1']
    place['JeudiAM11'] = request.POST['JeudiAM11']
    place['JeudiAM2'] = request.POST['JeudiAM2']
    place['JeudiAM22'] = request.POST['JeudiAM22']
    place['VendrediM1'] = request.POST['VendrediM1']
    place['VendrediM11'] = request.POST['VendrediM11']
    place['VendrediM2'] = request.POST['VendrediM2']
    place['VendrediM22'] = request.POST['VendrediM22']
    place['VendrediAM1'] = request.POST['VendrediAM1']
    place['VendrediAM11'] = request.POST['VendrediAM11']
    place['VendrediAM2'] = request.POST['VendrediAM2']
    place['VendrediAM22'] = request.POST['VendrediAM22']
    place['SamediM1'] = request.POST['SamediM1']
    place['SamediM11'] = request.POST['SamediM11']
    place['SamediM2'] = request.POST['SamediM2']
    place['SamediM22'] = request.POST['SamediM22']
    place['SamediAM1'] = request.POST['SamediAM1']
    place['SamediAM11'] = request.POST['SamediAM11']
    place['SamediAM2'] = request.POST['SamediAM2']
    place['SamediAM22'] = request.POST['SamediAM22']
    place['DimancheM1'] = request.POST['DimancheM1']
    place['DimancheM11'] = request.POST['DimancheM11']
    place['DimancheM2'] = request.POST['DimancheM2']
    place['DimancheM22'] = request.POST['DimancheM22']
    place['DimancheAM1'] = request.POST['DimancheAM1']
    place['DimancheAM11'] = request.POST['DimancheAM11']
    place['DimancheAM2'] = request.POST['DimancheAM2']
    place['DimancheAM22'] = request.POST['DimancheAM22']
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