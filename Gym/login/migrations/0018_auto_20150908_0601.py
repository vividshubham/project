# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_userprofile_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='instructor',
        ),
        migrations.AlterField(
            model_name='members',
            name='instructor',
            field=models.ForeignKey(related_name='instruct', to='login.UserProfile'),
        ),
        migrations.AlterField(
            model_name='members',
            name='member',
            field=models.ForeignKey(related_name='membs', to='login.UserProfile'),
        ),
    ]
