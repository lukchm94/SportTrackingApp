from rest_framework.serializers import CharField, ModelSerializer, Serializer

from ..models.player import TennisPlayer


class PlayerReq(Serializer):
    first_name = CharField()
    last_name = CharField()


class PlayerResp(ModelSerializer):
    class Meta:
        model = TennisPlayer
        fields = "__all__"


class PlayerNotFoundError(Serializer):
    error = CharField(
        help_text="The details of the error message", default="Player not found"
    )
