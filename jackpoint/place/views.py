# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from jack.models import UserProfile
from carac.forms import CaracForm
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from jack.scripts import enregistrementJack
from django.http import HttpResponseRedirect
from jack.models import CaracUser,SkillUser,ItemUser
from place.models import Place
from carac.forms import CaracFormChoice
from skill.forms import SkillFormChoice
from item.forms import ItemFormChoice
from place.forms import AddPlaceForm 
from place.script import enregistrementPlace
@login_required
def viewid(request,id):
    place = Place.objects.get(id=id)
    return render_to_response('placeviewid.html', {'place':place},RequestContext(request))# Create

@login_required
def addplace(request):
    if request.method == 'POST': # If the form has been submitted...
        nbre_carac = int(request.POST['carac-TOTAL_FORMS'])
        nbre_initial_carac = request.POST['carac-INITIAL_FORMS']
        levelcarac="carac-#-carac_level"
        namecarac = "carac-#-carac"
        privatecarac = "carac-#-carac_private"
        compteur_carac = 0
        caracs = {}
        while compteur_carac < nbre_carac :
            if int(request.POST["carac-%d-carac_level"%compteur_carac]) >= 0 :
                caracs[request.POST["carac-%d-carac"%compteur_carac]] = [request.POST["carac-%d-carac_level"%compteur_carac]]
                compteur_carac += 1
        nbr_skills = int(request.POST['skill-TOTAL_FORMS'])
        nbr_initial_skills = request.POST['skill-INITIAL_FORMS']
        levelskill = "skill-#-skill_level"
        nameskill = "skill-#-skill"
        privateskill = "skill-#-skill_private"
        compteur_skill = 0
        skills = {}
        
        while compteur_skill < nbr_skills :
            if int(request.POST["skill-%d-skill_level"%compteur_skill]) >= 0 :
                skills[request.POST["skill-%d-skill"%compteur_skill]] = [request.POST["skill-%d-skill_level"%compteur_skill]]
            compteur_skill += 1
            
        nbre_item = int(request.POST['item-TOTAL_FORMS'])
        nbre_initial_item = request.POST['item-INITIAL_FORMS']
        Possede = "item-#-item_Possede"
        nameitem = "item-#-item"
        privatecarac = "item-#-item_private"
        compteur_item = 0
        items = {}
        while compteur_item < nbre_item :
            if int(request.POST["item-%d-item_Possede"%compteur_item]) > 0 :
                items[request.POST['item-%d-item'%compteur_item]] = request.POST["item-%d-item_private"%compteur_item]
            compteur_item += 1
        print caracs
        print skills
        print items
        place = {}
               try:
            place['Categorie'] = []
        except:
            pass
        try:
            place['Nom'] = request.POST['Nom']
        except:
            pass
        try:
            place['Categorie'].append(request.POST['Categorie1'])
        except:
            pass
        try:
            place['Categorie'].append(request.POST['Categorie2'])
        except:
            pass
        try:
            place['Categorie'].append(request.POST['Categorie3'])
        except:
            pass
        try:
            place['GPS'] = request.POST['GPS']
        except:
            pass
        try:
            place['Geohash'] = request.POST['Hash']
        except:
            pass
        try:
            place['Adresse'] = []
        except:
            pass
        try:
            place['Adresse'].append(request.POST['AD1'])
        except:
            pass
        try:
            place['Adresse'].append(request.POST['AD2'])
        except:
            pass
        try:
            place['Adresse'].append(request.POST['AD3'])
        except:
            pass
        try:
            place['Adresse'].append(request.POST['AD4'])
        except:
            pass
        try:
            place['NumAdresse'] = []
        except:
            pass
        try:
            place['NumAdresse'].append(request.POST['NumAD1'])
        except:
            pass
        try:
            place['NumAdresse'].append(request.POST['NumAD2'])
        except:
            pass
        try:
            place['NumAdresse'].append(request.POST['NumAD3'])
        except:
            pass
        try:
            place['NumAdresse'].append(request.POST['NumAD4'])
        except:
            pass
        try:
            place['CP'] = request.POST['CP']
        except:
            pass
        try:
            place['Ville'] = request.POST['Ville']
        except:
            pass
        try:
            place['Region'] = request.POST['Region']
        except:
            pass
        try:
            place['Pays'] = request.POST['Pays']
        except:
            pass
        try:
            place['Telephone'] = request.POST['Tel']
        except:
            pass
        try:
            place['Email'] = request.POST['Email']
        except:
            pass
        try:
            place['LundiM1'] = request.POST['LundiM1']
        except:
            pass
        try:
            place['LundiM11'] = request.POST['LundiM11']
        except:
            pass
        try:
            place['LundiM2'] = request.POST['LundiM2']
        except:
            pass
        try:
            place['LundiM22'] = request.POST['LundiM22']
        except:
            pass
        try:
            place['LundiAM1'] = request.POST['LundiAM1']
        except:
            pass
        try:
            place['LundiAM11'] = request.POST['LundiAM11']
        except:
            pass
        try:
            place['LundiAM2'] = request.POST['LundiAM2']
        except:
            pass
        try:
            place['LundiAM22'] = request.POST['LundiAM22']
        except:
            pass
        try:
            place['MardiM1'] = request.POST['MardiM1']
        except:
            pass
        try:
            place['MardiM11'] = request.POST['MardiM11']
        except:
            pass
        try:
            place['MardiM2'] = request.POST['MardiM2']
        except:
            pass
        try:
            place['MardiM22'] = request.POST['MardiM22']
        except:
            pass
        try:
            place['MardiAM1'] = request.POST['MardiAM1']
        except:
            pass
        try:
            place['MardiAM11'] = request.POST['MardiAM11']
        except:
            pass
        try:
            place['MardiAM2'] = request.POST['MardiAM2']
        except:
            pass
        try:
            place['MardiAM22'] = request.POST['MardiAM22']
        except:
            pass
        try:
            place['MercrediM1'] = request.POST['MercrediM1']
        except:
            pass
        try:
            place['MercrediM11'] = request.POST['MercrediM11']
        except:
            pass
        try:
            place['MercrediM2'] = request.POST['MercrediM2']
        except:
            pass
        try:
            place['MercrediM22'] = request.POST['MercrediM22']
        except:
            pass
        try:
            place['MercrediAM1'] = request.POST['MercrediAM1']
        except:
            pass
        try:
            place['MercrediAM11'] = request.POST['MercrediAM11']
        except:
            pass
        try:
            place['MercrediAM2'] = request.POST['MercrediAM2']
        except:
            pass
        try:
            place['MercrediAM22'] = request.POST['MercrediAM22']
        except:
            pass
        try:
            place['JeudiM1'] = request.POST['JeudiM1']
        except:
            pass
        try:
            place['JeudiM11'] = request.POST['JeudiM11']
        except:
            pass
        try:
            place['JeudiM2'] = request.POST['JeudiM2']
        except:
            pass
        try:
            place['JeudiM22'] = request.POST['JeudiM22']
        except:
            pass
        try:
            place['JeudiAM1'] = request.POST['JeudiAM1']
        except:
            pass
        try:
            place['JeudiAM11'] = request.POST['JeudiAM11']
        except:
            pass
        try:
            place['JeudiAM2'] = request.POST['JeudiAM2']
        except:
            pass
        try:
            place['JeudiAM22'] = request.POST['JeudiAM22']
        except:
            pass
        try:
            place['VendrediM1'] = request.POST['VendrediM1']
        except:
            pass
        try:
            place['VendrediM11'] = request.POST['VendrediM11']
        except:
            pass
        try:
            place['VendrediM2'] = request.POST['VendrediM2']
        except:
            pass
        try:
            place['VendrediM22'] = request.POST['VendrediM22']
        except:
            pass
        try:
            place['VendrediAM1'] = request.POST['VendrediAM1']
        except:
            pass
        try:
            place['VendrediAM11'] = request.POST['VendrediAM11']
        except:
            pass
        try:
            place['VendrediAM2'] = request.POST['VendrediAM2']
        except:
            pass
        try:
            place['VendrediAM22'] = request.POST['VendrediAM22']
        except:
            pass
        try:
            place['SamediM1'] = request.POST['SamediM1']
        except:
            pass
        try:
            place['SamediM11'] = request.POST['SamediM11']
        except:
            pass
        try:
            place['SamediM2'] = request.POST['SamediM2']
        except:
            pass
        try:
            place['SamediM22'] = request.POST['SamediM22']
        except:
            pass
        try:
            place['SamediAM1'] = request.POST['SamediAM1']
        except:
            pass
        try:
            place['SamediAM11'] = request.POST['SamediAM11']
        except:
            pass
        try:
            place['SamediAM2'] = request.POST['SamediAM2']
        except:
            pass
        try:
            place['SamediAM22'] = request.POST['SamediAM22']
        except:
            pass
        try:
            place['DimancheM1'] = request.POST['DimancheM1']
        except:
            pass
        try:
            place['DimancheM11'] = request.POST['DimancheM11']
        except:
            pass
        try:
            place['DimancheM2'] = request.POST['DimancheM2']
        except:
            pass
        try:
            place['DimancheM22'] = request.POST['DimancheM22']
        except:
            pass
        try:
            place['DimancheAM1'] = request.POST['DimancheAM1']
        except:
            pass
        try:
            place['DimancheAM11'] = request.POST['DimancheAM11']
        except:
            pass
        try:
            place['DimancheAM2'] = request.POST['DimancheAM2']
        except:
            pass
        try:
            place['DimancheAM22'] = request.POST['DimancheAM22']
        except:
            pass
        try:
            place['URL1'] = request.POST['URL1']
        except:
            pass
        try:
            place['URL2'] = request.POST['URL2']
        except:
            pass
        try:
            place['URL3'] = request.POST['URL3']
        except:
            pass
        try:
            place['URL4'] = request.POST['URL4']
        except:
            pass
        try:
            place['URL5'] = request.POST['URL5']
        except:
            pass
                try:
            place['TypeTransport1'] = request.POST['TypeTransport1']
        except:
            pass
        try:
            place['LigneTransport1'] = request.POST['LigneTransport1']
        except:
            pass
        try:
            place['Transport1'] = request.POST['Transport1']
        except:
            pass
        try:
            place['TypeTransport2'] = request.POST['TypeTransport2']
        except:
            pass
        try:
            place['LigneTransport2'] = request.POST['LigneTransport2']
        except:
            pass
        try:
            place['Transport2'] = request.POST['Transport2']
        except:
            pass
        try:
            place['TypeTransport3'] = request.POST['TypeTransport3']
        except:
            pass
        try:
            place['LigneTransport3'] = request.POST['LigneTransport3']
        except:
            pass
        try:
            place['Transport3'] = request.POST['Transport3']
        except:
            pass
        try:
            place['TypeTransport4'] = request.POST['TypeTransport4']
        except:
            pass
        try:
            place['LigneTransport4'] = request.POST['LigneTransport4']
        except:
            pass
        try:
            place['Transport4'] = request.POST['Transport4']
        except:
            pass
        try:
            place['TypeTransport5'] = request.POST['TypeTransport5']
        except:
            pass
        try:
            place['LigneTransport5'] = request.POST['LigneTransport5']
        except:
            pass
        try:
            place['Transport5'] = request.POST['Transport5']
        except:
            pass
        try:
            place['TypeTransport6'] = request.POST['TypeTransport6']
        except:
            pass
        try:
            place['LigneTransport6'] = request.POST['LigneTransport6']
        except:
            pass
        try:
            place['Transport6'] = request.POST['Transport6']
        except:
            pass
        try:
            place['Commentaire'] = request.POST['Commentaire']
        except:
            pass
        tags = request.POST['Tags']
        retour = enregistrementPlace(request,caracs,skills,items,tags,place)  
        return HttpResponseRedirect('../../place/view/') # Redirect after POST
    Caracs = Carac.objects.all()
    Skills = Skill.objects.all()
    Items = Item.objects.all()
    initial = []
    for carac in Caracs :
        initial.append({'carac': carac.Nom,'id':carac.id})
    CaracFormSet = formset_factory(CaracFormChoice, extra=0)
    CaracFormSet = CaracFormSet(prefix='carac',initial=initial)
    initial = []
    # algo de skills a revoir pour le classement
    for skill in Skills :
        initial.append({'skill': skill.Nom,'id':skill.id})
    SkillFormSet = formset_factory(SkillFormChoice, extra=0)
    SkillFormSet = SkillFormSet(prefix='skill',initial=initial)
    initial = []
    for item in Items :
        initial.append({'item': item.Nom,'id':item.id})
    ItemFormSet = formset_factory(ItemFormChoice, extra=0)
    ItemFormSet = ItemFormSet(prefix='item',initial=initial)
    form = AddPlaceForm()
    return render_to_response('addplace.html',{
        'form': form,"CaracFormSet":CaracFormSet,'SkillFormSet':SkillFormSet,'ItemFormSet':ItemFormSet
    },RequestContext(request))

@login_required
def editplace(request):
    return render_to_response('addplace.html',RequestContext(request))