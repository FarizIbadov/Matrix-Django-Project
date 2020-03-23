from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

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
    fields = ('department',)
    list_display = ('id','department',)
    list_filter = ('department',)
    search_fields = ('department',)

@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    fields = ('position',)
    list_display = ('id','position',)
    list_filter = ('position',)
    search_fields = ('position',)


class JobResource(resources.ModelResource):
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget=ForeignKeyWidget(Department, 'department'))
        
    position = fields.Field(
        column_name='position',
        attribute='position',
        widget=ForeignKeyWidget(Position, 'position'))
    
    training = fields.Field(
        column_name='training',
        attribute='training',
        widget=ManyToManyWidget(Training,separator=',', field='title'))
        
    class Meta:
        model=Job
        fields = ('id','department','position',)

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    list_display = ('id','department', 'position','get_training',)
    search_fields = ('department__department','position__position',)
    filter_horizontal = ('training',)
    list_filter = ('department__department','position__position',)
    resource_class = JobResource    
    # fields = ('department','position',)
    # list_filter = ('department','position',)
    # search_fields = ('department','position',)
    
    def get_training(self, instance):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((line,) for line in instance.get_training()),
        ) or mark_safe("<span class='errors'>Training is not assigned yet.</span>")
    get_training.short_description = 'Training'
    
# class MyForeignKeyWidget(ForeignKeyWidget):
#     def clean(self, value, row):
#         t1 = super(widgets.ForeignKeyWidget, self).clean(value)
#         return self.model.objects.get(id=t1) if t1 else None
#     def render(self, value):
#         return value.name

# class JobResource(resources.ModelResource):
#     department = fields.Field(column_name='department', attribute='department', widget=MyForeignKeyWidget(Department,))
#     position = fields.Field(column_name='position', attribute='position', widget=MyForeignKeyWidget(Position,))

#     class Meta:
#         model=Job
#         fields = ('id','department','position',)



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