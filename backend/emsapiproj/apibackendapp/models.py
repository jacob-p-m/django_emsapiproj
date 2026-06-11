from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100,unique=True)
    department_code = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name

#create class project

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=150)
    Description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField(null=True, blank=True)
    Budget = models.DecimalField(max_digits=12, decimal_places=2)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.ProjectName

#create  class Employee

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Designation = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    DateOfJoining = models.DateField()
    Contact = models.CharField(max_length=15)
    #one department can have many employees->one to many 
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    #many to many relationship
    Projects = models.ManyToManyField(Project, related_name='employees')
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.EmployeeName


