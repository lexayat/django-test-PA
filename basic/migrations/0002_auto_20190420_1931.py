# Generated by Django 2.1.1 on 2019-04-20 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tusa',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 20, 19, 31, 14, 110038)),
        ),
    ]
