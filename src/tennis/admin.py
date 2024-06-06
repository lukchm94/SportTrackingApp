from django.contrib import admin

from .models.player import TennisPlayer


@admin.register(TennisPlayer)
class TennisPlayerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "nationality",
        "date_of_birth",
        "racket_brand",
        "racket_model",
    )
    search_fields = ("first_name", "last_name", "nationality")
