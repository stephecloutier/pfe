from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.photos_list, name='photos-list'),

    url(r'^add/$',
        views.photos_image_create, name='photos-image-add'),
    url(r'^(?P<img_pk>[0-9]+)/$',
        views.photos_image_edit, name='photos-image-update'),
    url(r'^(?P<img_pk>[0-9]+)/delete/$',
        views.photos_image_delete, name='photos-image-delete'),
    url(r'^reorder/$',
        views.ajax_reorder_photos_images, name='photos-images-reorder'),
    url(r'^upload/$',
        views.ajax_upload_image, name='photos-images-upload'),
]