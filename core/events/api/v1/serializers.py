from rest_framework import serializers
from events.models import Event


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
