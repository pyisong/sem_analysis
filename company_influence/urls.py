# -*- coding:utf-8 -*-
from django.conf.urls import url
from company_influence import views

urlpatterns = [
    url(r'^company_search_exponent/$', views.company_search_exponent, name="company_search_exponent"),
    url(r'^company_official_influence_(\d*?)/$', views.company_official_influence,
        name="company_official_influence_compare"),
    url(r'^company_information_influence_(\d*?)/$', views.company_information_influence,
        name="company_information_influence"),
    url(r'^company_data_statistics_(\d*?)/$', views.company_data_statistics, name="company_data_statistics"),
    url(r'^company_weibo_user_location_(\d*?)/$', views.company_weibo_user_location,
        name="company_weibo_user_location"),
    url(r'^company_hot_media_(\d*?)/$', views.company_hot_media, name="company_hot_media"),
]
