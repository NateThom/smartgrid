from django.db import models


class PowerSystemGenerationData(models.Model):
    power_system = models.IntegerField(primary_key=True)

    load_feeder_group = models.ForeignKey('AnnualPeakDemandAtLoadFeeder', on_delete=models.CASCADE)

    weekly_load_peak_group = models.ForeignKey('WeeklyLoadPercentOfAnnualPeak', on_delete=models.CASCADE)

    daily_load_peak_group = models.ForeignKey('DailyLoadPercentOfWeeklyPeak', on_delete=models.CASCADE)

    hourly_load_peak_group = models.ForeignKey('HourlyLoadPercentOfDailyPeakTimeOfYear', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("power_system", "load_feeder_group", "weekly_load_peak_group",
                           "daily_load_peak_group", "hourly_load_peak_group")

    def __str__(self):
        return 'PowerSystemGenerationData: ' + str(self.power_system)


class HourlyLoadPercentOfDailyPeakTimeOfYear(models.Model):
    hourly_load_peak_time_of_year_group = models.AutoField(primary_key=True)

    winter_weeks_group = models.ForeignKey('HourlyLoadPercentOfDailyPeakTimeOfWeek', on_delete=models.CASCADE,
                                           related_name='hourly_peak_load_time_of_year_winter')
    summer_weeks_group = models.ForeignKey('HourlyLoadPercentOfDailyPeakTimeOfWeek', on_delete=models.CASCADE,
                                           related_name='hourly_peak_load_time_of_year_summer')
    spring_fall_weeks_group = models.ForeignKey('HourlyLoadPercentOfDailyPeakTimeOfWeek', on_delete=models.CASCADE,
                                                related_name='hourly_peak_load_time_of_year_spring_fall')

    class Meta:
        unique_together = (
            "hourly_load_peak_time_of_year_group", "winter_weeks_group", "summer_weeks_group", "spring_fall_weeks_group")

    def __str__(self):
        return 'HourlyLoadPercentOfDailyPeakTimeOfYear: ' + str(self.hourly_load_peak_time_of_year_group)


class HourlyLoadPercentOfDailyPeakTimeOfWeek(models.Model):
    hourly_load_peak_time_of_week_group = models.AutoField(primary_key=True)

    weekday_group = models.ForeignKey('HourlyLoadPercentOfDailyPeak', on_delete=models.CASCADE,
                                      related_name='hourly_peak_load_time_of_week_day')
    weekend_group = models.ForeignKey('HourlyLoadPercentOfDailyPeak', on_delete=models.CASCADE,
                                      related_name='hourly_peak_load_time_of_week_end')

    class Meta:
        unique_together = ("hourly_load_peak_time_of_week_group", "weekday_group", "weekend_group")

    def __str__(self):
        return 'HourlyLoadPercentOfDailyPeakTimeOfWeek: ' + str(self.hourly_load_peak_time_of_week_group)


class HourlyLoadPercentOfDailyPeak(models.Model):
    hourly_load_peak_group = models.AutoField(primary_key=True)

    hour_1 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_1')
    hour_2 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_2')
    hour_3 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_3')
    hour_4 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_4')
    hour_5 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_5')
    hour_6 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_6')
    hour_7 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_7')
    hour_8 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_8')
    hour_9 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_9')
    hour_10 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_10')
    hour_11 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_11')
    hour_12 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_12')
    hour_13 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_13')
    hour_14 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_14')
    hour_15 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_15')
    hour_16 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_16')
    hour_17 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_17')
    hour_18 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_18')
    hour_19 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_19')
    hour_20 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_20')
    hour_21 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_21')
    hour_22 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_22')
    hour_23 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_23')
    hour_24 = models.ForeignKey('HourlyPeakLoad', on_delete=models.CASCADE, related_name='hourly_peak_load_24')

    class Meta:
        unique_together = (
            "hourly_load_peak_group", "hour_1", "hour_2", "hour_3", "hour_4", "hour_5", "hour_6", "hour_7", "hour_8",
            "hour_9", "hour_10", "hour_11", "hour_12", "hour_13", "hour_14", "hour_15", "hour_16", "hour_17", "hour_18",
            "hour_19", "hour_20", "hour_21", "hour_22", "hour_23", "hour_24")

    def __str__(self):
        return 'HourlyLoadPercentOfDailyPeak: ' + str(self.hourly_load_peak_group)


class HourlyPeakLoad(models.Model):
    hourly_load_peak = models.AutoField(primary_key=True)

    peak_load = models.FloatField()

    class Meta:
        unique_together = ("hourly_load_peak", "peak_load")

    def __str__(self):
        return 'HourlyPeakLoad: ' + str(self.hourly_load_peak)


class DailyLoadPercentOfWeeklyPeak(models.Model):
    daily_load_peak_group = models.AutoField(primary_key=True)

    day_1 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_1')
    day_2 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_2')
    day_3 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_3')
    day_4 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_4')
    day_5 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_5')
    day_6 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_6')
    day_7 = models.ForeignKey('DailyPeakLoad', on_delete=models.CASCADE, related_name='daily_peak_load_7')

    class Meta:
        unique_together = (
            "daily_load_peak_group", "day_1", "day_2", "day_3", "day_4", "day_5", "day_6", "day_7")

    def __str__(self):
        return 'DailyLoadPercentOfWeeklyPeak: ' + str(self.daily_load_peak_group)


class DailyPeakLoad(models.Model):
    daily_load_peak = models.AutoField(primary_key=True)

    peak_load = models.FloatField()

    class Meta:
        unique_together = ("daily_load_peak", "peak_load")

    def __str__(self):
        return 'DailyPeakLoad: ' + str(self.daily_load_peak)


class WeeklyLoadPercentOfAnnualPeak(models.Model):
    weekly_load_peak_group = models.AutoField(primary_key=True)

    week_1 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_1')
    week_2 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_2')
    week_3 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_3')
    week_4 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_4')
    week_5 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_5')
    week_6 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_6')
    week_7 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_7')
    week_8 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_8')
    week_9 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_9')
    week_10 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_10')
    week_11 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_11')
    week_12 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_12')
    week_13 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_13')
    week_14 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_14')
    week_15 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_15')
    week_16 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_16')
    week_17 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_17')
    week_18 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_18')
    week_19 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_19')
    week_20 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_20')
    week_21 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_21')
    week_22 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_22')
    week_23 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_23')
    week_24 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_24')
    week_25 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_25')
    week_26 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_26')
    week_27 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_27')
    week_28 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_28')
    week_29 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_29')
    week_30 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_30')
    week_31 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_31')
    week_32 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_32')
    week_33 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_33')
    week_34 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_34')
    week_35 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_35')
    week_36 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_36')
    week_37 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_37')
    week_38 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_38')
    week_39 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_39')
    week_40 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_40')
    week_41 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_41')
    week_42 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_42')
    week_43 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_43')
    week_44 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_44')
    week_45 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_45')
    week_46 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_46')
    week_47 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_47')
    week_48 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_48')
    week_49 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_49')
    week_50 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_50')
    week_51 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_51')
    week_52 = models.ForeignKey('WeeklyPeakLoad', on_delete=models.CASCADE, related_name='weekly_peak_load_52')

    class Meta:
        unique_together = (
            "weekly_load_peak_group", "week_1", "week_2", "week_3", "week_4", "week_5", "week_6", "week_7", "week_8",
            "week_9", "week_10", "week_11", "week_12", "week_13", "week_14", "week_15", "week_16", "week_17", "week_18",
            "week_19", "week_20", "week_21", "week_22", "week_23", "week_24", "week_25", "week_26", "week_27",
            "week_28", "week_29", "week_30", "week_31", "week_32", "week_33", "week_34", "week_35", "week_36",
            "week_37", "week_38", "week_39", "week_40", "week_41", "week_42", "week_43", "week_44", "week_45",
            "week_46", "week_47", "week_48", "week_49", "week_50", "week_51", "week_52")

    def __str__(self):
        return 'WeeklyLoadPercentOfAnnualPeak: ' + str(self.weekly_load_peak_group)


class WeeklyPeakLoad(models.Model):
    weekly_load_peak = models.AutoField(primary_key=True)

    peak_load = models.FloatField()

    class Meta:
        unique_together = ("weekly_load_peak", "peak_load")

    def __str__(self):
        return 'WeeklyPeakLoad: ' + str(self.weekly_load_peak)


class AnnualPeakDemandAtLoadFeeder(models.Model):
    load_feeder_group = models.AutoField(primary_key=True)

    load_1 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_1')
    load_2 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_2')
    load_3 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_3')
    load_4 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_4')
    load_5 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_5')
    load_6 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_6')
    load_7 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_7')
    load_8 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_8')
    load_9 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_9')
    load_10 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_10')
    load_11 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_11')
    load_12 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_12')
    load_13 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_13')
    load_14 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_14')
    load_15 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_15')
    load_16 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_16')
    load_17 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_17')
    load_18 = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_18')
    load_19_aggregate = models.ForeignKey('LoadFeeder', on_delete=models.CASCADE, related_name='load_feeder_19')

    class Meta:
        unique_together = (
            "load_feeder_group", "load_1", "load_2", "load_3", "load_4", "load_5", "load_6", "load_7", "load_8",
            "load_9", "load_10", "load_11", "load_12", "load_13", "load_14", "load_15", "load_16", "load_17", "load_18",
            "load_19_aggregate")

    def __str__(self):
        return 'AnnualPeakDemandAtLoadFeeder: ' + str(self.load_feeder_group)


class LoadFeeder(models.Model):
    load_feeder = models.AutoField(primary_key=True)

    active_power = models.FloatField()
    active_power_units = models.CharField(max_length=3, default='MW')

    reactive_power = models.FloatField()
    reactive_power_units = models.CharField(max_length=3, default='MVr')

    apparent_power = models.FloatField()
    apparent_power_units = models.CharField(max_length=3, default='MWA')

    power_factor = models.FloatField(default=0.9)

    class Meta:
        unique_together = ("load_feeder", "active_power", "active_power_units", "reactive_power",
                           "reactive_power_units", "apparent_power", "apparent_power_units", "power_factor")

    def __str__(self):
        return 'LoadFeeder: ' + str(self.load_feeder)


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


#The reading model is the main model and is made up of some internal
## information and the other models as foreign keys. It represents a
## single reading from some sensor or smart meter.

#reading_id is simply the primary key for Reading. It autoincrements
## and is represented by an integer

#the time that each reading was recorded is represented by a corresponding year,
## month, day, and hour field. In the future I would like to change these fields
## so that they inherit from one another much like the postion (Region, Aggregator, etc)
## fields do now. All of the dates are foreign keys from individual tables

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

    house_id = models.ForeignKey('House', on_delete=models.CASCADE, null=True,)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, null=True,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE, null=True,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)

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
        ),(
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "second"),)

    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id_id)+"////"+str(self.reading_id)

