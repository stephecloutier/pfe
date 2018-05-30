from pprint import pprint

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.models import AnonymousUser

from datetime import datetime, date, timedelta

from ..product.utils import products_visible_to_user

# Create your views here.
def calendar(request, date=datetime.now().strftime("%m-%Y")):
    user = AnonymousUser()
    release_days = []

    # Give a format to the date
    # Displays something like: Aug. 27, 2017, 2:57 p.m.
    date = datetime.strptime(date, "%m-%Y")
    formated_date = date.strftime("%B %Y")
    next_month = add_one_month(date).strftime("%m-%Y")
    previous_month = subtract_one_month(date).strftime("%m-%Y")

    products = products_visible_to_user(user).filter(release_date__month=date.month, release_date__year=date.year).order_by('release_date')
    if len(products):
        release_days = [{"products": [products[0]], "formated_day": products[0].release_date.strftime("%A %d %B").lstrip("0").replace(" 0", " ")}]
    i = 0
    for index, product in enumerate(products[1:]):
        pprint(release_days[i]["products"])
        if release_days[i]["products"][0].release_date != product.release_date:
            release_days.append({"products": [product], "formated_day": product.release_date.strftime("%A %d %B").lstrip("0").replace(" 0", " ")})
            i += 1
        else:
            release_days[i]["products"].append(product)
        
    # for index, release_day in enumerate(release_days):
    #     release_days[index] = release_day.strftime("%A %m %B").lstrip("0").replace(" 0", " ")



    return TemplateResponse(request, 'events/calendar.html', {
        'date': date,
        'formated_date': formated_date,
        'release_days': release_days,
        'previous_month': previous_month,
        'next_month': next_month
        })

def add_one_month(date):
    date = date.replace(day=1)
    date = date + timedelta(days=32)
    date = date.replace(day=1)
    return date

def subtract_one_month(date):
    date = date.replace(day=1)
    date = date - timedelta(days=1)
    date = date.replace(day=1)
    return date