# Generated by Django 2.1.7 on 2019-03-01 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0007_auto_20190301_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 1, 8, 46, 827)),
        ),
    ]
