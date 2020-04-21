from django.contrib import admin
from firstApp.models import Topic,Webpage,AccRecord
# Register your models here.

admin.site.register(AccRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
