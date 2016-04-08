# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_auto_20150923_2134'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diet',
        ),
    ]
