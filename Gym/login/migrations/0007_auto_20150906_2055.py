# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20150906_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberinfo',
            name='member',
        ),
        migrations.DeleteModel(
            name='MemberInfo',
        ),
    ]
