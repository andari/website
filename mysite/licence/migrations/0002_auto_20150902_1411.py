# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='licence_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('licence_number', models.CharField(max_length=20)),
                ('scan_time', models.DateTimeField(verbose_name=b'date_published')),
            ],
        ),
        migrations.DeleteModel(
            name='licence',
        ),
    ]
