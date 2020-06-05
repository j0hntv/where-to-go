from django.db import models


class Place(models.Model):
    title = models.CharField('Title', max_length=200)
    description_short = models.TextField('Short description', blank=True)
    description_long = models.TextField('Long description', blank=True)
    lat = models.FloatField('Latitude')
    lon = models.FloatField('Longitude')

    def __str__(self):
        return self.title
