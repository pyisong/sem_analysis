# -*- coding:utf-8 -*-
from django.conf.urls import url
from sem_index import views

urlpatterns = [
    url(r'^infl_show/(\d*?)/$', views.infl_show, name="infl_show"),
    url(r'^search_exponent/$', views.search_exponent, name="search_exponent"),
    url(r'^infl_dire/(\d*?)/$', views.infl_dire, name="infl_dire"),
    url(r'^tod_sem/(\d*?)/$', views.tod_sem, name="tod_sem"),
    url(r'^tod_hot/(\d*?)/$', views.tod_hot, name="tod_hot"),
    url(r'^tod_inform/(\d*?)/$', views.tod_inform, name="tod_inform"),
    url(r'^weibo/(\d*?)/$', views.weibo, name="weibo"),
    url(r'^baidu_zhidao/(\d*?)/$', views.baidu_zhidao, name="baidu_zhidao"),
    url(r'^app_info/(\d*?)/$', views.app_info, name="app_info"),
]
