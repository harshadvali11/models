from django.contrib import admin

# Register your models here.
from app.models import Topic,Webpage,Access_Records

#syntax fro registering ur models
# admin.site.register(modelname)


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)