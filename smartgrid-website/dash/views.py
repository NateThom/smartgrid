from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms

from .forms import MeanStatisticForm1, MeanStatisticForm2
from .models import Reading, Region, Aggregator, Neighborhood, House, Year, Month, Day, Hour

#Index View is currently unused
def index(request):
    context = {}
    return render(request, 'dash/index.html', context)

def dash(request):
    context = {}
    return render(request, 'dash/dash.html', context)

def dash_statistics_mean_1(request):
    mean_statistic_form_1 = MeanStatisticForm1()
    mean_items = 0
    context = {'mean_statistic_form_1': mean_statistic_form_1, 'mean_items': mean_items}
    return render(request, 'dash/dash_statistics_mean_1.html', context)

def dash_statistics_mean_2(request):
    mean_statistic_form_1 = MeanStatisticForm1()
    if(len(Reading.objects.all()) == 0):
        messages.warning(request, 'There are no Readings in the database.')
        return redirect('/dash/dash_statistics_mean_1/')

    position_selection = request.GET['position_field']
    measurement_selection = request.GET['measurement_field']
    modifier_selection = request.GET['modifier_field']
    time_period_selection = request.GET['time_period_field']

    if(len(eval(position_selection).objects.all()) == 0):
        messages.warning(request, f'There are no {position_selection} in the database.')
        return redirect('/dash/dash_statistics_mean_1/')

    mean_statistic_form_2 = MeanStatisticForm2(position_selection=position_selection,modifier_selection=modifier_selection,time_period_selection=time_period_selection)
    context = {'position_selection': position_selection, 'measurement_selection': measurement_selection, 'modifier_selection': modifier_selection, 'time_period_selection': time_period_selection, 'mean_statistic_form_2': mean_statistic_form_2}
    return render(request, 'dash/dash_statistics_mean_2.html', context)

def dash_statistics_mean_solution(request):
    form_1_measurement_selection = request.GET['form_1_measurement']
    form_1_position_selection = request.GET['form_1_position']
    form_1_time_period_selection = request.GET['form_1_time_period']
    form_1_modifier_selection = request.GET['form_1_modifier']

    form_2_position_selection = request.GET['position_field']
    form_2_modifier_selection = request.GET['modifier_field']
    form_2_time_period_selection = request.GET['time_period_field']

    if(len(Reading.objects.filter(**{form_1_time_period_selection.lower():form_2_time_period_selection})) == 0):
        messages.warning(request, f'There are no Readings with {form_1_time_period_selection} {form_2_time_period_selection} in the database.')
        return redirect('/dash/dash_statistics_mean_1/')

    mean = 0
    #readings_search_list = Reading.objects.all()
    if(form_1_modifier_selection == "None"):
        position_parameter = form_1_position_selection.lower()+"_id"
        time_period_parameter = form_1_time_period_selection.lower()
        kwargs = {position_parameter:form_2_position_selection, time_period_parameter:form_2_time_period_selection}
        reading_search_list = Reading.objects.filter(**kwargs)

        for item in reading_search_list:
            mean += item.consumption
        mean = mean/len(reading_search_list)
    messages.success(request, f"The mean {form_1_measurement_selection} in {form_1_position_selection} {form_2_position_selection} during {form_1_time_period_selection} {form_2_time_period_selection} is {mean}")
    return redirect('/dash/dash_statistics_mean_1/')

    # reading_list = Reading.objects.filter()
    # return HttpResponse("YAY")

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
