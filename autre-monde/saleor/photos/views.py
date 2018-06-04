from django.shortcuts import render
from django.template.response import TemplateResponse

def photos(request):
    return TemplateResponse(request, 'photos/photos.html')