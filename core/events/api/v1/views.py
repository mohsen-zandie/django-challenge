from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from events.models import Event
from events.api.v1.serializers import EventSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    permissionn_classes = ['IsAuthenticated']
    serializer_class = EventSerializer
    queryset = Event.objects.all()
