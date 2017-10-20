# -*- coding:utf-8 -*-
from django.conf.urls import url
from sem_index import views

urlpatterns = [
    url(r'^influence_show/(\d*?)/$', views.influence_show, name="influence_show"),
    url(r'^search_exponent/$', views.search_exponent, name="search_exponent"),
    url(r'^influence_directive/(\d*?)/$', views.influence_directive, name="influence_directive"),
    url(r'^today_sem/(\d*?)/$', views.today_sem, name="today_sem"),
    url(r'^today_hot/(\d*?)/$', views.today_hot, name="today_hot"),
    url(r'^today_information/(\d*?)/$', views.today_information, name="toady_information"),
    url(r'^weibo/(\d*?)/$', views.weibo, name="weibo"),
    url(r'^baidu_zhidao/(\d*?)/$', views.baidu_zhidao, name="baidu_zhidao"),
    url(r'^app_info/(\d*?)/$', views.app_info, name="app_info"),
]
