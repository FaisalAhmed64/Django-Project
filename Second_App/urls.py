from django.urls import re_path as url
from Second_App import views

urlpatterns=[
    url('', views.index, name='index'),
]