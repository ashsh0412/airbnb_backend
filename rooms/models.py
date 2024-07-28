from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    class RoomKindChoices(models.TextChoices):

        ENTIRE_PLACE = ("entire_place", "ENTIRE PLACE")
        PRIVATE_ROOM = ("private_room", "PRIVATE ROOM")
        SHARED_ROOM = ("shared_room", "SHARED ROOM")

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=100,
    )
    pet_allowed = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()


class Amenity(CommonModel):

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=100,
        default="",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
