from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from .forms import YearModelForm
from .models import Reading, Region, Aggregator, Neighborhood, House, Year, Month, Day, Hour

#Index View is currently unused
def index(request):
    context = {}
    return render(request, 'dash/index.html', context)

def dash(request):
    form = YearModelForm()
    context = {'form':form}
    return render(request, 'dash/dash.html', context)

def dash_statistics_mean_1(request):
    form = YearModelForm()
    mean_items = 0
    context = {'mean_items': mean_items}
    return render(request, 'dash/dash_statistics_mean.html', context)

def mean_statistic(request):
    if("time" in request.GET):
        time = request.GET['time']
    else:
        time = "no_input"
    if("metric" in request.GET):
        metric = request.GET['metric']
    else:
        metric = "no_input"
    if("data" in request.GET):
        data = request.GET['data']
    else:
        data = "no_input"

    if(time == "no_input" and metric == "no_input" and data == "no_input"):
        context = {'message': "No user input submitted.", 'time': time, 'metric': metric, 'data': data,}
        return render(request, 'dash/dash_statistics_mean.html', context)
