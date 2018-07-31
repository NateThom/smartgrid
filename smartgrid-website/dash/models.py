from django.db import models

#The reading model is the main model and is made up of some internal
## information and the other models as foreign keys

#reading_id is simply the primary key for Reading. It autoincrements
## and is represented by an integer

#date is a python datetime.datetime object that represents the date
## that the reading was measured

#house_id is a foreign key from the House object that tells us which
## house the reading is from

#neighborhood_id is a foreign key from the Neighborhood object that
## tells us which neighborhood the reading is from

#aggregator_id is a foreign key from the Aggregator object that tells
## us which aggregator the reading is from

#region_id is a foreign key from the Region object that tells us
## which region the reading is from

#consumption is an internal field that represents how much power was
## measured as being consumed between this reading and the previous
## one

#Weather is a foreign key from the Weather object that tells us which
## weather object this reading corresponds to
class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)

    date = models.DateTimeField()

    house_id = models.ForeignKey('House', on_delete=models.CASCADE,)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    consumption = models.BigIntegerField()

    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_direction = models.CharField(max_length=2, blank=True, null=True)

    cost = models.BigIntegerField(null=True, blank=True,)

    class Meta:
        unique_together = ((
        "reading_id",
        "date",
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id",
        "consumption",
        "temperature",
        "humidity",
        "wind_speed",
        "wind_direction",
        "cost"
        ),)

    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id_id)+"////"+str(self.reading_id)

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.region_id)


class Aggregator(models.Model):
    aggregator_id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    class Meta:
        unique_together = (("aggregator_id", 'region_id'),)

    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id)

class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(primary_key=True)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    class Meta:
        unique_together = ((
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)
    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id)

class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    class Meta:
        unique_together = ((
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)
    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id)

class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_direction = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return str(self.temperature)+"/"+str(self.humidity)+"/"+str(self.wind_speed)+"/"+str(self.wind_direction)
# class Appliance(models.Model):
#     appliance_id = models.AutoField(primary_key=True)
#     house_id = models.ForeignKey('House', on_delete=models.CASCADE,)
#     neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
#     aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
#     region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
#     type_id = models.ForeignKey('Appliance_Type', on_delete=models.CASCADE,)
#     appliance_consumption = models.BigIntegerField()
#
#     class Meta:
#         unique_together = ((
#         "appliance_id",
#         "house_id",
#         "neighborhood_id",
#         "aggregator_id",
#         "region_id"
#         ),)
#     def __str__(self):
#         return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id_id)+"////"+str(self.appliance_id)

# class Appliance_Type(models.Model):
#     type_id = models.AutoField(primary_key=True)
#     description = models.TextField()
#     def __str__(self):
#         return str(self.type_id)
