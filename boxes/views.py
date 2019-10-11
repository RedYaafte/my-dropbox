from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import Box
from .serializers import BoxSerializers


class BoxViewSet(ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializers


# @api_view(['GET'])
# def get_box_list(request):
#     queryset = Box.objects.all()
#     return Response({"Hola": "Mundo"}, status=status.HTTP_200_OK)
