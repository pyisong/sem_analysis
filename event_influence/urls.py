# -*- coding:utf-8 -*-
from django.conf.urls import url
from event_influence import views

urlpatterns = [
    url(r'^event_influence_overview_(\d*?)/$', views.event_influence_overview, name="event_influence_overview"),
    url(r'^event_hot_word_(\d*?)/$', views.event_hot_word, name="event_hot_word"),
    url(r'^event_propagation_trace_(\d*?)/$', views.event_propagation_trace, name="event_propagation_trace"),
    url(r'^event_attitude_statistics_(\d*?)/$', views.event_attitude_statistics, name="event_attitude_statistics"),
]
