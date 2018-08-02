from django.contrib import admin
from .models import Region, Aggregator, Neighborhood, House, Reading, Year, Month, Day, Hour

# Register your models here.
admin.site.register(Region)
admin.site.register(Aggregator)
admin.site.register(Neighborhood)
admin.site.register(House)
admin.site.register(Reading)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Hour)
