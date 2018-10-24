from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from basic.models import Location
from basic.serializers import LocationSerializer
import io

@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_list_of_tusas(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations,many=True)
        return JsonResponse(serializer.data,safe=False,status=200)