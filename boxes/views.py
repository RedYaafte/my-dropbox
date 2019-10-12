from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import Box
from .serializers import BoxSerializers


@api_view(['GET', 'POST'])
def box_list(request):
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializers(boxes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoxSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def box_detail(request, pk):
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoxSerializers(box)
        return Response(serializer.data)
