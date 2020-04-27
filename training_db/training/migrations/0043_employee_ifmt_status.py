# Generated by Django 3.0.4 on 2020-04-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0042_employee_ifmt'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ifmt_status',
            field=models.BooleanField(choices=[(True, 'Submited'), (False, 'Required')], default=True),
        ),
    ]
