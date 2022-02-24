from django.db import models
from tastypie.resources import ModelResource
from sims.models import Simulation

class SimResource(ModelResource):
    class Meta:
        queryset = Simulation.objects.all()
        resource_name = 'simulations'
