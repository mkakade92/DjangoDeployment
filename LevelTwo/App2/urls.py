from django.conf.urls import url
from django.urls import path
from App2 import views

urlpatterns = [
     path('',views.users,name="users"),
]
