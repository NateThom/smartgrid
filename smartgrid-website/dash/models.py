from django.db import models
from django.utils import timezone


class Data(models.Model):
    data = models.AutoField(primary_key=True)

    timestamp = models.FloatField()

    voltage_a = models.FloatField()
    voltage_a_units = models.CharField(max_length=3, default='kWh')

    voltage_b = models.FloatField()
    voltage_b_units = models.CharField(max_length=3, default='kWh')

    voltage_c = models.FloatField()
    voltage_c_units = models.CharField(max_length=3, default='kWh')

    class Meta:
        unique_together = (
            "data",
            "timestamp",
            "voltage_a",
            "voltage_a_units",
            "voltage_b",
            "voltage_b_units",
            "voltage_c",
            "voltage_c_units"
        )

    def __str__(self):
        return str(self.data)


# The reading model is the main model and is made up of some internal
# information and the other models as foreign keys. It represents a
# single reading from some sensor or smart meter.

# reading is simply the primary key for Reading. It autoincrements
# and is represented by an integer

# the time that each reading was recorded is represented by a corresponding year,
# month, day, and hour field. In the future I would like to change these fields
# so that they inherit from one another much like the postion (Region, Aggregator, etc)
# fields do now. All of the dates are foreign keys from individual tables

# house is a foreign key from the House object that tells us which
# house the reading is from

# neighborhood is a foreign key from the Neighborhood object that
# tells us which neighborhood the reading is from

# aggregator is a foreign key from the Aggregator object that tells
# us which aggregator the reading is from

# region is a foreign key from the Region object that tells us
# which region the reading is from

# consumption is an internal field that represents how much power was
# measured as being consumed between this reading and the previous
# one

# temperature is an internal field that represents the outdoor temperature
# that was recorded when the reading was taken

# humidity is an internal field that represents the outdoor humidity
# that was recorded when the reading was taken

# wind_speed is an internal field that represents the outdoor wind speed
# that was recorded when the reading was taken

# wind_direction is an internal field that represents the outdoor wind direction
# that was recorded when the reading was taken

# cost is an internal field that represents an estimated price for the reading

# unique_together means that in the database table the combination of the following
# fields must be unique

# __str__(self) gives the model a name in the django api. The name is a string
# made up of the fields in the return statement
class Reading(models.Model):
    reading = models.AutoField(primary_key=True)

    house = models.ForeignKey('House', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)
    aggregator = models.ForeignKey('Aggregator', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    # year = models.CharField(max_length=4, default="2018", null=True)
    # month = models.CharField(max_length=2, default="01", null=True)
    # day = models.CharField(max_length=2, default="01", null=True)
    # hour = models.CharField(max_length=2, default="00", null=True)
    # minute = models.CharField(max_length=2, default="00", null=True)
    # second = models.CharField(max_length=2, default="00", null=True)

    date = models.DateTimeField(default=timezone.now)

    consumption = models.BigIntegerField(default=0)
    consumption_units = models.CharField(max_length=3, default='kWh')

    temperature = models.IntegerField(default=0)
    temperature_units = models.CharField(max_length=1, default='F')

    cost = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=3, default="USD")

    class Meta:
        unique_together = ("reading",
                           # "year",
                           # "month",
                           # "day",
                           # "hour",
                           # "minute",
                           # "second",
                           "date",
                           "house",
                           "neighborhood",
                           "aggregator",
                           "region",
                           "consumption",
                           "temperature",
                           "cost")

    def __str__(self):
        return str(self.region_id) + "/" + str(self.aggregator_id) + "/" + str(self.neighborhood_id) + "/" + str(
            self.house_id) + "/" + str(self.reading)

# Region represents the region from which some reading was taken. Region is the
# outermost object in a heirarchy of objects. The objects within a region are:
# Aggregator, Neighborhood, and House

# region is the primary key for the Region model and is simply an auto incementing
# integer

