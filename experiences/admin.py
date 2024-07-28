from django.contrib import admin
from .models import Perk, Experience


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "details",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "start",
        "end",
        "price",
    )
