# Generated by Django 3.0.4 on 2020-03-24 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0023_job_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.Job'),
        ),
        migrations.DeleteModel(
            name='Matrix',
        ),
    ]
