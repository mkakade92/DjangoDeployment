from django.conf.urls import url
from django.urls import path,include
from basicApp import views

#Template Tagging

app_name= 'basicApp'

urlpatterns=[
    url('registration',views.register,name='registration'),
    url('user_login',views.user_login,name='user_login'),
]
