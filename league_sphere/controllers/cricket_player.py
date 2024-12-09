from django.http import JsonResponse
from league_sphere.models.cricket_player import CricketPlayer
from league_sphere.serializers import CricketPlayerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def filter(request):
    print("--------headers--------", request.headers)
    organisation_id = request.headers.get("organisation_id")
    queryset = CricketPlayer.objects.all()
    if organisation_id:
        queryset = queryset.filter(organisation_id=organisation_id)
    serialized_data = CricketPlayerSerializer(queryset, many=True).data
    return JsonResponse(serialized_data, safe=False)

def retrieve(request, pk):
    try:
        player_instance = CricketPlayer.objects.get(id=pk)
        serialized_data = CricketPlayerSerializer(player_instance).data
        return JsonResponse(serialized_data, safe=False)
    except Exception as e:
        return JsonResponse({"message": "Player does not exists"}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def update(request, pk):
    print("-----request-----", request)
    try:
        player_instance = CricketPlayer.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({"message": "Player does not exists"}, status=400)
