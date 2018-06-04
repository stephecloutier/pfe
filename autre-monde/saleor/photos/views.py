from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Photo

from pprint import pprint

def photos(request):
    images = Photo.objects.all()
    return TemplateResponse(request, 'photos/photos.html', {'images' : images})
