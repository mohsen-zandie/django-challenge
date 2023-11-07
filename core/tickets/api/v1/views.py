from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from tickets.models.tickets import Ticket
from tickets.models.baskets import Basket
from tickets.api.v1.serializers import TicketSerializer, BasketSerializer
from tickets.tasks import create_ticket


class TicketModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event_id = serializer.validated_data.get('event').id
        user_id = serializer.validated_data.get('user').id
        seat = serializer.validated_data.get('seat')
        price = serializer.validated_data.get('price')

        create_ticket.delay(event_id, user_id, seat, price)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BasketModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
