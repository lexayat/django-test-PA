from rest_framework import serializers
from basic.models import Location

class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    secure_radius = serializers.IntegerField()

    def create(self,validated_data):
        return Location.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.lat = validated_data.get('lat',instance.lat)
        instance.lng = validated_data.get('lng',instance.lng)
        instance.secure_radius = validated_data.get('secure_radius',instance.secure_radius)
        instance.save()
        return instance