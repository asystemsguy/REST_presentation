# Copyright (c) 2018 Zeyad Tamimi.  All rights reserved.

# External Imports
from django.urls import path, re_path
# Project Imports
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^messages/(?:(?P<message_id>[0-9]+)/)?$', views.Messages.as_view(), name='Chat'),
    re_path(r'profiles/(?:(?P<profile_id>[0-9]+)/)?$', views.Profiles.as_view(), name='index'),
]
