# Generated by Django 2.2.8 on 2020-02-29 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_employee_training_traininggroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.Department')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.Position')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'ordering': ('department', 'position'),
            },
        ),
    ]
