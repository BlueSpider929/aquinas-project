# Generated by Django 2.1.7 on 2019-03-01 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0007_auto_20190301_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 1, 23, 31, 30, 986394)),
        ),
    ]
