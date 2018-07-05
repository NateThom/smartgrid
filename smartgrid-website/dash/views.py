from django.shortcuts import render
from django.template import loader
from django.db.models import Count, Q


from .models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type

# Create your views here.
def index(request):
    largest_readings_list = Readings.objects.order_by('-kWh')[:5]
    template = loader.get_template('dash/index.html')
    context = {'largest_readings_list': largest_readings_list,}
    return render(request, 'dash/index.html', context)

def visualization(request):
    dataset = Readings.objects \
        .values('date_time', 'kWh') \
        .annotate(positive_usage_count=Count('kWh', filter=Q(kWh__gt=0)),
            no_usage_count=Count('kWh', filter=Q(kWh__lte=0))) \
        .order_by('date_time')
    context = {'dataset': dataset,}
    return render(request, 'dash/visualization.html', context)

def statistics(request):
    mean_items = 0
    template = loader.get_template('dash/statistics.html')
    context = {'mean_items': mean_items,}
    return render(request, 'dash/statistics.html', context)

def mean_statistic(request):
    metric = request.GET['metric']
    data = request.GET['data']
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
