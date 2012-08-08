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
        place['Categorie'] = []
        place['Nom'] = request.POST['Nom']
        place['Categorie'].append(request.POST['Categorie1'])
        place['Categorie'].append(request.POST['Categorie2'])
        place['Categorie'].append(request.POST['Categorie3'])
        place['GPS'] = request.POST['GPS']
        place['Geohash'] = request.POST['Hash']
        place['Adresse'] = []
        place['Adresse'].append(request.POST['AD1'])
        place['Adresse'].append(request.POST['AD2'])
        place['Adresse'].append(request.POST['AD3'])
        place['Adresse'].append(request.POST['AD4'])
        place['NumAdresse'] = []
        place['NumAdresse'].append(request.POST['NumAD1'])
        place['NumAdresse'].append(request.POST['NumAD2'])
        place['NumAdresse'].append(request.POST['NumAD3'])
        place['NumAdresse'].append(request.POST['NumAD4'])
        place['CP'] = request.POST['CP']
        place['Ville'] = request.POST['Ville']
        place['Region'] = request.POST['Region']
        place['Pays'] = request.POST['Pays']
        place['Telephone'] = request.POST['Tel']
        place['Email'] = request.POST['Email']
        place['LundiM1'] = request.POST['LundiM1']
        place['LundiM2'] = request.POST['LundiM2']
        place['LundiAM1'] = request.POST['LundiAM1']
        place['LundiAM2'] = request.POST['LundiAM2']
        place['MardiM1'] = request.POST['MardiM1']
        place['MardiM2'] = request.POST['MardiM2']
        place['MardiAM1'] = request.POST['MardiAM1']
        place['MardiAM2'] = request.POST['MardiAM2']
        place['MercrediM1'] = request.POST['MercrediM1']
        place['MercrediM2'] = request.POST['MercrediM2']
        place['MercrediAM1'] = request.POST['MercrediAM1']
        place['MercrediAM2'] = request.POST['MercrediAM2']
        place['JeudiM1'] = request.POST['JeudiM1']
        place['JeudiM2'] = request.POST['JeudiM2']
        place['JeudiAM1'] = request.POST['JeudiAM1']
        place['JeudiAM2'] = request.POST['JeudiAM2']
        place['VendrediM1'] = request.POST['VendrediM1']
        place['VendrediM2'] = request.POST['VendrediM2']
        place['VendrediAM1'] = request.POST['VendrediAM1']
        place['VendrediAM2'] = request.POST['VendrediAM2']
        place['SamediM1'] = request.POST['SamediM1']
        place['SamediM2'] = request.POST['SamediM2']
        place['SamediAM1'] = request.POST['SamediAM1']
        place['SamediAM2'] = request.POST['SamediAM2']
        place['DimancheM1'] = request.POST['DimancheM1']
        place['DimancheM2'] = request.POST['DimancheM2']
        place['DimancheAM1'] = request.POST['DimancheAM1']
        place['DimancheAM2'] = request.POST['DimancheAM2']
        place['URL1'] = request.POST['URL1']
        place['URL2'] = request.POST['URL2']
        place['URL3'] = request.POST['URL3']
        place['URL4'] = request.POST['URL4']
        place['URL5'] = request.POST['URL5']
        place['Transport1'] = request.POST['Transport1']
        place['Transport2'] = request.POST['Transport2']
        place['Transport3'] = request.POST['Transport3']
        place['Transport4'] = request.POST['Transport4']
        place['Transport5'] = request.POST['Transport5']
        place['Transport6'] = request.POST['Transport6']
        place['Commentaire'] = request.POST['Commentaire']
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