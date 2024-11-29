from league_sphere.models.cricket_player import CricketPlayer


def list_cricket_players(
    organisation_id: int,
):
    queryset = CricketPlayer.objects.filter(organisation_id=organisation_id)
    return queryset