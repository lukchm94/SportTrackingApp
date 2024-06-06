from django import forms

from ..models.player import TennisPlayer


class TennisPlayerForm(forms.ModelForm):
    class Meta:
        model = TennisPlayer
        fields: list[str] = [
            field.name for field in TennisPlayer._meta.fields if field.name != "id"
        ]
