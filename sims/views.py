from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Simulation
from .serializers import SimulationSerializer

@api_view()
def sim_list(request):
    queryset = Simulation.objects.all()
    serializer = SimulationSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def sim_page(request, id):
    try:
        simulation = Simulation.objects.get(pk=id)
        serializer = SimulationSerializer(simulation)
        return Response(serializer.data)
    except Simulation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)