# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150907_1546'),
    ]

    operations = [
        migrations.DeleteModel(
            name='extras',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
