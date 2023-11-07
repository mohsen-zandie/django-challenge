from rest_framework import serializers

from tickets.models.tickets import Ticket
from tickets.models.baskets import Basket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "event",
            "user",
            "seat",
            "price",
            "created_at",
            "updated_at",
        )


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = (
            "id",
            "user",
            "ticket",
            "is_paid",
            "created_at",
            "updated_at",
        )
