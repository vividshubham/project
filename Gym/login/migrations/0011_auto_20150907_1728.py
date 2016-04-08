# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_extras_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='instructor',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
