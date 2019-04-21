from rest_framework import serializers
from basic.models import Tusa


class TusaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    place = serializers.CharField()
    description = serializers.CharField()
   # geo =
    mens = serializers.IntegerField()
    girls = serializers.IntegerField()
    image = serializers.ImageField()
    tags = serializers.CharField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    tusadate = serializers.DateTimeField()
    type = serializers.CharField()

    def create(self,validated_data):
        return Tusa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.place = validated_data.get('place',instance.place)
        instance.description = validated_data.get('description',instance.description)
        instance.mens = validated_data.get('mens',instance.mens)
        instance.girls = validated_data.get('girls',instance.girls)
        instance.image = validated_data.get('image',instance.image)
        instance.tags = validated_data.get('tags',instance.tags)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.tusadate = validated_data.get('tusadate',instance.date)
        instance.type = validated_data.get('type',instance.type)
        instance.save()
        return instance

