from rest_framework import serializers
from events.models import Event, Stadium


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "stadium",
            "date",
            "price",
            "description",
            "created_at",
            "updated_at",
        )


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = (
            "id",
            "name",
            "capacity",
            "city",
            "country",
            "address",
            "opened",
            "description",
            "created_at",
            "updated_at",
        )
