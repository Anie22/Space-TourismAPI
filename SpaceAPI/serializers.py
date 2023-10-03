from rest_framework import serializers
from SpaceAPI.models import *

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = destination
        fields = '__all__'

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = crew
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = technology
        fields = '__all__'