from django.shortcuts import HttpResponse
from django.template import loader

from .models import Readings

# Create your views here.
def index(request):
    latest_readings_list = Readings.objects.order_by('-kWh')[:5]
    template = loader.get_template('dash/index.html')
    context = {
        'latest_readings_list': latest_readings_list,
    }
    return HttpResponse(template.render(context, request))

def visualization(request):
    return HttpResponse("You're looking at data vizualizations.")

def statistics(request):
    return HttpResponse("You're looking at data statistics.")

def comparisons(request):
    return HttpResponse("You're looking at data comparisons.")
