from django.db import models


class Capital(models.Model):
    country = models.CharField('country', max_length=150)
    capital_city = models.CharField('capital', max_length=150)
    capital_population = models.IntegerField('population')

    def str(self):
        return self.capital_city
