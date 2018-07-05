from django.shortcuts import render
from django.template import loader
from django.db.models import Count, Q


from .models import Readings
from .models import Neighborhood

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
    readings_list = Readings.objects.all()
    sum_readings = 0
    for reading in readings_list:
        sum_readings = reading.kWh + sum_readings
    mean_readings = sum_readings/len(readings_list)
    template = loader.get_template('dash/statistics.html')
    context = {'readings_list': readings_list, 'mean_readings': mean_readings, 'sum_readings': sum_readings,}
    return render(request, 'dash/statistics.html', context)

def mean_statistic(request):
    return render(request, 'dash/mean_statistic.html')

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
