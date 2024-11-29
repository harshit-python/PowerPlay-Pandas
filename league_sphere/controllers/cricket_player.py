from league_sphere.gateways import cricket_player as cricket_player_gateway

def list_cricket_players(
    request
):
    organisation_id = request.GET.get("organisation_id")
    return cricket_player_gateway.list_cricket_players(
        organisation_id=organisation_id
    )
