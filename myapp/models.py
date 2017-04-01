from django.db import models
import cities_light
#from cities_light.models import City, Country
from cities_light.abstract_models import AbstractCountry, AbstractRegion, AbstractCity
from cities_light.receivers import connect_default_signals

class Country(AbstractCountry):
    pass

connect_default_signals(Country)

class Region(AbstractRegion):
    pass

connect_default_signals(Region)

class City(AbstractCity):
    pass

connect_default_signals(City)

#def filter_city_import(sender, items, **kwargs):
#    if items[8] not in ('CA'):
#        raise cities_light.InvalidItems()
#cities_light.signals.city_items_pre_import.connect(filter_city_import)

class Province(models.Model):
    province = models.CharField(max_length=30)

    def __str__(self):
        return self.province

class MyGeo(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.name
