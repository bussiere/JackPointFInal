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
    try :
            result = Plage.objects.get(DebutH=place['LundiAM1'],DebutM= place['LundiAM11'],FinH=place['LundiAM2'], FinM=place['LundiAM22'])
    except :
            result = Plage.objects.create(DebutH=place['LundiAM1'],DebutM= place['LundiAM11'],FinH=place['LundiAM2'], FinM=place['LundiAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['MardiM1'],DebutM= place['MardiM11'],FinH=place['MardiM2'], FinM=place['MardiM22'])
    except :
            result = Plage.objects.create(DebutH=place['MardiM1'],DebutM= place['MardiM11'],FinH=place['MardiM2'], FinM=place['MardiM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['MardiAM1'],DebutM= place['MardiAM11'],FinH=place['MardiAM2'], FinM=place['MardiAM22'])
    except :
            result = Plage.objects.create(DebutH=place['MardiAM1'],DebutM= place['MardiAM11'],FinH=place['MardiAM2'], FinM=place['MardiAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['MercrediM1'],DebutM= place['MercrediM11'],FinH=place['MercrediM2'], FinM=place['MercrediM22'])
    except :
            result = Plage.objects.create(DebutH=place['MercrediM1'],DebutM= place['MercrediM11'],FinH=place['MercrediM2'], FinM=place['MercrediM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['MercrediAM1'],DebutM= place['MercrediAM11'],FinH=place['MercrediAM2'], FinM=place['MercrediAM22'])
    except :
            result = Plage.objects.create(DebutH=place['MercrediAM1'],DebutM= place['MercrediAM11'],FinH=place['MercrediAM2'], FinM=place['MercrediAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['JeudiM1'],DebutM= place['JeudiM11'],FinH=place['JeudiM2'], FinM=place['JeudiM22'])
    except :
            result = Plage.objects.create(DebutH=place['JeudiM1'],DebutM= place['JeudiM11'],FinH=place['JeudiM2'], FinM=place['JeudiM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['JeudiAM1'],DebutM= place['JeudiAM11'],FinH=place['JeudiAM2'], FinM=place['JeudiAM22'])
    except :
            result = Plage.objects.create(DebutH=place['JeudiAM1'],DebutM= place['JeudiAM11'],FinH=place['JeudiAM2'], FinM=place['JeudiAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['VendrediM1'],DebutM= place['VendrediM11'],FinH=place['VendrediM2'], FinM=place['VendrediM22'])
    except :
            result = Plage.objects.create(DebutH=place['VendrediM1'],DebutM= place['VendrediM11'],FinH=place['VendrediM2'], FinM=place['VendrediM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['VendrediAM1'],DebutM= place['VendrediAM11'],FinH=place['VendrediAM2'], FinM=place['VendrediAM22'])
    except :
            result = Plage.objects.create(DebutH=place['VendrediAM1'],DebutM= place['VendrediAM11'],FinH=place['VendrediAM2'], FinM=place['VendrediAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['SamediM1'],DebutM= place['SamediM11'],FinH=place['SamediM2'], FinM=place['SamediM22'])
    except :
            result = Plage.objects.create(DebutH=place['SamediM1'],DebutM= place['SamediM11'],FinH=place['SamediM2'], FinM=place['SamediM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['SamediAM1'],DebutM= place['SamediAM11'],FinH=place['SamediAM2'], FinM=place['SamediAM22'])
    except :
            result = Plage.objects.create(DebutH=place['SamediAM1'],DebutM= place['SamediAM11'],FinH=place['SamediAM2'], FinM=place['SamediAM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['DimancheM1'],DebutM= place['DimancheM11'],FinH=place['DimancheM2'], FinM=place['DimancheM22'])
    except :
            result = Plage.objects.create(DebutH=place['DimancheM1'],DebutM= place['DimancheM11'],FinH=place['DimancheM2'], FinM=place['DimancheM22'])
            result.save()
    plage.append(result)
    try :
            result = Plage.objects.get(DebutH=place['DimancheAM1'],DebutM= place['DimancheAM11'],FinH=place['DimancheAM2'], FinM=place['DimancheAM22'])
    except :
            result = Plage.objects.create(DebutH=place['DimancheAM1'],DebutM= place['DimancheAM11'],FinH=place['DimancheAM2'], FinM=place['DimancheAM22'])
            result.save()
    plage.append(result)

    place['URL1'] 
    place['URL2'] 
    place['URL3'] 
    place['URL4'] 
    place['URL5'] 
    place['TypeTransport1']
    place['LigneTransport1']
    place['Transport1']
    place['TypeTransport2']
    place['LigneTransport2']
    place['Transport2']
    place['TypeTransport3']
    place['LigneTransport3']
    place['Transport3']
    place['TypeTransport4']
    place['LigneTransport4']
    place['Transport4']
    place['TypeTransport5']
    place['LigneTransport5']
    place['Transport5']
    place['TypeTransport6']
    place['LigneTransport6']
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