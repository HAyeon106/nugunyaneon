# Generated by Django 4.0.5 on 2022-06-11 07:02

import django.contrib.postgres.fields
from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisModel',
            fields=[
                ('fileId', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('fileName', models.TextField(null=True)),
                ('filePath', models.TextField(null=True)),
                ('file', models.FileField(null=True, upload_to='audiofiles/')),
                ('error', models.CharField(max_length=100, null=True)),
                ('probability', models.FloatField()),
                ('phishingType', models.CharField(max_length=50, null=True)),
                #('words', models.JSONField(default=dict)),
                ('isAllowed', models.BooleanField(default=False)),
            ],
        ),
    ]
