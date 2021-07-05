from rest_framework import serializers
from .models import Traffic, Road, Light

class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = "__all__"

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = "__all__"

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = "__all__"