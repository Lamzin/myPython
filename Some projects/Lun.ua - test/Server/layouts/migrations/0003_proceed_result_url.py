# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layouts', '0002_proceed_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceed_result',
            name='url',
            field=models.URLField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
