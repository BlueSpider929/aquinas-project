# Generated by Django 2.1.7 on 2019-03-01 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0013_auto_20190302_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 3, 10, 50, 552260)),
        ),
    ]