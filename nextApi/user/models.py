from django.db import models
from company.models import Company

# Create your models here.
class CompanyAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    usesrname = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    companyName = models.CharField(max_length=120, blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.usesrname
