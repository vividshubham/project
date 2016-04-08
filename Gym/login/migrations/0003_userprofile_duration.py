# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userprofile_bloodgrp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='duration',
            field=models.CharField(default='30', max_length=3, choices=[(b'30', b'30'), (b'60', b'60'), (b'90', b'90'), (b'180', b'180'), (b'365', b'365')]),
            preserve_default=False,
        ),
    ]
