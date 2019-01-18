from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms

from .forms import LoadDataForm1, MeanStatisticForm1, MeanStatisticForm2
from .models import Data, Reading, Region, Aggregator, Neighborhood, House, Year, Month, Day, Hour

import scipy.io as spio
import os


# All views are function based views. For more information see Django documentation

# The main view for the project. All the other views are called from here.
def dash(request):
    # No context information is passed into the html template.
    context = {}
    # The view returns the request data, the html template that should be used to
    # render the page, and the context data that should be passed into the page
    return render(request, 'dash/dash.html', context)


def dash_load_data1(request):
    # This form is defined in forms.py
    load_data_form1 = LoadDataForm1()
    # The form's data is stored into a variable and then sent to the html template
    # as a context variable
    context = {'load_data_form1': load_data_form1}
    return render(request, 'dash/dash_load_data1.html', context)


def dash_load_data2(request):
    file_path = request.GET['file_path']

    for file_number in range(1, 1153):
        mat = spio.loadmat(f'{file_path}/data{file_number}.mat', squeeze_me=True)

        data_array = mat['dataArray']
        time_data = data_array[0]
        voltage_a_data = data_array[1]
        voltage_b_data = data_array[2]
        voltage_c_data = data_array[3]

        for sample in range(0, len(data_array[0])):
            time = time_data[sample]
            volt_a = voltage_a_data[sample]
            volt_b = voltage_b_data[sample]
            volt_c = voltage_c_data[sample]
            data_instance = Data.objects.create(timestamp=time,
                                                voltage_a=volt_a,
                                                voltage_b=volt_b,
                                                voltage_c=volt_c)

    messages.success(request, "YESSSS!")
    return redirect('/dash/')

    # if(file_path):
    #     messages.success(request, file_path)
    #     return redirect('/dash/')
    # else:
    #     messages.warning(request, 'Unfortunately, there was an error while uploading the data.')
    #     return redirect('/dash/dash_load_data1.html/')


# This view is the first form for the Mean statistic selection. In this form the
# user defines in a broad sense what they are searching for. The user will define
# things like the category of positions that they would like to search for or
# the measurement that they would like to calculate the mean for and so on.
def dash_statistics_mean_1(request):
    # This form is defined in forms.py
    mean_statistic_form_1 = MeanStatisticForm1()
    # The form's data is stored into a variable and then sent to the html template
    # as a context variable
    context = {'mean_statistic_form_1': mean_statistic_form_1}
    return render(request, 'dash/dash_statistics_mean_1.html', context)


# This view is the second form for the mean statistic selection. In this form the
# user will define specific things about their selection. Piggy-backing off of
# the previous example: in the first form the user selects Region and in the
# second form he or she selects which Region.
def dash_statistics_mean_2(request):
    # Check to see if there are readings in the database. If there are none then
    # this will redirect the user to the first form and post a message to the
    # page via the messages block informing the user that there is no data to be
    # worked with.
    if len(Reading.objects.all()) == 0:
        messages.warning(request, 'There are no Readings in the database.')
        return redirect('/dash/dash_statistics_mean_1/')

    # These variables store the data that is found in the url/request from the first form
    position_selection = request.GET['position_field']
    measurement_selection = request.GET['measurement_field']
    time_period_selection = request.GET['time_period_field']

    # If there are no readings from the specified position selection then post a message
    # and redirect to the first page
    if len(eval(position_selection).objects.all()) == 0:
        messages.warning(request, f'There are no {position_selection} in the database.')
        return redirect('/dash/dash_statistics_mean_1/')

    # This form is defined in forms.py
    # We pass the data into the form's function, however we also pass the data
    # to the web page by way of the context. The second part is to be used for
    # anything that uses the data on the page except for forms.
    mean_statistic_form_2 = MeanStatisticForm2(
        position_selection=position_selection,
        time_period_selection=time_period_selection,
        measurement_selection=measurement_selection)

    context = {
        'position_selection': position_selection,
        'measurement_selection': measurement_selection,
        'time_period_selection': time_period_selection,
        'mean_statistic_form_2': mean_statistic_form_2}

    return render(request, 'dash/dash_statistics_mean_2.html', context)


