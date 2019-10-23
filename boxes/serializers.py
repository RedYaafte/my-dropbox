from rest_framework import serializers

from .models import Box


class BoxSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    thing = serializers.FileField(required=False)

    def create(self, validated_data):
        return Box.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.thing = validated_data.get('thing', instance.thing)
        instance.save()
        return instance
