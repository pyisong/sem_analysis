# -*- coding:utf-8 -*-
from django.conf.urls import url
from product_influence import views

urlpatterns = [
    url(r'^pro_search_exponent/$', views.pro_search_exponent, name="pro_search_exponent"),
    url(r'^pro_weixin_expression/(\d*?)/$', views.pro_weixin_expression, name="pro_weixin_expression"),
    url(r'^pro_inform_infl/(\d*?)/$', views.pro_inform_infl, name="pro_inform_infl"),
    url(r'^pro_data_stas/(\d*?)/$', views.pro_data_stas, name="pro_data_stas"),
    url(r'^pro_weibo_usr_loc/(\d*?)/$', views.pro_weibo_usr_loc, name="pro_weibo_usr_loc"),
    url(r'^pro_hot_med/(\d*?)/$', views.pro_hot_med, name="pro_hot_med"),
]
