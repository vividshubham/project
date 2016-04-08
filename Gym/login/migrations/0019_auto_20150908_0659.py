# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20150908_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='instructor',
            field=models.ForeignKey(related_name='instruct', blank=True, to='login.UserProfile', null=True),
        ),
    ]
