# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20150907_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='instructor',
            field=models.CharField(default=b'', max_length=20, null=True, blank=True),
        ),
    ]
