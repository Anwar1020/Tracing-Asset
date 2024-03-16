
from rest_framework import serializers
from .models import Company, Employee, Asset, AssetLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location']  

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'company', 'email', 'phone_number']  

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'name', 'company', 'assigned_to', 'serial_number']  

class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        fields = ['id', 'asset', 'checked_out_by', 'checked_in_by', 'checked_out_date', 'checked_in_date']  
