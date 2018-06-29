from django.contrib import admin
from .models import Region, Aggregator, Neighborhood, House, Readings, Appliance, Appliance_Type

# Register your models here.
admin.site.register(Region)
admin.site.register(Aggregator)
admin.site.register(Neighborhood)
admin.site.register(House)
admin.site.register(Readings)
admin.site.register(Appliance)
admin.site.register(Appliance_Type)
