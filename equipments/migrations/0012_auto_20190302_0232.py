# Generated by Django 2.1.7 on 2019-03-01 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0011_auto_20190302_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 2, 32, 19, 242342)),
        ),
    ]
