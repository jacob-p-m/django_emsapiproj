from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer
from .models import Department, Employee, Project
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
# create view for department

#class based view
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = [
        'Department',
        'Designation'
    ]
    search_fields = [
        'Employee'
    ]