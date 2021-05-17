from django.db import models

from django.contrib.auth import get_user_model


class Capital(models.Model):
    country = models.CharField('country', max_length=150)
    capital_city = models.CharField('capital', max_length=150)
    capital_population = models.IntegerField('population')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.capital_city
