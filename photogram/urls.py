from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name ='index'),
    path(r'^new/photo$', views.new_photo, name='new-photo'),
]