from django.db.models import QuerySet
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse

from ..models.player import TennisPlayer


def find_player(req: HttpRequest) -> JsonResponse:
    first_name: str = req.GET.get("first_name")
    last_name: str = req.GET.get("last_name")
    if not first_name or not last_name:
        return HttpResponseBadRequest("Please provide both first name and last name.")
    try:
        player: TennisPlayer = TennisPlayer.objects.get(
            first_name=first_name, last_name=last_name
        )
        return JsonResponse(
            {
                "method": req.method,
                "data": model_to_dict(player),
            }
        )
    except TennisPlayer.DoesNotExist:
        return JsonResponse({"error": "Player not found"}, status=404)


def all_players(req: HttpRequest) -> JsonResponse:
    try:
        players: QuerySet = TennisPlayer.objects.all().values()
        return JsonResponse(
            {
                "method": req.method,
                "players": len([p for p in players]),
                "data": [p for p in players],
            }
        )
    except TennisPlayer.DoesNotExist:
        return JsonResponse({"error": "Player not found"}, status=404)
