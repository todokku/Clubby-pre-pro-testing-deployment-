# Generated by Django 3.0.3 on 2020-02-29 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of your club.', max_length=50)),
                ('address', models.CharField(help_text='Enter the full address so google maps can find it.', max_length=200)),
                ('max_capacity', models.IntegerField(help_text="The capacity of your club, you're responsible for the enforcement of this number.")),
                ('NIF', models.CharField(help_text='Company number for the club', max_length=10)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('event_type', models.CharField(blank=True, choices=[('p', 'payed'), ('f', 'free')], default='m', help_text='event type', max_length=1)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Club')),
            ],
        ),
    ]