# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_remove_userprofile_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instructor',
            field=models.ForeignKey(blank=True, to='login.UserProfile', null=True),
        ),
    ]
