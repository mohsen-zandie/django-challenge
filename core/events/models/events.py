from django.db import models

from stadiums.models import Stadium


class Event(models.Model):
    """
    Event model (match, concert, etc.)
    """

    name = models.CharField(max_length=100)
    stadium = models.ForeignKey(
        Stadium, on_delete=models.CASCADE, null=True, blank=True, default=None)
    date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
