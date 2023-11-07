from rest_framework import serializers
from events.models.events import Event


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
