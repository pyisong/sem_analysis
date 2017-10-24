# -*- coding:utf-8 -*-
from django.conf.urls import url
from sem_information import views

urlpatterns = [
    url(r'^inform_list/$', views.inform_list, name="inform_list"),
    url(r'^inform_det/$', views.inform_det, name="inform_det"),
]
