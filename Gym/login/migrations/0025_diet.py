# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_auto_20150923_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=15)),
                ('meal', models.CharField(max_length=50)),
                ('food_type', models.CharField(max_length=100)),
                ('diet', models.TextField()),
            ],
        ),
    ]
