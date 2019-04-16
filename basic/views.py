from rest_framework import generics
from basic.models import Location
from basic.serializers import LocationSerializer
from basic.models import Tusa
from basic.serializers import TusaSerializer

class LocationsList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TusasList(generics.ListCreateAPIView):
    queryset = Tusa.objects.all()
    serializer_class = TusaSerializer

class TusasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tusa.objects.all()
    serializer_class = TusaSerializer