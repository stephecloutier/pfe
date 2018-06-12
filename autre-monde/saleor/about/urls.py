from django.conf.urls import url
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^(?P<product_slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/$',
        views.about_cta_contact, name='about-contact'),
    url(r'^send/', views.send_contact_email, name='send-contact-email')
]
