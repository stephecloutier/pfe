from pprint import pprint

from django.shortcuts import render
from django.template.response import TemplateResponse

from datetime import datetime

# Create your views here.
def calendar(request, date=datetime.now().strftime("%m-%Y")):
    # Give a format to the date
    # Displays something like: Aug. 27, 2017, 2:57 p.m.
    date = datetime.strptime(date, "%m-%Y")
    formatedDate = date.strftime("%B %Y")

    return TemplateResponse(request, 'events/calendar.html', {
        'date': date,
        'formatedDate': formatedDate
        })
