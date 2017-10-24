# -*- coding:utf-8 -*-
from django.conf.urls import url
from company_influence import views

urlpatterns = [
    url(r'^comp_search_exponent/$', views.comp_search_exponent, name="comp_search_exponent"),
    url(r'^comp_offi_infl/$', views.comp_offi_infl, name="comp_offi_infl"),
    url(r'^comp_inform_infl/$', views.comp_inform_infl, name="comp_inform_infl"),
    url(r'^comp_data_stas/$', views.comp_data_stas, name="comp_data_stas"),
    url(r'^comp_weibo_usr_loc/$', views.comp_weibo_usr_loc, name="comp_weibo_usr_loc"),
    url(r'^comp_hot_med/$', views.comp_hot_med, name="comp_hot_med"),
]
