# -*- coding:utf-8 -*-
from django.conf.urls import url
from event_influence import views

urlpatterns = [
    url(r'^event_infl_overview/$', views.event_infl_overview, name="event_infl_overview"),
    url(r'^event_hot_word/$', views.event_hot_word, name="event_hot_word"),
    url(r'^event_propagation_trace/$', views.event_propagation_trace, name="event_propagation_trace"),
    url(r'^event_atti_stas/$', views.event_atti_stas, name="event_atti_stas"),
]
