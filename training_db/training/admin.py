from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('name','cost_code',)
    list_display = ('name','cost_code',)
    list_filter = ('name','cost_code',)
    search_fields = ('name','cost_code',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ('department','position',)
    list_display = ('department','position',)
    list_filter = ('department','position',)
    search_fields = ('department','position',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('badge', 'name','start_date','end_date','status', 'job','location',)
    list_display = ('badge', 'name','start_date','end_date','status', 'job','location',)
    list_filter = ('badge', 'name','start_date','end_date','status', 'job','location',)
    search_fields = ('badge', 'name','start_date','end_date', 'job','location',)
    

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