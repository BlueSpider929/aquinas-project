# Generated by Django 2.1.7 on 2019-03-01 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0010_auto_20190302_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 2, 31, 57, 920296)),
        ),
    ]