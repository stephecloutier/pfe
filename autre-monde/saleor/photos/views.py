from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def photos(request):
    return TemplateResponse(request, 'photos/photos.html')