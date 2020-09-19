from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    pbox = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
