from django.db import models

class Invitation(models.Model):
    employeeEmail = models.CharField(max_length=100, blank=True)
    confirmed = models.BooleanField(default=False)
    sender_username = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.employeeEmail

