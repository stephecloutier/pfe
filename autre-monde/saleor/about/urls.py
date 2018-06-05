from django.conf.urls import url
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^send/', views.send_contact_email, name='send-contact-email')
]
