from django.db import models
from django.contrib.auth import get_user_model

from events.models import Event

# getting user model
User = get_user_model()


class Ticket(models.Model):
    """
    Ticket model 
    """

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event} - {self.user}"
