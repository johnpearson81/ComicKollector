
import import_export
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from app.models import ComicInput
from app.models import Profile
from import_export import resources
from django.db import transaction
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

################ Include impirt/export functions for each Model ###################
class ComicInputFileAdmin(ImportExportModelAdmin):
    pass
    list_display = ("Title", "Type", "Number", "Grade","Value","CoverPic")
    list_filter = ("Title", "Grade","SellingNotes")

class ComicInputResource(resources.ModelResource):
    class Meta:
        model = ComicInput
        exclude = ('is_active',)

#class ProfileFileAdmin(ImportExportModelAdmin):
#    pass
#    list_display = ("id","user","email")
#    list_filter = ("id","user","email")

#class ProfileInputResource(resources.ModelResource):
#    class Meta:
#        model = Profile
        #exclude = ('is_active',)





#admin.site.register(Admin, TaskAdmin)


##################################################################
################ Admin Site Registration #########################


UserAdmin.list_display = ('id','username', 'is_active', 'date_joined', 'is_staff')

admin.site.unregister(User)
#admin.site.register(Profile, ProfileFileAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ComicInput, ComicInputFileAdmin)