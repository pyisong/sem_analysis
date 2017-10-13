# -*- coding:utf-8 -*-
from django.conf.urls import url
from product_influence import views

urlpatterns = [
    url(r'^product_search_exponent/$', views.product_search_exponent, name="product_search_exponent"),
    url(r'^product_sentiment_statistics_(\d*?)/$', views.product_sentiment_statistics,
        name="product_sentiment_statistics"),
    url(r'^product_information_influence_(\d*?)/$', views.product_information_influence,
        name="product_information_influence"),
    url(r'^product_data_statistics_(\d*?)/$', views.product_data_statistics, name="product_data_statistics"),
    url(r'^product_weibo_user_location_(\d*?)/$', views.product_weibo_user_location,
        name="product_weibo_user_location"),
    url(r'^product_hot_media_(\d*?)/$', views.product_hot_media, name="product_hot_media"),
]
