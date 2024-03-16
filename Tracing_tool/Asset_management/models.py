# asset_management/models.py

from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
   

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    serial_number = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name

class AssetLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, related_name='checked_out_by', on_delete=models.CASCADE)
    checked_in_by = models.ForeignKey(Employee, related_name='checked_in_by', on_delete=models.CASCADE, null=True, blank=True)
    checked_out_date = models.DateTimeField(default=timezone.now)
    checked_in_date = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.asset} - Checked out by: {self.checked_out_by} on {self.checked_out_date}"
