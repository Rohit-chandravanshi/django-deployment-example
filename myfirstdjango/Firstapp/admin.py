from django.contrib import admin

# Register your models here.

from Firstapp.models import Accessrecord,Topic,webpage,user,UserProfileInfo

admin.site.register(Accessrecord)
admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(user)
admin.site.register(UserProfileInfo)
