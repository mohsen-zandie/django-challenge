from django.db import models
from django.contrib.auth import get_user_model

# getting user model
User = get_user_model()


class Basket(models.Model):
    """
    Basket model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
