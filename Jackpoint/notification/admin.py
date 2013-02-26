from django.contrib import admin
from notification.models import CategorieNotification,Notification,PlaceNotification
admin.site.register(CategorieNotification)
admin.site.register(Notification)
admin.site.register(PlaceNotification)
