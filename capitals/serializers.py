from rest_framework import serializers


class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=200)
    capital_population = serializers.IntegerField()
    author = serializers.CharField(source='author.username', max_length=200)
