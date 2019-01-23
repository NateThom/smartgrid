from django import forms

from .models import Reading, Region, Aggregator, Neighborhood, House


class CreateDataForm2(forms.Form):
    # First define the fields that will be in the form. The form will have three
    number_of_regions = forms.IntegerField(min_value=1)
    number_of_aggregators = forms.IntegerField(min_value=1)
    number_of_neighborhoods = forms.IntegerField(min_value=1)
    number_of_houses = forms.IntegerField(min_value=1)

    number_of_readings = forms.IntegerField(min_value=1)
    start_year = forms.IntegerField(min_value=1)
    end_year = forms.IntegerField(min_value=1)
    max_consumption = forms.IntegerField(min_value=1)
    consumption_units = forms.CharField()
    min_temperature = forms.IntegerField()
    max_temperature = forms.IntegerField()
    temperature_units = forms.ChoiceField(choices=[('F', 'F'), ('C', 'C')])
    currency_of_cost = forms.CharField()

    # __init__ is a fucntion that runs before anything else in the class. In C
    # this is like a contructor. Checkout the python docs.
    def __init__(self, *args, **kwargs):
        # First get the data out of the kwargs that were passed into the function
        # when it was called from the views.py
        data_selection = kwargs.pop('data_selection', None)

        super().__init__(*args, **kwargs)

        self.fields['number_of_regions'].initial = 0
        self.fields['number_of_regions'].disabled = True
        self.fields['number_of_aggregators'].initial = 0
        self.fields['number_of_aggregators'].disabled = True
        self.fields['number_of_neighborhoods'].initial = 0
        self.fields['number_of_neighborhoods'].disabled = True
        self.fields['number_of_houses'].initial = 0
        self.fields['number_of_houses'].disabled = True

        self.fields['number_of_readings'].initial = 0
        self.fields['number_of_readings'].disabled = True
        self.fields['start_year'].initial = 0
        self.fields['start_year'].disabled = True
        self.fields['end_year'].initial = 0
        self.fields['end_year'].disabled = True
        self.fields['max_consumption'].initial = 0
        self.fields['max_consumption'].disabled = True
        self.fields['consumption_units'].initial = 'None'
        self.fields['consumption_units'].disabled = True
        self.fields['min_temperature'].initial = 0
        self.fields['min_temperature'].disabled = True
        self.fields['max_temperature'].initial = 0
        self.fields['max_temperature'].disabled = True
        self.fields['temperature_units'].disabled = True
        self.fields['currency_of_cost'].initial = 'None'
        self.fields['currency_of_cost'].disabled = True

        if data_selection:
            for user_selection in data_selection:
                if user_selection == 'Region':
                    self.fields['number_of_regions'].initial = 1
                    self.fields['number_of_regions'].disabled = False
                elif user_selection == 'Aggregator':
                    self.fields['number_of_aggregators'].initial = 1
                    self.fields['number_of_aggregators'].disabled = False
                elif user_selection == 'Neighborhood':
                    self.fields['number_of_neighborhoods'].initial = 1
                    self.fields['number_of_neighborhoods'].disabled = False
                elif user_selection == 'House':
                    self.fields['number_of_houses'].initial = 1
                    self.fields['number_of_houses'].disabled = False
                elif user_selection == 'Reading':
                    self.fields['number_of_readings'].initial = 1
                    self.fields['number_of_readings'].disabled = False
                    self.fields['start_year'].disabled = False
                    self.fields['end_year'].disabled = False
                    self.fields['max_consumption'].disabled = False
                    self.fields['consumption_units'].disabled = False
                    self.fields['consumption_units'].initial = 'kWh'
                    self.fields['min_temperature'].disabled = False
                    self.fields['max_temperature'].disabled = False
                    self.fields['temperature_units'].disabled = False
                    self.fields['currency_of_cost'].disabled = False
                    self.fields['currency_of_cost'].initial = 'USD'


class CreateDataForm1(forms.Form):
    object_choices = [('Region', 'Region'), ('Aggregator', 'Aggregator'), ('Neighborhood', 'Neighborhood'),
                        ('House', 'House'), ('Reading', 'Reading')]

    data_options_field = forms.MultipleChoiceField(choices=object_choices)


class LoadDataForm1(forms.Form):
    file_path = forms.CharField()

