from rest_framework import serializers

from .models import Box


class BoxSerializers(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    thing = serializers.FileField(required=False)

    def create(self, validated_data):
        return Box.objects.create(**validated_data)
