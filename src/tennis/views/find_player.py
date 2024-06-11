from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.serializers import CharField, ModelSerializer, Serializer

from app.__app_configs import HttpMethods

from ..models.player import TennisPlayer
from ..serializers.player import PlayerNotFoundError, PlayerReq, PlayerResp


@extend_schema(
    responses={
        status.HTTP_200_OK: PlayerResp,
        status.HTTP_404_NOT_FOUND: PlayerNotFoundError,
    },
    summary="Find Player by First and Last Names",
    description="""This endpoint takes the HttpRequest object, validates the input data using a serializer,
    retrieves a TennisPlayer object based on the provided first name and last name, and returns the
    player's data in a JSON response.""",
    methods=[HttpMethods.GET.value],
)
@api_view([HttpMethods.GET.value])
def find_player(req: HttpRequest) -> JsonResponse:
    serializer = PlayerReq(data=req.GET)

    if not serializer.is_valid():
        return HttpResponseBadRequest("Please provide both first name and last name.")
    try:
        first_name: str = serializer.validated_data.get("first_name")
        last_name: str = serializer.validated_data.get("last_name")
        player: TennisPlayer = TennisPlayer.objects.get(
            first_name=first_name, last_name=last_name
        )
        player_data: PlayerResp = PlayerResp(player).data
        return JsonResponse(
            {
                "method": req.method,
                "data": player_data,
            },
        )
    except TennisPlayer.DoesNotExist:
        return JsonResponse(
            {"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view([HttpMethods.GET.value])
def all_players(req: HttpRequest) -> JsonResponse:
    """
    This function retrieves all tennis players from the database and returns a JSON response with
    information about the players.

    :param req: The `req` parameter in the `all_players` function is of type `HttpRequest`, which is
    typically a request object representing an incoming HTTP request. It contains information about the
    request made by the client, such as headers, method, body, and other request-related data
    :type req: HttpRequest
    :return: The `all_players` function returns a JSON response containing the HTTP method used in the
    request, the total number of players retrieved from the database, and a list of player data in JSON
    format. If an exception of type `TennisPlayer.DoesNotExist` is raised (indicating that no players
    were found), it returns a JSON response with an error message and a status code of 404.
    """
    try:
        players: QuerySet = TennisPlayer.objects.all().values()
        players_data: PlayerResp = [PlayerResp(player).data for player in players]
        return JsonResponse(
            {
                "method": req.method,
                "players": len(players_data),
                "data": players_data,
            }
        )
    except TennisPlayer.DoesNotExist:
        return JsonResponse({"error": "Player not found"}, status=404)
