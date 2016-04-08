# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='day',
            field=models.CharField(max_length=15, choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Friday', b'Friday'), (b'Saturday', b'Saturday'), (b'Sunday', b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='diet',
            name='meal',
            field=models.CharField(max_length=50, choices=[(b'Early Morning', b'Early Morning'), (b'Breakfast', b'Breakfast'), (b'Mid-Morning', b'Mid-Morning'), (b'Lunch', b'Lunch'), (b'Tea and Snacks', b'Tea and Snacks'), (b'Dinner', b'Dinner'), (b'Bedtime', b'Bedtime')]),
        ),
    ]
