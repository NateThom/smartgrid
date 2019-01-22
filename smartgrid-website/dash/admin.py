from django.contrib import admin
from .models import Region, Aggregator, Neighborhood, House, Reading

# Register your models here.
admin.site.register(Region)
admin.site.register(Aggregator)
admin.site.register(Neighborhood)
admin.site.register(House)
admin.site.register(Reading)
