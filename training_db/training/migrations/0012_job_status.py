# Generated by Django 2.2.8 on 2020-02-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_job_training'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.BooleanField(choices=[(True, 'R'), (False, 'N/R')], default=False),
        ),
    ]