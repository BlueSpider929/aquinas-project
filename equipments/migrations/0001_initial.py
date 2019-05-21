# Generated by Django 2.1.7 on 2019-02-28 18:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultants', '0002_auto_20190301_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=200)),
                ('equipment_type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('driver', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 1, 2, 7, 7, 568780))),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='consultants.Consultant')),
            ],
        ),
    ]