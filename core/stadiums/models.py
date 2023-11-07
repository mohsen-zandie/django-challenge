from django.db import models


class Stadium(models.Model):
    """
    Stadium model (arena, stadium, etc.)
    """

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    opened = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StadiumPlan(models.Model):
    """
    StadiumPlan model : we assume the shape of stadium are rectangular
    """
    name = models.CharField(max_length=100)
    stadium = models.ForeignKey(
        Stadium, on_delete=models.CASCADE, default=None)
    rows = models.IntegerField()
    columns = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.stadium.name} - {self.name}'
