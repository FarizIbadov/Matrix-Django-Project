# Generated by Django 3.0.4 on 2020-04-26 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0036_auto_20200426_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequiredTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='badgenumber', to='training.Employee')),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.TrainingMatrix')),
            ],
            options={
                'verbose_name': 'Required Training',
                'verbose_name_plural': 'RequiredTraining',
                'ordering': ('badge',),
            },
        ),
    ]