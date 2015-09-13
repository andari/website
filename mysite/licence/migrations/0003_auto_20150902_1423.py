# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licence', '0002_auto_20150902_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licence_model',
            name='scan_time',
            field=models.CharField(max_length=20),
        ),
    ]
