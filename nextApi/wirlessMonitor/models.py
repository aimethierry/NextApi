from django.db import models
from employee.models import employeeAccount
from company.models import Company


# Create your models here to check all wifi slected by the companies 
class internetMonitor(models.Model):
    employee = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)
    
    def __str__(self):
        return self.name



# Create your models here.
class vpnApi(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    username = models.CharField(max_length=120, blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class vpnFile(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    upload = models.FileField(upload_to ='uploads/') 

    def __str__(self):
        return self.name

