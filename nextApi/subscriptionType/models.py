from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
