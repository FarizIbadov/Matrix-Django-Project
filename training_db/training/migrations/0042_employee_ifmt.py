# Generated by Django 3.0.4 on 2020-04-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0041_auto_20200428_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ifmt',
            field=models.FileField(null=True, upload_to='IFMT'),
        ),
    ]
