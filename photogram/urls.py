from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.profile,name ='profile'),
    path(r'new/photo', views.new_photo, name='new-photo'),
    path(r'edit/profile', views.edit_profile, name='edit-profile'),
    path(r'comment/(\d<photo_id>+)',views.comment,name='comment'),
    path(r'like/(\d<photo_id>+)',views.like_photo,name='like-photo')
]