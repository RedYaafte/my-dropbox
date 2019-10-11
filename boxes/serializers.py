from rest_framework import serializers

from .models import Box


class BoxSerializers(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = ['pk', 'title', 'description', 'created', 'modified']