#Year represents the year that a reading was recorded in.
## The primary key for the field is a char field of length 4. Years are expected
## to be in the following format: 2018
## The field uses char fields rather than ints because they are easier to work with.

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=4)

    def __str__(self):
        return str(self.year)

#Month represents the month that a reading was recorded in.
## The primary key for the field is a char field of length 2. Months are expected
## to be in the following format: 01 or 12
## The field uses char fields rather than ints because they are easier to work with.

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Month(models.Model):
    month = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.month)

#Day represents the day that a reading was recorded in.
## The primary key for the field is a char field of length 2. Years are expected
## to be in the following format: 01 or 30
## The field uses char fields rather than ints because they are easier to work with.

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Day(models.Model):
    day = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.day)

#Hour represents the hour that a reading was recorded in.
## The primary key for the field is a char field of length 2. Years are expected
## to be in the following format: 01 or 19
## The field uses char fields rather than ints because they are easier to work with.

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Hour(models.Model):
    hour = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return str(self.hour)
#
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

#Region represents the region from which some reading was taken. Region is the
## outermost object in a heirarchy of objects. The objects within a region are:
## Aggregator, Neighborhood, and House

#region_id is the primary key for the Region model and is simply an auto incementing
## integer

#__str__(self) gives the model a name in the django api. The name is a string
## made up of the fields in the return statement
class Region(models.Model):
    region_id = models.CharField(max_length=25)
    full_name = models.CharField(max_length=25, primary_key=True, default="full_name",)

    def __str__(self):
        return self.region_id

    def save(self):
        self.full_name = self.region_id
        super(Region, self).save()

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
    aggregator_id = models.CharField(max_length=25)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    full_name = models.CharField(max_length=51, primary_key=True, default="full_name")

    class Meta:
        unique_together = (("aggregator_id", 'region_id'),)

    def __str__(self):
        return self.region_id_id+"/"+self.aggregator_id

    def save(self):
        self.full_name = self.region_id_id+"/"+self.aggregator_id
        super(Aggregator, self).save()

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
    neighborhood_id = models.CharField(max_length = 25)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    full_name = models.CharField(max_length = 78, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)

    def __str__(self):
        return self.aggregator_id_id+"//"+self.neighborhood_id

    def save(self):
        self.full_name = self.aggregator_id_id+"//"+self.neighborhood_id
        super(Neighborhood, self).save()

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
    house_id = models.CharField(max_length = 25)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    full_name = models.CharField(max_length = 106, primary_key=True, default="full_name")

    class Meta:
        unique_together = ((
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)

    def __str__(self):
        return self.neighborhood_id_id+"///"+self.house_id

    def save(self):
        self.full_name = self.neighborhood_id_id+"///"+self.house_id
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
