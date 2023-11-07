from rest_framework import viewsets
from events.api.v1.permissions import IsAdminOrReadOnly


from events.models import Event, Stadium
from events.api.v1.serializers import EventSerializer, StadiumSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class StadiumModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()
