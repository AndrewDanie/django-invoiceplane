from django.db.models import Count
from django.shortcuts import render
from .models import *
import datetime

from plotly.offline import plot
from plotly.graph_objs import Scatter



def main_page(request):
    if request.method == 'POST':
        if request.POST.get("del-dash-button"):
            pk = request.POST['del-dash-button']
            try:
                dash_to_delete = Dashboard_set.objects.get(pk=pk)
                print(dash_to_delete)
                dash_to_delete.delete()
            except:
                pass

        if request.POST.get("new-dash-button"):
            dash_name = request.POST['new-dash-button']
            new_dash = Dashboard_set(name=dash_name)
            new_dash.save()
            print('Создать', new_dash)

    user_dashboards = Dashboard_set.objects.all()

    data = {}
    data['carset'] = Vehicle.objects.all()
    data['last_year'] = Vehicle.objects.filter(sale_date__gte=datetime.date(2022, 1, 1)).order_by('sale_date')
    names = [f.verbose_name.title() for f in Vehicle._meta.get_fields()][1:]
    data['income'] = Vehicle.objects.values('sale_date', 'price').order_by('sale_date')

    x_data = [0, 1, 2, 3]
    y_data = [x ** 2 for x in x_data]
    plot_sold_cars = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.9, marker_color='green')],
                    output_type='div')

    plot_kia = plot([Scatter(x=x_data, y=y_data,
                                   mode='lines', name='test',
                                   opacity=0.9, marker_color='green')],
                          output_type='div')

    return render(request, 'djangoinvoicelike/index.html',
                  {'data': data,
                   'names': names,
                   'dash_types': user_dashboards,
                   'plot_sold_cars': plot_sold_cars,
                   'plot_kia': plot_kia,
                })