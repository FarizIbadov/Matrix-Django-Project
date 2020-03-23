# Generated by Django 2.2.8 on 2020-03-23 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0020_auto_20200322_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='department',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training.Department'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training.Position'),
        ),
    ]
