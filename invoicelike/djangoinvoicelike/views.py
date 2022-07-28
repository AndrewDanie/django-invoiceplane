from django.shortcuts import render
from .models import *


def main_page(request):
    user_tables = []
    cars = Vehicle.objects.all()
    user_tables.append(cars)
    names = [f.verbose_name.title() for f in Vehicle._meta.get_fields()][1:]
    return  render(request, 'djangoinvoicelike/index.html', {'user_tables': user_tables, 'names': names})