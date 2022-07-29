from django.shortcuts import render
from .models import *


def main_page(request):

    user_dashboards = Dashboard_set.objects.all()
    dash_types = []
    for dashboard in user_dashboards:
        dash_types.append(dashboard.name)
    print(dash_types)

    carset = Vehicle.objects.all()
    names = [f.verbose_name.title() for f in Vehicle._meta.get_fields()][1:]
    return render(request, 'djangoinvoicelike/index.html',
                  {'carset': carset,
                   'names': names,
                   'dash_types': dash_types}
                  )