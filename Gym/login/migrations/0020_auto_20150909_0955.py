# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20150908_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='diet',
            field=models.TextField(default=b'', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exercises',
            field=models.TextField(default=b'', null=True, editable=False, blank=True),
        ),
    ]
