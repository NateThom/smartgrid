from django import forms

from .models import Year

class YearModelForm(forms.ModelForm):
    def get_year_choices():
        TUPLE_LIST = Year.objects.values_list()
        TUPLE_LIST = list(TUPLE_LIST)
        YEAR_CHOICES = []
        for entry in TUPLE_LIST:
            YEAR_CHOICES.append(entry+entry)
        return YEAR_CHOICES

    year_choices = forms.ChoiceField(choices=get_year_choices(), widget=forms.RadioSelect())
    years = forms.ModelMultipleChoiceField(queryset=Year.objects.all())
    class Meta:
        model = Year
        fields = ['year_choices', 'years']
