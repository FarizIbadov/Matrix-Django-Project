from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export import widgets

class TrainingGroup(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('title',)
        verbose_name='Training group'
        verbose_name_plural='Training groups'

class Training(models.Model):
    training_group = models.ForeignKey(TrainingGroup, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('title', 'training_group',)
        verbose_name='Training'
        verbose_name_plural='Training'

class Location(models.Model):
    project = models.CharField(max_length=100)
    cost_code = models.CharField(max_length=20)

    def __str__(self):
        return self.project

    class Meta:
        ordering=('project', 'cost_code',)
        verbose_name='Location'
        verbose_name_plural='Locations'

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='Department'
        verbose_name_plural='Departments'

class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('title',)
        verbose_name='Position'
        verbose_name_plural='Positions'

class Job(models.Model):
    department = models.ForeignKey(Department, to_field='name',on_delete=models.CASCADE,blank=False, null=True)
    position = models.ForeignKey(Position, to_field='title',on_delete=models.CASCADE,blank=False, null=True)

    def __str__(self):
        return str(self.department.name) + str(" - ") + str(self.position.title)

    class Meta:
        ordering=('department', 'position',)
        verbose_name='Job'
        verbose_name_plural='Jobs'

class Matrix(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE,blank=False, null=True)
    status = models.BooleanField(choices=(
        (True, 'R'), 
        (False, 'N/R')
        ), default=False)

    def __str__(self):
         return f"{self.job.department} - {self.job.position}"

    class Meta:
        ordering=('job', 'training', 'status',)
        verbose_name='Matrix'
        verbose_name_plural='Matrix'


class Employee(models.Model):
    badge = models.CharField(max_length=15, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    status = models.BooleanField(choices=(
        (True, 'Active'), 
        (False, 'Inactive')
        ), default=True)
    job = models.ForeignKey(Matrix, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.badge)+ str(" - ") + str(self.name)

    class Meta:
        ordering=('name', 'badge', 'start_date', 'status',)
        verbose_name='Employee'
        verbose_name_plural='Employees'

# class TrainingData(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
#     training = models.ForeignKey(Employee, to_field='job.training.title', on_delete=models.CASCADE, blank=True, null=True)
#     date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=True)
    



