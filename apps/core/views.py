from rest_framework import generics

from apps.core.filters import CarFilter
from apps.core.models import Car
from apps.core.serializers import RetrieveCarsSerializer


class GetCarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = RetrieveCarsSerializer
    filterset_class = CarFilter
    permission_classes = []
