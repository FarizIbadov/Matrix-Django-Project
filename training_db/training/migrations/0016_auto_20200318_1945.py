# Generated by Django 2.2.8 on 2020-03-18 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0015_auto_20200318_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('title',), 'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.RenameField(
            model_name='position',
            old_name='name',
            new_name='title',
        ),
    ]
