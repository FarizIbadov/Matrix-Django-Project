from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, DateWidget

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

# Register your models here.

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


class TrainingMatrixResource(resources.ModelResource):
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
        model=TrainingMatrix
        exclude=('id',)
        import_id_fields = ('department', 'position',)
        fields = ('department','position','job',)

@admin.register(TrainingMatrix)
class TrainingMatrixAdmin(ImportExportModelAdmin):
    list_display = ('id','department', 'position','get_training','job',)
    search_fields = ('department__department','position__position',)
    filter_horizontal = ('training',)
    list_filter = ('department__department','position__position',)
    resource_class = TrainingMatrixResource    
    skip_unchanged = True
    report_skipped = False

    def get_training(self, instance):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((line,) for line in instance.get_training()),
        ) or mark_safe("<span class='errors'>Training is not assigned yet.</span>")
    get_training.short_description = 'Training'


class EmployeeResource(resources.ModelResource):
    start_date = fields.Field(
        attribute='start_date', 
        column_name='start_date', 
        widget=DateWidget('%d/%m/%Y')) 
    cost_code = fields.Field(
        column_name='cost_code',
        attribute='cost_code',
        widget=ForeignKeyWidget(Location, 'cost_code'))
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget=ForeignKeyWidget(Department, 'department'))
    position = fields.Field(
        column_name='position',
        attribute='position',
        widget=ForeignKeyWidget(Position, 'position'))
    job = fields.Field(
        column_name='job',
        attribute='job',
        widget=ForeignKeyWidget(TrainingMatrix, 'job'))

    class Meta:
        model=Employee
        exclude = ('id',)
        import_id_fields = ('badge',)
        fields = ('badge', 'name','start_date','end_date','status','cost_code', 'department', 'position','job',)

    
    def before_save_instance(self, instance, using_transactions, dry_run):
        if instance.job == TrainingMatrix.job:
            return instance
            

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    def project(self, obj):
        return obj.cost_code.project

    def required_training(self, instance):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((line,) for line in instance.job.training.all()),
        ) or mark_safe("<span class='errors'>Training is not assigned yet.</span>")
    required_training.short_description = 'Mandatory Training'


    resource_class=EmployeeResource
    # readonly_fields = ('badge',)
    list_display = ('badge', 'name','start_date','end_date','status','cost_code', 'project','department', 'position','ifmt','ifmt_status','required_training',)
    list_select_related = ['cost_code']
    list_filter = ('status','ifmt_status','cost_code__cost_code','cost_code__project',)
    search_fields = ('badge', 'name','start_date','end_date','cost_code__cost_code','cost_code__project','position__position', 'department__department','job__job',)

class RequiredTrainingResource(resources.ModelResource):
   
    badge = fields.Field(
        column_name='badge',
        attribute='badge',
        widget=ForeignKeyWidget(Employee, 'badge'))
    training = fields.Field(
        column_name='training',
        attribute='training',
        widget=ForeignKeyWidget(TrainingMatrix, 'training'))


    class Meta:
        model=RequiredTraining
        exclude = ('id',)
        import_id_fields = ('badge',)
        fields = ('badge', 'training',)


@admin.register(RequiredTraining)
class RequiredTrainingAdmin(ImportExportModelAdmin):

    resource_class=RequiredTrainingResource
    list_display = ('badge','training',)


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
