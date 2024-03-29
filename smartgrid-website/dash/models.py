from django.db import models


class PowerSystemReading(models.Model):
    id = models.AutoField(primary_key=True)

    house = models.IntegerField()
    neighborhood = models.IntegerField()
    aggregator = models.IntegerField()
    region = models.IntegerField()

    year = models.CharField(max_length=4, default="2018")
    season = models.CharField(max_length=6, default="Winter")
    week = models.CharField(max_length=2, default="01")
    day = models.CharField(max_length=9, default="Monday")
    hour = models.CharField(max_length=2, default="00")

    power_system = models.CharField(max_length=5, default="1")
    load_feeder = models.CharField(max_length=5, default="1")

    weekly_peak_load_percentage = models.FloatField()
    daily_peak_load_percentage = models.FloatField()
    hourly_peak_load_percentage = models.FloatField()

    active_power = models.IntegerField()
    reactive_power = models.IntegerField()
    apparent_power = models.IntegerField()

    class Meta:
        unique_together = (
            "id",

            "year",
            "season",
            "week",
            "day",
            "hour",

            "house",
            "neighborhood",
            "aggregator",
            "region",

            "power_system",
            "load_feeder",

            "active_power",
            "reactive_power",
            "apparent_power"
        )

    def __str__(self):
        return str(self.id)


class Data(models.Model):
    data_id = models.AutoField(primary_key=True)

    timestamp = models.FloatField()

    voltage_a = models.FloatField()
    voltage_a_units = models.CharField(max_length=3, default='kWh')

    voltage_b = models.FloatField()
    voltage_b_units = models.CharField(max_length=3, default='kWh')

    voltage_c = models.FloatField()
    voltage_c_units = models.CharField(max_length=3, default='kWh')

    class Meta:
        unique_together = ((
                               "data_id",
                               "timestamp",
                               "voltage_a",
                               "voltage_a_units",
                               "voltage_b",
                               "voltage_b_units",
                               "voltage_c",
                               "voltage_c_units"),)

    def __str__(self):
        return str(self.data_id)


# The reading model is the main model and is made up of some internal
## information and the other models as foreign keys. It represents a
## single reading from some sensor or smart meter.

# reading_id is simply the primary key for Reading. It autoincrements
## and is represented by an integer

# the time that each reading was recorded is represented by a corresponding year,
## month, day, and hour field. In the future I would like to change these fields
## so that they inherit from one another much like the postion (Region, Aggregator, etc)
## fields do now. All of the dates are foreign keys from individual tables

# house_id is a foreign key from the House object that tells us which
## house the reading is from

# neighborhood_id is a foreign key from the Neighborhood object that
## tells us which neighborhood the reading is from

# aggregator_id is a foreign key from the Aggregator object that tells
## us which aggregator the reading is from

# region_id is a foreign key from the Region object that tells us
## which region the reading is from

# consumption is an internal field that represents how much power was
## measured as being consumed between this reading and the previous
## one

# temperature is an internal field that represents the outdoor temperature
## that was recorded when the reading was taken

# humidity is an internal field that represents the outdoor humidity
## that was recorded when the reading was taken

# wind_speed is an internal field that represents the outdoor wind speed
## that was recorded when the reading was taken

# wind_direction is an internal field that represents the outdoor wind direction
## that was recorded when the reading was taken

# cost is an internal field that represents an estimated price for the reading

# unique_together means that in the database table the combination of the following
## fields must be unique

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)

    house_id = models.ForeignKey('House', on_delete=models.CASCADE, null=True, )
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, null=True, )
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE, null=True, )
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, )

    year = models.CharField(max_length=4, default="2018", null=True)
    month = models.CharField(max_length=2, default="01", null=True)
    day = models.CharField(max_length=2, default="01", null=True)
    hour = models.CharField(max_length=2, default="00", null=True)
    minute = models.CharField(max_length=2, default="00", null=True)
    second = models.CharField(max_length=2, default="00", null=True)

    consumption = models.BigIntegerField()
    consumption_units = models.CharField(max_length=3, default='kWh')

    temperature = models.IntegerField(null=True)
    temperature_units = models.CharField(max_length=1, default='F', null=True)

    cost = models.BigIntegerField(null=True)
    currency = models.CharField(max_length=3, default="USD", null=True)

    class Meta:
        unique_together = ((
                               "reading_id",
                               "year",
                               "month",
                               "day",
                               "hour",
                               "minute",
                               "second",
                               "house_id",
                               "neighborhood_id",
                               "aggregator_id",
                               "region_id",
                               "consumption",
                               "temperature",
                               "cost"
                           ), (
                               "year",
                               "month",
                               "day",
                               "hour",
                               "minute",
                               "second"),)

    def __str__(self):
        return str(self.region_id_id) + "/" + str(self.aggregator_id_id) + "//" + str(
            self.neighborhood_id_id) + "///" + str(self.house_id_id) + "////" + str(self.reading_id)


