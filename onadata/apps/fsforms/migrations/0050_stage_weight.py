# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsforms', '0050_auto_20180309_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
