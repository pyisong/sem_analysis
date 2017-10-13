# -*- coding:utf-8 -*-
from django.conf.urls import url
from sem_information import views

urlpatterns = [
    url(r'^information_list/$', views.information_list, name="information_list"),
    url(r'^information_detail/$', views.information_detail, name="information_detail"),
]
