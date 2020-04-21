from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basicApp import views


#Template tagging
app_name= 'basicApp'
urlpatterns=[
    path('other/',views.other,name='other'),
    path('relative/',views.relUrl,name='relativeURL'),
]
