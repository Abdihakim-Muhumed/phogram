from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    path('',views.profile,name ='profile'),
    path(r'new/photo$', views.new_photo, name='new-photo'),
    path(r'edit/profile', views.edit_profile, name='edit-profile'),
]