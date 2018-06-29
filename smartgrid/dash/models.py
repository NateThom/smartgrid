from django.db import models

# Create your models here.
# Create tables in the following order:
# appliance_type, region, aggregator, neighborhood,
## house, appliance, readings


class Appliance_Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    description = models.TextField()
    def __str__(self):
        return str(self.type_id)

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_consumption = models.BigIntegerField()
    def __str__(self):
        return str(self.region_id)


class Aggregator(models.Model):
    aggregator_id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    aggregator_consumption = models.BigIntegerField()

    class Meta:
        unique_together = (("aggregator_id", 'region_id'),)

    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id)

class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(primary_key=True)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    neighborhood_consumption = models.BigIntegerField()

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
    house_consumption = models.BigIntegerField()

    class Meta:
        unique_together = ((
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)
    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id)

class Appliance(models.Model):
    appliance_id = models.AutoField(primary_key=True)
    house_id = models.ForeignKey('House', on_delete=models.CASCADE,)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    type_id = models.ForeignKey('Appliance_Type', on_delete=models.CASCADE,)
    appliance_consumption = models.BigIntegerField()

    class Meta:
        unique_together = ((
        "appliance_id",
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id"
        ),)
    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id_id)+"////"+str(self.appliance_id)

class Readings(models.Model):
    date_time = models.CharField(max_length=19)
    house_id = models.ForeignKey('House', on_delete=models.CASCADE,)
    neighborhood_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE,)
    aggregator_id = models.ForeignKey('Aggregator', on_delete=models.CASCADE,)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE,)
    kWh = models.BigIntegerField()
    outdoor_temp = models.IntegerField()

    class Meta:
        unique_together = ((
        "date_time",
        "house_id",
        "neighborhood_id",
        "aggregator_id",
        "region_id",
        "kWh",
        "outdoor_temp"
        ),)
    def __str__(self):
        return str(self.region_id_id)+"/"+str(self.aggregator_id_id)+"//"+str(self.neighborhood_id_id)+"///"+str(self.house_id_id)+"////"+str(self.date_time)
