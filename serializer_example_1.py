import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from rest_framework import serializers

"""
Имитируем записи в модели Capital.
Создаём класс для записи, создаём 4 объекта этого класса, объединяем записи в набор (кверисет)
"""
class Capital(object): # аналог объекта записи об одной столице в модели Capital
    def __init__(self, country, capital_city, capital_population):
        self.country = country
        self.capital_city = capital_city
        self.capital_population = capital_population
# создаём 4 отдельные записи
capital_1 = Capital('Norway', 'Oslo', 693500)
capital_2 = Capital('Sweden ', 'Stockholm', 961600)
capital_3 = Capital('Finland', 'Helsinki', 655300)
capital_4 = Capital('Iceland', 'Reykjavik', 128800)
# объединяем записи в набор - аналог Capital.objects.all()
queryset = [capital_1, capital_2, capital_3, capital_4]

"""
Объявляем класс сериалайзера.
Создаём объект этого класса.
При создании указываем, что нужно преобразовать не одну табличную запись, а их набор (many=True),
передаем набор записей, который нужно преобразовать (instance=queryset)
"""
class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=200)
    capital_population = serializers.IntegerField()


serializer_obj = CapitalSerializer(instance=queryset, many=True)

print(serializer_obj.data)
