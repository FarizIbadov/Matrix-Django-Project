from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from django.db.models.signals import post_save, pre_save

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
        return self.cost_code

    class Meta:
        ordering=('project', 'cost_code',)
        verbose_name='Location'
        verbose_name_plural='Locations'

class Department(models.Model):
    department = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.department or ''

    class Meta:
        ordering=('department',)
        verbose_name='Department'
        verbose_name_plural='Departments'

class Position(models.Model):
    position = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.position or ''

    class Meta:
        ordering=('position',)
        verbose_name='Position'
        verbose_name_plural='Positions'


class TrainingMatrix(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=False, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,blank=False, null=True)
    training = models.ManyToManyField(Training)
    job = models.CharField(max_length=300, null=True, unique=True)

    def get_training(self):
        return [p.title for p in self.training.all()]
        # return [p.title for p in self.training.all()][:3]

    def display_eqpm_training(self):
        tr = set()
        for training in self.training.all().filter(training_group__title="Equipment"):
            tr.add(training.title)
        if tr:
            return tr
        else:
            return "N/A"

    def display_sys_training(self):
        tr = set()
        for training in self.training.all().filter(training_group__title="System"):
            tr.add(training.title)
        if tr:
            return tr
        else:
            return "N/A"

    def display_thr_training(self):
        tr = set()
        for training in self.training.all().filter(training_group__title="Theoretical"):
            tr.add(training.title)
        if tr:
            return tr
        else:
            return "N/A"

    def display_prdt_training(self):
        tr = set()
        for training in self.training.all().filter(training_group__title="Product knowledge"):
            tr.add(training.title)
        if tr:
            return tr
        else:
            return "N/A"
  
    # get_training.allow_tags = True

    def __str__(self):
        return str(self.department.department) + str(" - ") + str(self.position.position)

    class Meta:
        ordering=('department', 'position',)
        verbose_name='Training Assignement'
        verbose_name_plural='Training Matrix'
        constraints = [
            models.UniqueConstraint(fields=['department', 'position'], name='job')
        ]

class Employee(models.Model):
    badge = models.CharField(max_length=15, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=True)
    end_date = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(choices=(
        (True, 'Active'), 
        (False, 'Inactive')
        ), default=True)
    cost_code = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True, related_name='costCode')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True,related_name='department_name')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True,related_name='position_title')
    training = models.ForeignKey(TrainingMatrix, to_field='job', on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(TrainingMatrix, on_delete=models.CASCADE, blank=True,null=True, related_name='checkjob')
    ifmt = models.FileField(upload_to='IFMT', blank=True, null=True)
    ifmt_status = models.BooleanField(choices=(
        (True, 'Submited'), 
        (False, 'Required')
        ), default=False)

    def __str__(self):
        return str(self.badge)+ str(" - ") + str(self.name)


    def save(self, *args, **kwargs):
        if self.end_date is None:
            self.status = 1
        else:
            self.status = 0
        if self.ifmt:
            self.ifmt_status = 1
        else:
            self.ifmt_status=0
        # if self.department.department == TrainingMatrix.department.department and self.position == TrainingMatrix.position:
        #     self.training = TrainingMatrix.training
        # else:
        #     self.training = "no"

        super(Employee, self).save(*args, **kwargs)


    class Meta:
        ordering=('name', 'badge', 'start_date', 'status',)
        verbose_name='Employee'
        verbose_name_plural='Employees'

class RequiredTraining(models.Model):
    badge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='badgenumber')
    training = models.ForeignKey(TrainingMatrix, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.badge)+ str(" - ")


    def save(self, *args, **kwargs):
        if self.badge.department == TrainingMatrix.department and self.badge.position == TrainingMatrix.position :
            self.training = TrainingMatrix.training
        else:
            self.training=TrainingMatrix.department.department

        super(RequiredTraining, self).save(*args, **kwargs)


    class Meta:
        ordering=('badge', )
        verbose_name='Required Training'
        verbose_name_plural='RequiredTraining'



