from league_sphere.models.cricket_player import CricketPlayer
from league_sphere.serializers import CricketPlayerSerializer
from rest_framework.response import Response


def list_cricket_players(
    organisation_id: int,
):
    queryset = CricketPlayer.objects.filter(organisation_id=organisation_id)
    serializer = CricketPlayerSerializer(queryset, many=True)
    return Response(serializer.data)
