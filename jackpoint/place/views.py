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
from place.form import AddPlaceForm 
@login_required
def viewid(request,id):
    place = Place.objects.get(id=id)
    return render_to_response('placeviewid.html', {'place':place},RequestContext(request))# Create

@login_required
def addplace(request):
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