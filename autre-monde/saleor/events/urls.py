from django.conf.urls import url
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^(?P<date>(?:0[1-9]|1[0-2]?)-(?:200[2-9]|2[0-9][1-9][0-9]))/$',
        views.calendar, name='calendar-date'),
]
