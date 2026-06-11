#create a serializer for Department Class
from rest_framework import serializers
from .models import Department, Employee, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: #to give additional information
        model = Department
        fields = '__all__' #serialize the entire fields of department

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: #to give additional information
        model = Project
        fields = '__all__' #serialize the entire fields of department

class EmployeeSerializer(serializers.ModelSerializer):
    DepartmentSerializer(source = 'Department',read_only=True)

    class Meta: #to give additional information
        model = Employee
        fields = '__all__' #serialize the entire fields of department

