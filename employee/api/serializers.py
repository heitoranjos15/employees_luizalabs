from rest_framework import serializers
from employee.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']
