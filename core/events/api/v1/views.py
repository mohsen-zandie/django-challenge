from rest_framework import viewsets

from events.api.v1.permissions import IsAdminOrReadOnly
from events.models.events import Event
from events.api.v1.serializers import EventSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
