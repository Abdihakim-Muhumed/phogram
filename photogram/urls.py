from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    path('',views.profile,name ='profile'),
    path('timeline/',views.index,name='index'),
    path(r'new/photo', views.new_photo, name='new-photo'),
    path(r'edit/profile', views.edit_profile, name='edit-profile'),
    path(r'comment/(\d<photo_id>+)',views.comment,name='comment'),
    path(r'like/(\d<photo_id>+)',views.like_photo,name='like-photo'),
    path('people',views.people,name='people'),
    path(r'people/follow/(\d<user_id>+)',views.follow_user,name ='follow'),
]