from django.db import models
from company.models import Company
from subscriptionType.models import Subscription 


# Create your models here.
class Reservations(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    starDate = models.DateField()
    endDate = models.DateField()
    
    def __str__(self):
        return self.company.name