from django.conf.urls import url
from . import views
urlpatters=[
    url('/',views.index,name ='index'),
]