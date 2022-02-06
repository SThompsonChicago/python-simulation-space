from django.shortcuts import get_object_or_404, render
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

def detail(request, id):
    simulation = get_object_or_404(Simulation, pk=id)
    return render(request, 'sims/detail.html', { 'simulation': simulation })

def index(request):
    simulations = Simulation.objects.all()
    return render(request, 'index.html', { 'simulations': simulations })