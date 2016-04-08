# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20150909_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructors',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='members',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='members',
            name='member',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instructor',
            field=models.ForeignKey(related_name='instruct', default=b'', blank=True, to='login.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='members',
            field=models.ForeignKey(related_name='membs', default=b'', blank=True, to='login.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=' ', max_length=70),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='instructors',
        ),
        migrations.DeleteModel(
            name='members',
        ),
    ]
