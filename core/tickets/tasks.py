
from celery import shared_task
from django.contrib.auth import get_user_model

from tickets.models.tickets import Ticket
from tickets.models.baskets import Basket
from events.models.events import Event

# getting user model
User = get_user_model()


@shared_task
def create_ticket(event_id, user_id, seat, price):
    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)

    try:
        basket = Basket.objects.get(user=user)
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=user)

    ticket = Ticket.objects.create(
        event=event, user=user, basket=basket, seat=seat, price=price)
    return f"Ticket created: {ticket}"
