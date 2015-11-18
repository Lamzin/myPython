# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layouts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proceed_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('proceed_default', models.CharField(max_length=64)),
                ('proceed_bfs', models.CharField(max_length=64)),
            ],
        ),
    ]
