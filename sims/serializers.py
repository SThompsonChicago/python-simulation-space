from sims.models import Comment
from rest_framework import serializers

class SimulationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    