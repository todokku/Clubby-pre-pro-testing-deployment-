# Generated by Django 3.0.3 on 2020-03-03 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0005_auto_20200301_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'permissions': (('can_add_event', 'Set event to be had.'),)},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('can_mark_assistance', 'Set event to assist.'),)},
        ),
    ]
