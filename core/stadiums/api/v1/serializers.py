from rest_framework import serializers
from events.models import Stadium, StadiumPlan


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


class StadiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumPlan
        fields = (
            "id",
            "name",
            "row_size",
            "column_size",
            "created_at",
            "updated_at",
        )
