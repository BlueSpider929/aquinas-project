# Generated by Django 2.1.7 on 2019-02-28 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0002_auto_20190301_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 1, 2, 27, 44, 979794)),
        ),
    ]
