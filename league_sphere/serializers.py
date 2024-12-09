# serializers.py
from rest_framework import serializers
from league_sphere.models.cricket_player import CricketPlayer

class CricketPlayerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modified_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = CricketPlayer
        fields = '__all__'

