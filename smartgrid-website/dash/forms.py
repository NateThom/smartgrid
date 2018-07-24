from django import forms
from django.forms import ModelForm
from dash.models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type

class MeanStatistic(forms.Form):
    data = forms.ChoiceField(label='Metric', choices=Region.objects.all())

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['region_id', 'region_consumption']
