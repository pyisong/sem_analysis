# -*- coding:utf-8 -*-
from django.conf.urls import url
from event_influence import views

urlpatterns = [
    url(r'^event_infl_overview/(\d*?)/$', views.event_infl_overview, name="event_infl_overview"),
    url(r'^event_hot_word/(\d*?)/$', views.event_hot_word, name="event_hot_word"),
    url(r'^event_propagation_trace/(\d*?)/$', views.event_propagation_trace, name="event_propagation_trace"),
    url(r'^event_atti_stas/(\d*?)/$', views.event_atti_stas, name="event_atti_stas"),
]
