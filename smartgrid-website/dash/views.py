from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import loader


from .models import Readings

# Create your views here.
def index(request):
    largest_readings_list = Readings.objects.order_by('-kWh')[:5]
    template = loader.get_template('dash/index.html')
    context = {'largest_readings_list': largest_readings_list,}
    return render(request, 'dash/index.html', context)

def visualization(request):
    template = loader.get_template('dash/visualization.html')
    return render(request, 'dash/visualization.html')

def statistics(request):
    readings_list = Readings.objects.all()
    sum_readings = 0
    for reading in readings_list:
        sum_readings = reading.kWh + sum_readings
    mean_readings = sum_readings/len(readings_list)
    template = loader.get_template('dash/statistics.html')
    context = {'mean_readings': mean_readings, 'sum_readings': sum_readings,}
    return render(request, 'dash/statistics.html', context)

def comparisons(request):
    return HttpResponse("You're looking at data comparisons.")
