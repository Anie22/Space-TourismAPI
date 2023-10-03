from django.shortcuts import render
from urllib import request
from django.http import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import renderers
from SpaceAPI.serializers import DestinationSerializer, CrewSerializer, TechnologySerializer 
from SpaceAPI.models import *
from SpaceAPI.renderers import Space_TourismAPI
# Create your views here.


class DestinationViewSet(ViewSet):
    renderer_classes = [JSONRenderer, Space_TourismAPI]

    def list(self, request, format=None):
        travel = destination.objects.all()
        serializer = DestinationSerializer(travel, many=True)
        return Response(serializer.data)

class CrewViewSet(ViewSet):
    renderer_classes = [JSONRenderer, Space_TourismAPI]

    def list(self, request, format=None):
        people = crew.objects.all()
        serializer = CrewSerializer(people, many=True)
        return Response(serializer.data)

class TechnologyViewSet(ViewSet):
    renderer_classes = [JSONRenderer, Space_TourismAPI]

    def list(self, request, format=None):
        devices = technology.objects.all()
        serializer = TechnologySerializer(devices, many=True)
        return Response(serializer.data)