# Generated by Django 3.0.4 on 2020-04-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0031_employee_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='end_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
