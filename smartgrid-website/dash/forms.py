from django import forms

from .models import Reading, Region, Aggregator, Neighborhood, House, Year, Month, Day, Hour

class MeanStatisticForm1(forms.Form):
    time_frame_choices = [('Year','Year'), ('Month','Month'), ('Day','Day'), ('Hour','Hour')]
    position_choices = [('Region','Region'), ('Aggregator','Aggregator'), ('Neighborhood','Neighborhood'), ('House','House')]
    measurement_choices = [('Consumption','Consumption'), ('Temperature','Temperature'), ('Humidity','Humidity'), ('Wind Direction','Wind Direction'), ('Wind Speed','Wind Speed')]
    modifier_choices = [('Exact Consumption', 'Exact Consumption'), ('Exact Temperature','Exact Temperature'), ('Exact Humidity','Exact Humidity'), ('Exact Wind Direction','Exact Wind Direction'), ('Exact Wind Speed','Exact Wind Speed'), ('None','None')]

    position_field = forms.MultipleChoiceField(choices=position_choices)
    measurement_field = forms.ChoiceField(choices=measurement_choices)
    modifier_field = forms.MultipleChoiceField(choices=modifier_choices)
    time_period_field = forms.ChoiceField(choices=time_frame_choices)

class MeanStatisticForm2(forms.Form):
    position_field = forms.ChoiceField()
    modifier_field = forms.CharField()
    if(modifier_field.max_length == 0):
        fields['modifier_field'].initial = "None"
        fields['modifier_field'].disabled = True
    time_period_field = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
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

# #Returns all of the years currently in database
# def get_year_choices():
#     #create a queryset of single-value tuples. The values are the years
#     ## currently stored in the database
#     TUPLE_LIST = Year.objects.values_list()
#     #Change tuple_list from a queryset to a regular list
#     TUPLE_LIST = list(TUPLE_LIST)
#     #Create an empty list to fill
#     YEAR_CHOICES = []
#     #For every single-value tuple in the tuple_list...
#     for entry in TUPLE_LIST:
#         #add the entry's current single-value to itself making every tuple
#         ## a double-value tuple with two of the same value
#         YEAR_CHOICES.append(entry+entry)
#     #Return the list of double-tuples
#     return YEAR_CHOICES

# class YearModelForm(forms.ModelForm):
#     def get_year_choices():
#         TUPLE_LIST = Year.objects.values_list()
#         TUPLE_LIST = list(TUPLE_LIST)
#         YEAR_CHOICES = []
#         for entry in TUPLE_LIST:
#             YEAR_CHOICES.append(entry+entry)
#         return YEAR_CHOICES
#
#     year_choices = forms.ChoiceField(choices=get_year_choices(), widget=forms.RadioSelect())
#     years = forms.ModelMultipleChoiceField(queryset=Year.objects.all())
#     class Meta:
#         model = Year
#         fields = ['year_choices', 'years']
