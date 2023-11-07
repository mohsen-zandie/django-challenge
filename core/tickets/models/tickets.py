from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.models import Event
from tickets.models.baskets import Basket

# getting user model
User = get_user_model()


class Ticket(models.Model):
    """
    Ticket model 
    """

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, null=True, blank=True)
    seat = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event} - {self.user}"


@receiver(post_save, sender=Ticket)
def create_basket_for_ticket(sender, instance, created, **kwargs):
    if created and not instance.basket:
        try:
            basket = Basket.objects.get(user=instance.user)
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=instance.user)
        instance.basket = basket
        instance.save()
