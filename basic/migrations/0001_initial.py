# Generated by Django 2.1.1 on 2019-04-21 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tusa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('lat', models.FloatField(blank=True, default=None, null=True)),
                ('lng', models.FloatField(blank=True, default=None, null=True)),
                ('mens', models.IntegerField(default=0)),
                ('girls', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 4, 27, 10, 10, 3))),
                ('type', models.CharField(default='1', max_length=20)),
                ('tags', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='tusa',
            unique_together={('name',)},
        ),
    ]
