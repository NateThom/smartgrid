from django.db import models

#The reading model is the main model and is made up of some internal
## information and the other models as foreign keys. It represents a
## single reading from some sensor or smart meter.

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

#temperature is an internal field that represents the outdoor temperature
## that was recorded when the reading was taken

#humidity is an internal field that represents the outdoor humidity
## that was recorded when the reading was taken

#wind_speed is an internal field that represents the outdoor wind speed
## that was recorded when the reading was taken

#wind_direction is an internal field that represents the outdoor wind direction
## that was recorded when the reading was taken

#cost is an internal field that represents an estimated price for the reading

#unique_together means that in the database table the combination of the following
## fields must be unique

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)

    year = models.ForeignKey('Year', null=True, on_delete=models.DO_NOTHING)
    month = models.ForeignKey('Month', null=True, on_delete=models.DO_NOTHING)
    day = models.ForeignKey('Day', null=True, on_delete=models.DO_NOTHING)
    hour = models.ForeignKey('Hour', null=True, on_delete=models.DO_NOTHING)

    house_id = models.ForeignKey('House', on_delete=models.CASCADE,)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    consumption = models.BigIntegerField()

    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_direction = models.CharField(max_length=2, blank=True, null=True)

    cost = models.BigIntegerField(null=True, blank=True,)

    class Meta:
        unique_together = ((
        "reading_id",
        "year",
        "month",
        "day",
        "hour",
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

class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=4)

    def __str__(self):
        return str(self.year)

class Month(models.Model):
    month = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.month)

class Day(models.Model):
    day = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.day)

class Hour(models.Model):
    hour = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.hour)
#Region represents the region from which some reading was taken. Region is the
## outermost object in a heirarchy of objects. The objects within a region are:
## Aggregator, Neighborhood, and House

#region_id is the primary key for the Region model and is simply an auto incementing
## integer

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Region(models.Model):
    region_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.region_id)

#Aggregator represents the aggregator from which some reading was taken. Aggregator
## is the second outermost object in a heirarchy of objects. The objects within a
##aggregator are: Neighborhood, and House

#aggregator_id is the primary key for the Aggregator model and is simply an
##auto incementing integer

#region_id is a foreign key from the Region model and is simply an auto incementing
## integer

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Aggregator(models.Model):
    aggregator_id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

    class Meta:
        unique_together = (("aggregator_id", 'region_id'),)

    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id)

#Neighborhood represents the neighborhood from which some reading was taken.
## Aggregator is the third outermost object in a heirarchy of objects. The
## object within a neighborhood is House

#neighborhood_id is the primary key for the Neighborhood model and is simply an
##auto incementing integer

#aggregator_id is a foreign key from the Aggregator model and is simply an
##auto incementing integer

#region_id is a foreign key from the Region model and is simply an auto incementing
## integer

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
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

#House represents the house from which some reading was taken.
## House is the innermost object in a heirarchy of objects.

#house_id is the primary key for the House model and is simply an
##auto incementing integer

#neighborhood_id is a foreign key from the Neighborhood model and is simply an
##auto incementing integer

#aggregator_id is a foreign key from the Aggregator model and is simply an
##auto incementing integer

#region_id is a foreign key from the Region model and is simply an auto incementing
## integer

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
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
