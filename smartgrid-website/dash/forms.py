from django import forms

from .models import Reading, Region, Aggregator, Neighborhood, House, Year, Month, Day, Hour

#This form is the first part of searching the database for mean values. In this form
## the user will select the data that they want information on, in a broad sense.
## Here the user can say that they want to know the "Mean Regional Consumption
## with no Modifiers over the course of some Time Period"
class MeanStatisticForm1(forms.Form):
    #These lists of two-tuples are hard coded because I could not find a way to
    ## automate the process of finding out what tables or models were defined for
    ## the database. The cool thing is that it is super easy to change the models
    ## that can be searched for or used if need be in the future.

    #Note that the lists must be in the form of two-tuples because that is what
    ## the "choices" variable requires. One of the values is the value that will
    ## be displayed for the user and the other is the value that will be submitted
    ## with the form. See the docs for more information.
    time_frame_choices = [('Year','Year'), ('Month','Month'), ('Day','Day'), ('Hour','Hour')]
    position_choices = [('Region','Region'), ('Aggregator','Aggregator'), ('Neighborhood','Neighborhood'), ('House','House')]
    measurement_choices = [('Consumption','Consumption'), ('Temperature','Temperature'), ('Humidity','Humidity'), ('Wind Direction','Wind Direction'), ('Wind Speed','Wind Speed')]
    modifier_choices = [('Exact Consumption', 'Exact Consumption'), ('Exact Temperature','Exact Temperature'), ('Exact Humidity','Exact Humidity'), ('Exact Wind Direction','Exact Wind Direction'), ('Exact Wind Speed','Exact Wind Speed'), ('None','None')]

    #The django library makes it super easy to render these fields with built-in functions.
    ## There are many different "widget" options available and they could be cusotmized too.
    ## That being said, I though that these looked good for out-of-the-box options.

    #This may be obvious, but the MultipleChoiceField allows for multiple selections
    ## to be submitted with the query and the ChoiceField allows for only one
    position_field = forms.MultipleChoiceField(choices=position_choices)
    measurement_field = forms.ChoiceField(choices=measurement_choices)
    modifier_field = forms.MultipleChoiceField(choices=modifier_choices)
    time_period_field = forms.ChoiceField(choices=time_frame_choices)

#This form is used as the second form in the process of making a mean query. In this
## form the user will specify the information that they already chose in the first
## form. Here's an example. In form 1 the user selected Region, Consumption,
## Exact Temperature, and Year. Then in form 2 the user will specify which region,
## the value of the modifier, and which year that the mean should be calculated for.
class MeanStatisticForm2(forms.Form):
    #First define the fields that will be in the form. The form will have three
    ## fields: position, modifier, and time_period
    position_field = forms.ChoiceField()
    modifier_field = forms.CharField()
    if(modifier_field.max_length == 0):
        fields['modifier_field'].initial = "None"
        fields['modifier_field'].disabled = True
    time_period_field = forms.ChoiceField()

    #__init__ is a fucntion that runs before anything else in the class. In C
    ## this is like a contructor. Checkout the python docs.
    def __init__(self, *args, **kwargs):
        #First get the data out of the kwargs that were passed into the function
        ## when it was called from the views.py
        position_selection = kwargs.pop('position_selection', None)
        modifier_selection = kwargs.pop('modifier_selection', None)
        time_period_selection = kwargs.pop('time_period_selection', None)
        super().__init__(*args, **kwargs)

        def get_region_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            return TUPLE_LIST

        def get_aggregator_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[2],)
                CHOICES.append(tpl+tpl)
            return CHOICES

        def get_neighborhood_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[3],)
                CHOICES.append(tpl+tpl)
            return CHOICES

        def get_house_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                tpl = (entry[4],)
                CHOICES.append(tpl+tpl)
            return CHOICES

        def get_time_period_choices(selection):
            TUPLE_LIST = list(eval(selection).objects.values_list())
            CHOICES = []
            for entry in TUPLE_LIST:
                CHOICES.append(entry+entry)
            return CHOICES

        def get_modifier_length(selection):
            if(selection[0:5] == "Exact"):
                if(selection[6:] == "Consumption"):
                    return 16
                elif(selection[6:] == "Temperature"):
                    return 3
                elif(selection[6:] == "Humidity"):
                    return 3
                elif(selection[6:] == "Wind Direction"):
                    return 2
                elif(selection[6:] == "Wind Speed"):
                    return 3
            else:
                return 0

        if position_selection:
            if(position_selection == "Region"):
                self.fields['position_field'].choices=get_region_choices(position_selection)
            elif(position_selection == "Aggregator"):
                self.fields['position_field'].choices=get_aggregator_choices(position_selection)
            elif(position_selection == "Neighborhood"):
                self.fields['position_field'].choices=get_neighborhood_choices(position_selection)
            else:
                self.fields['position_field'].choices=get_house_choices(position_selection)
        if modifier_selection:
            self.fields['modifier_field'].max_length=get_modifier_length(modifier_selection)
        if time_period_selection:
            self.fields['time_period_field'].choices=get_time_period_choices(time_period_selection)
