from django.db.models import QuerySet
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from drf_yasg.openapi import TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, Schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.serializers import CharField, Serializer

from app.__app_configs import HttpMethods

from ..models.player import TennisPlayer


class FindPlayerSerializer(Serializer):
    first_name = CharField()
    last_name = CharField()


@api_view([HttpMethods.GET.value])
@swagger_auto_schema(
    request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            "first_name": Schema(type=TYPE_STRING),
            "last_name": Schema(type=TYPE_STRING),
        },
        required=["first_name", "last_name"],
    ),
    responses={200: "Success response description"},
    operation_description="Endpoint to render http template to calculate math operations on the two numbers",
)
def find_player(req: HttpRequest) -> JsonResponse:
    serializer = FindPlayerSerializer(data=req.GET)

    if not serializer.is_valid():
        return HttpResponseBadRequest("Please provide both first name and last name.")
    try:
        first_name: str = serializer.validated_data.get("first_name")
        last_name: str = serializer.validated_data.get("last_name")
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
