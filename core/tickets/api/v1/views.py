from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tickets.models import Ticket, Basket
from tickets.api.v1.serializers import TicketSerializer, BasketSerializer


class TicketModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class BasketModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
