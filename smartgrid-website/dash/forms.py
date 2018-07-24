from django import forms
from dash.models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type

class MeanStatistic(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region_consumption']
        widgets = {
            'region_consumption': forms.TextInput(attrs={
            'region_id': 'post-text',
            'required': True,
            'placeholder': 'Say something...'
            })
        }
