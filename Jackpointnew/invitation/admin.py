from django.contrib import admin
from invitation.models import Task,CategorieInvitation,Usage,Invitation,InvitationUsed
admin.site.register(Task)
admin.site.register(CategorieInvitation)
admin.site.register(Usage)
admin.site.register(Invitation)
admin.site.register(InvitationUsed)
