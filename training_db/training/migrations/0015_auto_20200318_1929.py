# Generated by Django 2.2.8 on 2020-03-18 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_auto_20200229_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('project', 'cost_code'), 'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='project',
        ),
    ]
