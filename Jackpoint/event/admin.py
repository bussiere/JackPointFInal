from django.contrib import admin
from event.models import CategorieEvent,Url,Event,OldEvent
admin.site.register(CategorieEvent)
admin.site.register(Url)
admin.site.register(Event)
admin.site.register(OldEvent)
