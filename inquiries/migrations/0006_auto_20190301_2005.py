# Generated by Django 2.1.7 on 2019-03-01 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0005_auto_20190301_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 1, 20, 5, 31, 372158)),
        ),
    ]
