import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Count, Q

from .models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type
from .forms import MeanStatistic

# Create your views here.
def dash(request):
    context = {}
    return render(request, 'dash/dash.html', context)

def dash_statistics_mean(request):
    mean_items = 0
    context = {'mean_items': mean_items}
    return render(request, 'dash/dash_statistics_mean.html', context)

def mean_statistic(request):
    metric = request.GET['metric']
    data = request.GET['data']
    if((metric == "consumption" and data == "Readings")):
        #template = loader.get_template('dash/dash_statistics_mean.html')
        context = {'mean_items': -1, "metric": metric, "data": data,}
        return render(request, 'dash/dash_statistics_mean.html', context)

    if((metric == "kWh" and data != "Readings") or (metric == "outdoor_temp" and data != "Readings")):
        #template = loader.get_template('dash/dash_statistics_mean.html')
        context = {'mean_items': -1, "metric": metric, "data": data,}
        return render(request, 'dash/dash_statistics_mean.html', context)

    if(metric == "consumption"):
        metric = data.lower()+"_"+metric

    list = eval(data).objects.all()
    sum_items = 0
    for item in list:
        temp = eval("item"+"."+metric)
        sum_items = temp + sum_items
    mean_items = sum_items/len(list)
    #template = loader.get_template('dash/dash_statistics_mean.html')
    context = {'list': list, 'mean_items': mean_items, 'sum_items': sum_items, 'metric': metric, 'data': data,}
    return render(request, 'dash/dash_statistics_mean.html', context)

def visualization(request):
    house_dataset = House.objects \
        .values('house_consumption', 'house_id') \
        .order_by('house_id')
    region_dataset = Region.objects \
        .values('region_consumption', 'region_id') \
        .order_by('region_id')
    len_house_dataset = []
    for house in range(1, len(house_dataset)):
        len_house_dataset.append(house)
    context = {'house_dataset': house_dataset, 'region_dataset': region_dataset, 'len_house_dataset': len_house_dataset,}
    return render(request, 'dash/visualization.html', context)
