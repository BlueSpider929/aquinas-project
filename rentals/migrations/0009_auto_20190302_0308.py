# Generated by Django 2.1.7 on 2019-03-01 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0008_auto_20190302_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 3, 8, 44, 108631)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='equipment_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