# This form is the first part of searching the database for mean values. In this form
# the user will select the data that they want information on, in a broad sense.
# Here the user can say that they want to know the "Mean Regional Consumption
# with no Modifiers over the course of some Time Period"
class StatisticForm1(forms.Form):
    # These lists of two-tuples are hard coded because I could not find a way to
    # automate the process of finding out what tables or models were defined for
    # the database. The cool thing is that it is super easy to change the models
    # that can be searched for or used if need be in the future.

    # Note that the lists must be in the form of two-tuples because that is what
    # the "choices" variable requires. One of the values is the value that will
    # be displayed for the user and the other is the value that will be submitted
    # with the form. See the docs for more information.
    statistics_choices = [('Mean', 'Mean'), ('Standard Deviation', 'Standard Deviation'), ('Minimum', 'Minimum'),
                          ('Maximum', 'Maximum'), ('Range', 'Range'), ('All Statistics', 'All Statistics')]
    time_frame_choices = [('Year', 'Year'), ('Month', 'Month'), ('Week', 'Week'), ('Day', 'Day'), ('Hour', 'Hour')]
    # Maybe include later ('day_of_week', 'Day Of Week'), ('season', 'Season'),
    position_choices = [('Region', 'Region'), ('Aggregator', 'Aggregator'), ('Neighborhood', 'Neighborhood'),
                        ('House', 'House')]
    measurement_choices = [('Consumption', 'Consumption'), ('Temperature', 'Temperature')]

    # The django library makes it super easy to render these fields with built-in functions.
    # There are many different "widget" options available and they could be cusotmized too.
    # That being said, I though that these looked good for out-of-the-box options.

    # This may be obvious, but the MultipleChoiceField allows for multiple selections
    # to be submitted with the query and the ChoiceField allows for only one
    statistic_field = forms.ChoiceField(choices=statistics_choices)
    position_field = forms.MultipleChoiceField(choices=position_choices)
    measurement_field = forms.ChoiceField(choices=measurement_choices)
    time_period_field = forms.ChoiceField(choices=time_frame_choices)


# This form is used as the second form in the process of making a mean query. In this
# form the user will specify the information that they already chose in the first
# form. Here's an example. In form 1 the user selected Region, Consumption,
# Exact Temperature, and Year. Then in form 2 the user will specify which region,
# the value of the modifier, and which year that the mean should be calculated for.
class StatisticForm2(forms.Form):
    # First define the fields that will be in the form. The form will have three
    # fields: position, modifier, and time_period
    position_field = forms.ChoiceField()
    time_period_field = forms.MultipleChoiceField()
    measurement_unit_field = forms.ChoiceField()

    # __init__ is a fucntion that runs before anything else in the class. In C
    # this is like a contructor. Checkout the python docs.
    def __init__(self, *args, **kwargs):
        def get_region_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            return TUPLE_LIST

        def get_aggregator_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[2],)
                CHOICES.append(tpl + tpl)
            return CHOICES

        def get_neighborhood_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[3],)
                CHOICES.append(tpl + tpl)
            return CHOICES

        def get_house_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[4],)
                CHOICES.append(tpl + tpl)
            return CHOICES

        def get_time_period_choices(selection):
            if selection == 'Year':
                year_list = list(Reading.objects.datetimes('date', 'year', 'ASC'))
                choices = []
                for year in range(len(year_list)):
                    choices.append((year_list[year].strftime('%Y'), year_list[year].strftime('%Y')))

                return choices

            # elif selection == 'season':

            elif selection == 'Month':
                month_list = list(Reading.objects.datetimes('date', 'month', 'ASC'))
                choices = []
                for month in range(len(month_list)):
                    choices.append((month_list[month].strftime('%m/%Y'), month_list[month].strftime('%m/%Y')))

                return choices

            elif selection == 'Week':
                week_list = list(Reading.objects.datetimes('date', 'week', 'ASC'))
                choices = []
                for week in range(len(week_list)):
                    choices.append((week_list[week].strftime('%V/%Y'), week_list[week].strftime('%V/%Y')))

                return choices

            elif selection == 'Day':
                day_list = list(Reading.objects.datetimes('date', 'day', 'ASC'))
                choices = []
                for day in range(len(day_list)):
                    choices.append((day_list[day].strftime('%m/%d/%Y'), day_list[day].strftime('%m/%d/%Y')))

                return choices

            # elif selection == 'day_of_week':

            elif selection == 'Hour':
                hour_list = list(Reading.objects.datetimes('date', 'hour', 'ASC'))
                choices = []
                for hour in range(len(hour_list)):
                    choices.append((hour_list[hour].strftime('%R %m/%d/%Y'), hour_list[hour].strftime('%R %m/%d/%Y')))

                return choices

        def get_measurement_unit_choices(selection):
            if selection == "Consumption":
                CHOICES = [('kWh', 'kWh')]
            else:
                CHOICES = [('F', 'Fahrenheit'), ('C', 'Celsius')]

            return CHOICES

        # First get the data out of the kwargs that were passed into the function
        # when it was called from the views.py
        position_selection = kwargs.pop('position_selection', None)
        time_period_selection = kwargs.pop('time_period_selection', None)
        measurement_selection = kwargs.pop('measurement_selection', None)

        super().__init__(*args, **kwargs)

        if position_selection:
            if position_selection == "Region":
                self.fields['position_field'].choices = get_region_choices(position_selection)
            elif position_selection == "Aggregator":
                self.fields['position_field'].choices = get_aggregator_choices(position_selection)
            elif position_selection == "Neighborhood":
                self.fields['position_field'].choices = get_neighborhood_choices(position_selection)
            else:
                self.fields['position_field'].choices = get_house_choices(position_selection)

        if time_period_selection:
            self.fields['time_period_field'].choices = get_time_period_choices(time_period_selection)

        if measurement_selection:
            self.fields['measurement_unit_field'].choices = get_measurement_unit_choices(measurement_selection)