# __str__(self) gives the model a name in the django api. The name is a string
# made up of the fields in the return statement
class Region(models.Model):
    region = models.CharField(max_length=25)
    full_name = models.CharField(max_length=25, primary_key=True, default="full_name", )

    def __str__(self):
        return self.region

    def save(self):
        self.full_name = self.region
        super(Region, self).save()


# Aggregator represents the aggregator from which some reading was taken. Aggregator
# is the second outermost object in a heirarchy of objects. The objects within a
#aggregator are: Neighborhood, and House

# aggregator is the primary key for the Aggregator model and is simply an
#auto incementing integer

# region is a foreign key from the Region model and is simply an auto incementing
# integer

# __str__(self) gives the model a name in the django api. The name is a string
# made up of the fields in the return statement
class Aggregator(models.Model):
    aggregator = models.CharField(max_length=25)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=51, primary_key=True, default="full_name")

    class Meta:
        unique_together = (("aggregator", 'region'),)

    def __str__(self):
        return self.region_id + "/" + self.aggregator

    def save(self):
        self.full_name = self.region_id + "/" + self.aggregator
        super(Aggregator, self).save()


# Neighborhood represents the neighborhood from which some reading was taken.
# Aggregator is the third outermost object in a heirarchy of objects. The
# object within a neighborhood is House

# neighborhood is the primary key for the Neighborhood model and is simply an
# auto incementing integer

# aggregator is a foreign key from the Aggregator model and is simply an
# auto incementing integer

# region is a foreign key from the Region model and is simply an auto incementing
# integer

# __str__(self) gives the model a name in the django api. The name is a string
# made up of the fields in the return statement
class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=25)
    aggregator = models.ForeignKey('Aggregator', on_delete=models.CASCADE, )
    region = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=78, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
                               "neighborhood",
                               "aggregator",
                               "region"
                           ),)

    def __str__(self):
        return self.aggregator_id + "/" + self.neighborhood

    def save(self):
        self.full_name = self.aggregator_id + "/" + self.neighborhood
        super(Neighborhood, self).save()


# House represents the house from which some reading was taken.
# House is the innermost object in a heirarchy of objects.

# house is the primary key for the House model and is simply an
# auto incementing integer

# neighborhood is a foreign key from the Neighborhood model and is simply an
# auto incementing integer

# aggregator is a foreign key from the Aggregator model and is simply an
# auto incementing integer

# region_id is a foreign key from the Region model and is simply an auto incementing
# integer

# __str__(self) gives the model a name in the django api. The name is a string
# made up of the fields in the return statement
class House(models.Model):
    house = models.CharField(max_length=25)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, )
    aggregator = models.ForeignKey('Aggregator', on_delete=models.CASCADE, )
    region = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=106, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
                               "house",
                               "neighborhood",
                               "aggregator",
                               "region"
                           ),)

    def __str__(self):
        return self.neighborhood_id + "/" + self.house

    def save(self):
        self.full_name = self.neighborhood_id + "/" + self.house
        super(House, self).save()

# class Appliance(models.Model):
#     appliance = models.AutoField(primary_key=True)
#     house = models.ForeignKey('House', on_delete=models.CASCADE,)
#     neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
#     aggregator = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
#     region = models.ForeignKey('Region', on_delete=models.CASCADE,)
#     type = models.ForeignKey('Appliance_Type', on_delete=models.CASCADE,)
#     appliance_consumption = models.BigIntegerField()
#
#     class Meta:
#         unique_together = ((
#         "appliance",
#         "house",
#         "neighborhood",
#         "aggregator",
#         "region"
#         ),)
#     def __str__(self):
#         return str(self.region_id)+"/"+str(self.aggregator_id)+"//"+str(self.neighborhood_id)+"///"+str(self.house_id)+"////"+str(self.appliance)

# class Appliance_Type(models.Model):
#     type = models.AutoField(primary_key=True)
#     description = models.TextField()
#     def __str__(self):
#         return str(self.type)
