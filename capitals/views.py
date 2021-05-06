from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Capital
from .serializers import CapitalSerializer


class GetCapitalInfoView(APIView):
    def get(self, request):
        # извлекаем набор всех записей из таблицы Capital
        queryset = Capital.objects.all()
        print(Capital.objects.first().__dict__)
        # создаём сериалайзер для извлечённого наборa записей
        serializer_for_queryset = CapitalSerializer(
            instance=queryset, # передаём набор записей
            many=True # указываем, что на вход подается именно набор, а не одна запись
        )
        return Response(serializer_for_queryset.data)
