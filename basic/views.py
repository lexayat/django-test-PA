from rest_framework import generics
from basic.models import Tusa
from basic.serializers import TusaSerializer


class TusasList(generics.ListCreateAPIView):
    queryset = Tusa.objects.all()
    serializer_class = TusaSerializer

class TusasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tusa.objects.all()
    serializer_class = TusaSerializer

