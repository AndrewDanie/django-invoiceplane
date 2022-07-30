from django.db.models import Count
from django.shortcuts import render
from .models import *
import datetime


def main_page(request):

    user_dashboards = Dashboard_set.objects.all()
    dash_types = []
    for dashboard in user_dashboards:
        dash_types.append(dashboard.name)

    data = {}
    data['carset'] = Vehicle.objects.all()
    data['last_year'] = Vehicle.objects.filter(sale_date__gte=datetime.date(2022, 1, 1)).order_by('sale_date')
    names = [f.verbose_name.title() for f in Vehicle._meta.get_fields()][1:]
    data['income'] = Vehicle.objects.values('sale_date', 'price').order_by('sale_date')

    return render(request, 'djangoinvoicelike/index.html',
                  {'data': data,
                   'names': names,
                   'dash_types': dash_types}
                  )