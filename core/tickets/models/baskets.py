from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from tickets.models.tickets import Ticket

# getting user model
User = get_user_model()


class Basket(models.Model):
    """
    Basket model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticket} - {self.user}"


@receiver(post_save, sender=Ticket)
def create_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(ticket=instance, user=instance.user)