def dash_statistics_mean_solution(request):
    # These variables store the data that is found in the url/request from the first and second forms
    form_1_measurement_selection = request.GET['form_1_measurement']
    form_1_position_selection = request.GET['form_1_position']
    form_1_time_period_selection = request.GET['form_1_time_period']

    form_2_position_selection = request.GET['position_field']
    form_2_time_period_selection = request.GET.getlist('time_period_field')
    form_2_measurement_unit_selection = request.GET['measurement_unit_field']

    # messages.success(request, f"form 2 time period selection: {form_2_time_period_selection}")
    # return redirect('/dash/dash_statistics_mean_1/')

    mean = 0

    # We will use kwargs to pass the parameter variables into django's ORM.
    # For more information on this topic see Django's documentation on making queries
    # For more information on python's kwargs just do a quick Google search for
    # *args and **kwargs
    kwargs = {}

    final_query_set = []

    kwargs[form_1_position_selection.lower()] = form_2_position_selection
    # Create a string that matches a parameter that can be filtered. An example
    # is "year"

    # time_period_parameter = form_1_time_period_selection
    #loop through these for as many items are in the form2_time_period_selection list
    for user_selection in form_2_time_period_selection:

        if form_1_time_period_selection == 'year':
            # year
            kwargs['date__year'] = user_selection

        elif form_1_time_period_selection == 'month':
            # month
            if user_selection[0] == '0':
                kwargs['date__month'] = user_selection[1]
            else:
                kwargs['date__month'] = user_selection[:2]

            # year
            kwargs['date__year'] = user_selection[3:]

        elif form_1_time_period_selection == 'week':
            # week
            if user_selection[0] == '0':
                kwargs['date__week'] = user_selection[1]
            else:
                kwargs['date__week'] = user_selection[:2]

            # year
            kwargs['date__year'] = user_selection[3:]

        elif form_1_time_period_selection == 'day':
            # month
            if user_selection[0] == '0':
                kwargs['date__month'] = user_selection[1]
            else:
                kwargs['date__month'] = user_selection[:2]

            # day
            if user_selection[3] == '0':
                kwargs['date__day'] = user_selection[4]
            else:
                kwargs['date__day'] = user_selection[3:5]

            # year
            kwargs['date__year'] = user_selection[6:]

        elif form_1_time_period_selection == 'hour':
            #hour
            if user_selection[0] == '0':
                kwargs['date__hour'] = user_selection[1]
            else:
                kwargs['date__hour'] = user_selection[:2]

            # month
            if user_selection[6] == '0':
                kwargs['date__month'] = user_selection[7]
            else:
                kwargs['date__month'] = user_selection[6:8]

            # day
            if user_selection[9] == '0':
                kwargs['date__day'] = user_selection[10]
            else:
                kwargs['date__day'] = user_selection[9:11]

            # year
            kwargs['date__year'] = user_selection[12:]

        # The purpose of the reading_search_list is to collect all of the readings
        # in the database that have the matching position and time_period fields
        # to what the user requested.

        reading_search_list = Reading.objects.filter(**kwargs)
        for query in reading_search_list:
            final_query_set.append(query)

    if len(final_query_set) == 0:
        messages.warning(request, f"There are no objects that match your search criteria. Please change the search parameters and try again.")
        return redirect('/dash/dash_statistics_mean_1/')

    # This for loop calculates the mean of all of the readings that matched
    # the search criteria.
    for item in final_query_set:
        # Get current reading's measurement. i.e. Reading.consumption or
        # Reading.temperature
        current_reading_measurement = eval(f'item.{form_1_measurement_selection.lower()}')

        # If the units of the reading are different than the units that the
        # user selects in form 2 then convert the units. For example,
        # reading units are F and user selects C

        if form_2_measurement_unit_selection != eval(f'item.{form_1_measurement_selection.lower()}_units'):
            # Measurement selection is consumption
            if form_1_measurement_selection == 'Consumption':
                # Do nothing because only units are kWh
                current_reading_measurement = current_reading_measurement * 1
            # Measurement selection is temperature
            else:
                # If the reading's units are in Farenheit then convert to C
                if eval(f'item.{form_1_measurement_selection.lower()}_units') == 'F':
                    current_reading_measurement = (current_reading_measurement - 32) / 1.8
                # If the reading's units are in Celcius then convert to F
                else:
                    current_reading_measurement = (current_reading_measurement * 1.8) + 32

        mean += current_reading_measurement
    mean = mean / len(final_query_set)

    # Send a message to Django's messages framework. For more information on how that
    # works checkout the documentation or take a look at this tutorial:
    # https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html
    messages.success(request,
                     f"The mean {form_1_measurement_selection} in {form_2_position_selection} during the {form_1_time_period_selection}: {form_2_time_period_selection} was {mean} {form_2_measurement_unit_selection}")

    # Return the user to the first page of the form. The message will be posted
    # there and the user will be able to make as many other queries as they wish.
    return redirect('/dash/dash_statistics_mean_1/')
