from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from SpaceAPI.views import *

urlpatterns = [
    path('destination/', DestinationViewSet.as_view({'get': 'list'}), name='destination'),
    path('crew/', CrewViewSet.as_view({'get': 'list'}), name='crew'),
    path('technology/', TechnologyViewSet.as_view({'get': 'list'}), name='technologie'),
]

urlpatterns = format_suffix_patterns(urlpatterns)