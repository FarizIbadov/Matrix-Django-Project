from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    fields = ('badge', 'name','start_date','end_date','status', 'job','location',)
    list_display = ('badge', 'name','start_date','end_date','status', 'job','location',)
    list_filter = ('badge', 'name','start_date','end_date','status', 'job','location',)
    search_fields = ('badge', 'name','start_date','end_date', 'job','location',)

@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    fields = ('project','cost_code',)
    list_display = ('project','cost_code',)
    list_filter = ('project','cost_code',)
    search_fields = ('project','cost_code',)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    fields = ('title',)
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class JobResource(resources.ModelResource):
    department = fields.Field(
        column_name='department',
        attribute='Department',
        widget=ForeignKeyWidget(Department, 'name'))
        
    position = fields.Field(
        column_name='position',
        attribute='Position',
        widget=ForeignKeyWidget(Position, 'title'))

    class Meta:
        model=Job
        exclude = ('id',)
        fields = ('department','position',)

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    list_display = ('department', 'position')
    resource_class = JobResource    
    # fields = ('department','position',)
    # list_display = ('department','position',)
    # list_filter = ('department','position',)
    # search_fields = ('department','position',)

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
  

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    fields = ('title','training_group',)
    list_display = ('title','training_group',)
    list_filter = ('title','training_group',)
    search_fields = ('title','training_group',)

@admin.register(TrainingGroup)
class TrainingGroupAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    fields = ('job','training', 'status',)
    list_display = ('job','training', 'status',)
    list_filter = ('job','training', 'status',)
    search_fields = ('job','training', 'status',)

# @admin.register(TrainingData)
# class TrainingDataAdmin(admin.ModelAdmin):
#     fields = ('emloyee','training', 'date',)
#     list_display = ('emloyee','training', 'date',)
#     list_filter = ('emloyee','training', 'date',)
#     search_fields = ('emloyee','training', 'date',)