from django.db.models import Count, Sum
from django.db.models.functions import TruncYear, TruncMonth
from django.shortcuts import render
from .models import *
import datetime
from .toPDF import render_to_pdf

from plotly.offline import plot
from plotly.graph_objs import Scatter


def main_page(request):
    user_dashboards = Dashboard_set.objects.all()
    carset = Vehicle.objects.all()

    last_year = carset.filter(sale_date__gte=datetime.date(2022, 1, 1)).order_by('sale_date')
    income = carset.values(year=TruncYear('sale_date')).annotate(Sum('price')).order_by('year')
    car_amount_by_brand = carset.values('brand').annotate(Count('id'))

    sold_cars_month = Vehicle.objects.\
                    values(month=TruncMonth('sale_date')).\
                    annotate(Count('id')).\
                    order_by('month')
    plot_sold_cars = plot([Scatter(x=[month['month'] for month in sold_cars_month],
                                   y=[month['id__count'] for month in sold_cars_month],
                            mode='markers+lines',
                            marker=dict(color='LightSkyBlue', size=12, line=dict(color='MediumPurple', width=2)),
                            name='test',
                            opacity=0.9
                         )],
                        output_type='div')

    kia_delivery = Vehicle.objects\
                    .values(year=TruncYear('delivery_date'))\
                    .annotate(Count('id'))\
                    .order_by('year')
    plot_kia = plot([Scatter(x=[car['year'] for car in kia_delivery],
                             y=[car['id__count'] for car in kia_delivery],
                       mode='markers+lines',
                       marker=dict(color='LightSkyBlue', size=12, line=dict(color='MediumPurple', width=2)),
                       name='test',
                       opacity=0.9,
                    )],
                    output_type='div')

    names = [f.verbose_name.title() for f in Vehicle._meta.get_fields()][1:]

    context = {'carset': carset,
                   'income': income,
                   'last_year': last_year,
                   'car_amount_by_brand': car_amount_by_brand,
                   'names': names,
                   'dash_types': user_dashboards,
                   'plot_sold_cars': plot_sold_cars,
                   'plot_kia': plot_kia,
                }

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

        # if request.POST.get("to-pdf-dash-button"):
        #     dash_type = request.POST['to-pdf-dash-button']
        #     print(f'Конвертируем в pdf {dash_type}')
        #     context['dash_type'] = dash_type
        #     return render_to_pdf(context)

    return render(request, 'djangoinvoicelike/index.html', context=context)