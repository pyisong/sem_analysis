# -*- coding:utf-8 -*-
from django.conf.urls import url
from app_info import views

urlpatterns = [
    url(r'^app_bangdan_curve_(\d*?)/$', views.app_bangdan_curve, name="app_bangdan_curve"),
    url(r'^app_bangdan_info_(\d*?)/$', views.app_bangdan_info, name="app_bangdan_info"),
    url(r'^app_comment_(\d*?)/$', views.app_comment, name="app_comment"),
]