# Year represents the year that a reading was recorded in.
## The primary key for the field is a char field of length 4. Years are expected
## to be in the following format: 2018
## The field uses char fields rather than ints because they are easier to work with.

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=4)

    def __str__(self):
        return str(self.year)


# Month represents the month that a reading was recorded in.
## The primary key for the field is a char field of length 2. Months are expected
## to be in the following format: 01 or 12
## The field uses char fields rather than ints because they are easier to work with.

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Month(models.Model):
    month = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.month)


# Day represents the day that a reading was recorded in.
## The primary key for the field is a char field of length 2. Years are expected
## to be in the following format: 01 or 30
## The field uses char fields rather than ints because they are easier to work with.

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Day(models.Model):
    day = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.day)


# Hour represents the hour that a reading was recorded in.
## The primary key for the field is a char field of length 2. Years are expected
## to be in the following format: 01 or 19
## The field uses char fields rather than ints because they are easier to work with.

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Hour(models.Model):
    hour = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.hour)


# class Minute(models.Model):
#     Minute = models.CharField(primary_key=True, max_length=2)
#
#     def __str__(self):
#         return str(self.minute)
#
# class Second(models.Model):
#     second = models.CharField(primary_key=True, max_length=2)
#
#     def __str__(self):
#         return str(self.second)

# Region represents the region from which some reading was taken. Region is the
## outermost object in a heirarchy of objects. The objects within a region are:
## Aggregator, Neighborhood, and House

# region_id is the primary key for the Region model and is simply an auto incementing
## integer

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Region(models.Model):
    region_id = models.CharField(max_length=25)
    full_name = models.CharField(max_length=25, primary_key=True, default="full_name", )

    def __str__(self):
        return self.region_id

    def save(self):
        self.full_name = self.region_id
        super(Region, self).save()


# Aggregator represents the aggregator from which some reading was taken. Aggregator
## is the second outermost object in a heirarchy of objects. The objects within a
##aggregator are: Neighborhood, and House

# aggregator_id is the primary key for the Aggregator model and is simply an
##auto incementing integer

# region_id is a foreign key from the Region model and is simply an auto incementing
## integer

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Aggregator(models.Model):
    aggregator_id = models.CharField(max_length=25)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=51, primary_key=True, default="full_name")

    class Meta:
        unique_together = (("aggregator_id", 'region_id'),)

    def __str__(self):
        return self.region_id_id + "/" + self.aggregator_id

    def save(self):
        self.full_name = self.region_id_id + "/" + self.aggregator_id
        super(Aggregator, self).save()


# Neighborhood represents the neighborhood from which some reading was taken.
## Aggregator is the third outermost object in a heirarchy of objects. The
## object within a neighborhood is House

# neighborhood_id is the primary key for the Neighborhood model and is simply an
##auto incementing integer

# aggregator_id is a foreign key from the Aggregator model and is simply an
##auto incementing integer

# region_id is a foreign key from the Region model and is simply an auto incementing
## integer

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Neighborhood(models.Model):
    neighborhood_id = models.CharField(max_length=25)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE, )
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=78, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
                               "neighborhood_id",
                               "aggregator_id",
                               "region_id"
                           ),)

    def __str__(self):
        return self.aggregator_id_id + "//" + self.neighborhood_id

    def save(self):
        self.full_name = self.aggregator_id_id + "//" + self.neighborhood_id
        super(Neighborhood, self).save()


# House represents the house from which some reading was taken.
## House is the innermost object in a heirarchy of objects.

# house_id is the primary key for the House model and is simply an
##auto incementing integer

# neighborhood_id is a foreign key from the Neighborhood model and is simply an
##auto incementing integer

# aggregator_id is a foreign key from the Aggregator model and is simply an
##auto incementing integer

# region_id is a foreign key from the Region model and is simply an auto incementing
## integer

# __str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class House(models.Model):
    house_id = models.CharField(max_length=25)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, )
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE, )
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=106, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
                               "house_id",
                               "neighborhood_id",
                               "aggregator_id",
                               "region_id"
                           ),)

    def __str__(self):
        return self.neighborhood_id_id + "///" + self.house_id

    def save(self):
        self.full_name = self.neighborhood_id_id + "///" + self.house_id
        super(House, self).save()

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
