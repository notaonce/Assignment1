# Generated by Django 4.0.3 on 2022-04-10 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='d_day',
            field=models.DateField(default=datetime.datetime(2022, 4, 10, 8, 29, 57, 653484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 8, 29, 57, 653244, tzinfo=utc)),
        ),
    ]