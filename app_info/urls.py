# -*- coding:utf-8 -*-
from django.conf.urls import url
from app_info import views

urlpatterns = [
    url(r'^app_bd_curve/(\d*?)/$', views.app_bd_curve, name="app_bd_curve"),
    url(r'^app_bd_info/(\d*?)/$', views.app_bd_info, name="app_bd_info"),
    url(r'^app_comt/(\d*?)/$', views.app_comt, name="app_comt"),
]
