from django.shortcuts import render
from django.template import loader
from django.db.models import Count, Q

from .models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type

# Create your views here.
def dash(request):
    context = {}
    return render(request, 'dash/dash.html', context)

def dash_statistics_mean(request):
    context = {}
    return render(request, 'dash/dash_statistics_mean.html', context)

def statistics(request):
    mean_items = 0
    template = loader.get_template('dash/statistics.html')
    context = {'mean_items': mean_items,}
    return render(request, 'dash/statistics.html', context)

def mean_statistic(request):
    metric = request.GET['metric']
    data = request.GET['data']
    if((metric == "consumption" and data == "Readings")):
        template = loader.get_template('dash/statistics.html')
        context = {'mean_items': -1, "metric": metric, "data": data,}
        return render(request, 'dash/statistics.html', context)

    if((metric == "kWh" and data != "Readings") or (metric == "outdoor_temp" and data != "Readings")):
        template = loader.get_template('dash/statistics.html')
        context = {'mean_items': -1, "metric": metric, "data": data,}
        return render(request, 'dash/statistics.html', context)

    if(metric == "consumption"):
        metric = data.lower()+"_"+metric

    list = eval(data).objects.all()
    sum_items = 0
    for item in list:
        temp = eval("item"+"."+metric)
        sum_items = temp + sum_items
    mean_items = sum_items/len(list)
    template = loader.get_template('dash/statistics.html')
    context = {'list': list, 'mean_items': mean_items, 'sum_items': sum_items, 'metric': metric, 'data': data,}
    return render(request, 'dash/statistics.html', context)

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

def comparisons(request):
    readings_list = Readings.objects.all()
    num_readings = len(readings_list)
    neighborhoods_greater_25 = Neighborhood.objects.filter(neighborhood_consumption__gt=25)
    neighborhoods_less_25 = Neighborhood.objects.filter(neighborhood_consumption__lte=25)
    num_neighborhoods_greater_25 = len(neighborhoods_greater_25)
    num_neighborhoods_less_25 = len(neighborhoods_less_25)
    template = loader.get_template('dash/comparisons.html')
    context = {'num_readings': num_readings, 'num_neighborhoods_less_25': num_neighborhoods_less_25, 'num_neighborhoods_greater_25': num_neighborhoods_greater_25,}
    return render(request, 'dash/comparisons.html', context)

def number_of_comparison(request):
    data = request.GET['data']
    list = eval(data).objects.all()
    number_of = len(list)
    template = loader.get_template('dash/comparisons.html')
    context = {'number_of': number_of, 'data': data,}
    return render(request, 'dash/comparisons.html', context)
