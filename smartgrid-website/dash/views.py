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
    return HttpResponse("You're looking at data statistics.")

def comparisons(request):
    return HttpResponse("You're looking at data comparisons.")
