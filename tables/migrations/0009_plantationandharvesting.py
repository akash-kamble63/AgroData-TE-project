# Generated by Django 4.0.1 on 2022-06-05 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0008_alter_crop_avgplanthei_alter_crop_croptype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='plantationandharvesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('plotid', models.CharField(blank=True, max_length=60)),
                ('cropid', models.CharField(blank=True, max_length=60)),
                ('dateofpreparation', models.CharField(blank=True, max_length=60)),
                ('dateofplantation', models.CharField(blank=True, max_length=60)),
                ('startofharvesting', models.CharField(blank=True, max_length=60)),
                ('endofharvesting', models.CharField(blank=True, max_length=60)),
                ('currentharvest', models.CharField(blank=True, max_length=60)),
                ('previousharvest', models.CharField(blank=True, max_length=60)),
                ('accumulatedharvest', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
