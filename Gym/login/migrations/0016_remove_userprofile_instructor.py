# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_instructors_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='instructor',
        ),
    ]
